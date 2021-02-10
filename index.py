import tornado.ioloop
import tornado.web


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(
            "Hello, World this is a python command executed from the backend")


class htmlRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/html", htmlRequestHandler)
    ])

    port = 8080

    app.listen(port)
    print(f"this app is listening on port {port}")
    tornado.ioloop.IOLoop.current().start()
