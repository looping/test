from bottle import route
import c
@route('/')
def r():
	return c.hello() 
@route('/p/<title>/<content>', method='GET')
def p(title, content):
	return c.save_post(title, content)
@route('/g')
def g():
	return c.show_post()
