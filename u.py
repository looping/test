from bottle import route, view, request, template
import c

@route('/')
@view('t/post_list')
def r():
	return c.list_post() 

@route('/p')
@view('t/post_form')
def p():
	return dict()

@route('/ps', method = 'post')
@view('t/post_result')
def ps():
	title = request.forms.get('title')
	content = request.forms.get('content')
	return c.save_post(title, content)

@route('/t/r/s/<key>/<value>')
def trs(key, value):
	return c.test_redis_set(key, value)

@route('/t/r/g/<key>')
def trg(key):
	return c.test_redis_get(key)

@route('/t/m/s/<key>/<value>')
def tms(key, value):
	return c.test_memcache_set(key, value)

@route('/t/m/g/<key>')
def tmg(key):
	return c.test_memcache_get(key)
