import os
import sys


def create():
    from sqlalchemy import Table
    import model
    for (name, table) in vars(model).iteritems():
        if isinstance(table, Table):
            table.create()


def createtestdata():
    import model
    i = model.entry_table.insert()
    i.execute(
        id='1', title="Some Text", content='Some pithy text...',
        updated='2016-11-30T01:00:01Z')
    i.execute(
        id='2', title="Some Word", content='Some pithy word...',
        updated='2016-11-30T02:00:01Z')


def run():
    import urls
    if os.environ.get('REQUEST_METHOD', ''):
        from wsgiref.handlers import BaseCGIHandler
        BaseCGIHandler(
            sys.stdin, sys.stdout, sys.stderr, os.environ).run(urls.urls)
    else:
        from wsgiref.simple_server import WSGIServer, WSGIRequestHandler
        httpd = WSGIServer(('', 8080), WSGIRequestHandler)
        httpd.set_app(urls.urls)
        print "Server HTTP on %s port %s..." % httpd.socket.getsockname()
        httpd.serve_forever()


if __name__ == '__main__':
    if 'create' in sys.argv:
        create()
    if 'run' in sys.argv:
        run()
    if 'createtestdata' in sys.argv:
        createtestdata()
