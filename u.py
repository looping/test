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

