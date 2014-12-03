from pyramid.view import view_config
from pyramid.response import Response
from pyramid.renderers import render

@view_config(route_name='home')#,renderer='templates/poo.pt')
def my_view(request):
	result = render('myproject:templates/poo.pt',{'a':'1'},request=request)
	response = Response(result)
	response.content_type = 'text/plain'
	return response
	#return {'project':'MyProject'}

@view_config(route_name="hello",renderer='json')
def hello_world(request):
	return u'ok',{'content':'Hello!'}

