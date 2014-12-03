from wsgiref.simple_server import make_server
from pyramid.config  import  Configurator
from pyramid.request  import Request

def view_one(request):
	subreq = Request.blank('/view_two')
	response = request.invoke_subrequest(subreq,use_tweens=True)
	return response

def view_two(request):
	#request.response.body = 'This came from view_two'
	#return request.response
	#return 'sdsffsdf two'
	raise ValueError('foo')

def excview(request):
	request.response.body = b'An exception was raised'
	request.response.status_int = 500
	return request.response

if __name__ == '__main__':
	config = Configurator()
	config.add_route('one','/view_one')
	config.add_route('two','/view_two')
	config.add_view(view_one,route_name='one')
	config.add_view(view_two,route_name='two',renderer='string')
	config.add_view(excview,context=Exception)
	app = config.make_wsgi_app()
	server = make_server('0.0.0.0',8080,app)
	server.serve_forever()

