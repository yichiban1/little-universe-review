"""Local native-video QA server with byte-range support for browser seeks."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

class RangeHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        target = Path(self.translate_path(self.path))
        value = self.headers.get('Range', '')
        match = re.fullmatch(r'bytes=(\d*)-(\d*)', value)
        if not match or not target.is_file():
            return super().do_GET()
        size = target.stat().st_size
        a, b = match.groups()
        start = int(a) if a else max(0, size-int(b))
        end = min(size-1, int(b)) if a and b else size-1
        if start > end or start >= size:
            self.send_response(416)
            self.send_header('Content-Range', f'bytes */{size}')
            self.end_headers()
            return
        self.send_response(206)
        self.send_header('Content-Type', self.guess_type(str(target)))
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Content-Range', f'bytes {start}-{end}/{size}')
        self.send_header('Content-Length', str(end-start+1))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        with target.open('rb') as stream:
            stream.seek(start)
            remaining = end-start+1
            try:
                while remaining:
                    block = stream.read(min(131072, remaining))
                    if not block:
                        break
                    self.wfile.write(block)
                    remaining -= len(block)
            except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
                pass

if __name__ == '__main__':
    ThreadingHTTPServer(('127.0.0.1', 8817), RangeHandler).serve_forever()
