from bottle import route, view, request, template
import c

@route('/sd')
@view('t/logout')
def sd():
	s = request.environ.get('beaker.session')
	token = s.get('public_token')
	if token:
		#c.logout()
		s.delete()
	return dict() 

@route('/si')
@view('t/sign_ui')
def s():
	return dict()

@route('/e', method = 'get')
@view('t/send_email_done')
def se():
	email = request.query.get('ail')
	return c.send_ui_email(email)

@route('/c', method = 'get')
@view('t/auth_email_code')
def co():
	code = request.query.get('de')
	s = request.environ.get('beaker.session')
	s['public_token'] = code
	return c.auth_email_code(code) 

@route('/')
@view('t/post_list')
def r():
	s = request.environ.get('beaker.session')
	public_token = s.get('public_token')
	if public_token == None or c.auth_public_token(public_token) == 'NO':
		return '<a href ="./si">Sign UI</a>'
	else:
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
