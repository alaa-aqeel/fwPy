from werkzeug.serving import run_simple
from .wrappers_mvc import Response,Request

class server:

	def main_app(self, environ, start_response):
		request = Request(environ)
		# request.pkg = self.pkg
		response = Response(request.resp_ctx())

		response.setCookies(request.req__cookie)
		
		return response(environ, start_response)

	def __call__(self, environ, start_response):
		return self.main_app(environ, start_response)


	def runserver(self,port=80,host='localhost',debug=True,auto_reloader=True):
		run_simple(host, port, self , use_debugger=debug, use_reloader=auto_reloader)
