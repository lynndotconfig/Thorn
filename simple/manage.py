"""Usage.

$ python manage.py run
"""
import os
import sys


def run():
    import app
    if os.environ.get('REQUEST_METHOD', ''):
        from wsgiref.handlers import BaseCGIHandler
        BaseCGIHandler(
            sys.stdin, sys.stdout, sys.stderr, os.environ).run(app.application)
    else:
        from wsgiref.simple_server import WSGIServer, WSGIRequestHandler
        httpd = WSGIServer(('', 8080), WSGIRequestHandler)
        httpd.set_app(app.application)
        print "Server HTTP on %s port %s..." % httpd.socket.getsockname()
        httpd.serve_forever()


if __name__ == '__main__':
    if 'run' in sys.argv:
        run()
