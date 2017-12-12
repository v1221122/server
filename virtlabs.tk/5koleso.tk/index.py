import api
from livereload import Server

app = api.app

app.debug = True

server = Server(app.wsgi_app)
server.serve()