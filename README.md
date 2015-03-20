# demo_prd
pyramid dem

pyramid 入门
1.简单例子
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

2.安装
docs.pylonsproject.org/projects/pyramid/en/1.4-branch/narr/install.html#installing-pyramid-on-a-unix-system
3.
$ bin/pcreate -s starter MyProject
$ bin/pcreate -s alchemy MyProject
$ cd MyProject
$ ../bin/python setup.py develop
$ ../bin/pserve development.ini
$ ../bin/pserve development.ini --reload

3.路由添加
config.add_route('hello', '/hello/{name}')
hello 视图名字   '/hello/{name}'  访问路径

4.添加视图装饰器
@view_config(renderer='json') 渲染返回成json串
@view_config(route_name='')   视图路由名字
@view_config(renderer='string')  返回字符串
@view_config(renderer='templates/mytemplate.jinja2') 使用模板渲染

@view_defaults(route_name='') 类的视图
@view_config(request_method = 'GET', renderer = 'json') 修饰类中的函数
 
5.pyhton class中默认调用__call__() 函数
