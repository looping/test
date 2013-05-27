#coding: utf-8
import m
from bottle import route, run, template
#from bottle import route, run, app, request
"""
from beaker.middleware import SessionMiddleware
from gevent import monkey; 
monkey.patch_all()
import time 
@route('/stream')
def stream():
	yield 'start'
	time.sleep(2)
	yield 'middle'
	time.sleep(3)
	yield 'end'
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app().catchall = True
app = SessionMiddleware(app(), session_opts)
"""
@route('/')
def hello():
    #return '<h1>Hello %s!</h1>' % name.title()
	m.db.connect()
	"""
	iuser = m.User()
	iuser.username = "Looping"
	iuser.name = "Looping"
	iuser.password = "Looping"
	iuser.last_login = "Looping"
	iuser.save()
	"""
	users = m.User().select().limit(10)
	m.db.close()
	username = ''
	for user in users:
		 username = username + user.username		
	
	return template('<b>Hello {{name}}</b>!', name=username)
@route('/post/<title>/<content>')
def save_post(title, content):
	m.db.connect()
	blog = m.Blog()
	blog.title = title
	blog.content = content
	blog.save()
	m.db.close()
	return 'saved'
@route('/show/<page>')
@route('/show')
def show_post(page = 0):
	page_index = int(page)
	m.db.connect()
	#blogs = m.Blog.select().limit(20)
	showblog = 'Blog list'
	for blog in m.Blog.raw('select * from blog limit %d, 10'% page_index):
		showblog = showblog + "<br />" + blog.title + " | " + blog.content
	return showblog

"""
@route('/test')
def test():
  s = request.environ.get('beaker.session')
  s['test'] = s.get('test',0) + 1
  s.save()
  return 'Test counter: %d' % s['test']
"""
#run(app=app, host='0.0.0.0', port=8880)
#run(app=app, server='tornado', host='0.0.0.0', port=8880)
#run(server='bjoern', host='0.0.0.0', port=8888, app=app)
run(server='bjoern', host='0.0.0.0', port=8888)
