#coding: utf-8
import m
from bottle import route, run, template
#from bottle import route, run, app, request

@route('/')
def hello():
    #return '<h1>Hello %s!</h1>' % name.title()
	m.db.connect()
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

#run(app=app, host='0.0.0.0', port=8880)
#run(app=app, server='tornado', host='0.0.0.0', port=8880)
#run(server='bjoern', host='0.0.0.0', port=8888, app=app)
run(server='bjoern', host='0.0.0.0', port=8888)
