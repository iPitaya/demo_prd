from pyramid.config import Configurator
from pyramid.view import notfound_view_config,view_config,view_defaults
from pyramid.response import Response
import models

'''
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
'''


@view_config(route_name='noslash')
def no_slash(request):
	name_value = models.get_name_value()
	for dt in name_value:
		print dt.name,dt.value
	return Response('No slash')

@view_config(route_name='hasslash')
def has_slash(request):
	request.response.set_cookie('abc','123')
	request.response.body = 'Has slash'
	#return Response('Has slash')
	return request.response

def main(global_config,**settings):
	config = Configurator()
	config.include('pyramid_chameleon')
	config.add_route('noslash','/no_slash')
	config.add_route('hasslash','/has_slash/')
	config.add_route('home','/')
	config.add_route('hello','/hello/')
	config.add_route('first','/first/')
	config.scan()
	return config.make_wsgi_app()
