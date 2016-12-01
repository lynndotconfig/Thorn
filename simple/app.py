import re


# def application(environ, start_response):
#     """Simple possible application object."""
#     status = '200 OK'
#     response_headers = [('Content-Type', 'text/plain')]
#     start_response(status, response_headers)
#     return ['Hello World\n']


class WSGIApp:

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):

        try:
            response = self.delegate()
        except Exception:
            return self.get_response(*self.internalerror())
        return self.get_response(*response)

    def delegate(self):
        path_info = self.environ['PATH_INFO']
        method = self.environ['REQUEST_METHOD']

        for pattern, name in self.urls:
            m = re.match("^" + pattern + '$', path_info)
            if m:
                args = m.groups()
                funcname = method.lower() + "_" + name
                func = getattr(self, funcname)
                return func(*args)
        return self.notfound()

    def get_response(self, status, response):
        if status is None:
            status = '200 OK'
        response_headers = [('Content-Type', 'text/plain')]
        self.start(status, response_headers)
        yield response


    def notfound(self):
        return ('404 Not Found', "Not Found\n")

    def internalerror(self):
        return '500 Internal Error', "Internal Error"


class application(WSGIApp):

    urls = [
        ("/", "index"),
        ("/hello", "hello"),
        ("/list", "list"),
    ]


    def get_index(self):
        return None, "Welcom!\n"

    def get_hello(self):
        return None, "Hello World!\n"

    def get_list(self):
        return None, "There are my list!\n"
