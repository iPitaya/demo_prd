from pyramid.response  import Response
from pyramid.view  import  view_config,view_defaults
import oauth2

#@view_defaults(route_name = 'first')
class AView(object):
	def __init__(self,request):
		self.request = request

	#@view_config(request_method = 'GET')
	@oauth2.check_permission
	@view_config(route_name = 'first')
	def first(self):
		id = self.request.params.get('id','')
		print id
		return Response('first')

