from bottle import route
import c
@route('/')
def root():
	return c.hello() 
