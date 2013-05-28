#coding: utf-8
import m

from bottle import template

def hello():
#	m.db.connect()
	users = m.User().select().limit(10)
#	m.db.close()
	username = ''
	for user in users:
		 username = username + user.username		
	
	return template('<b>Hello {{name}}</b>!', name=username)

def save_post(title = ' ', content = ' '):
#	m.db.connect()
	status = 'OK'
	try:
		blog = m.Blog()
		blog.title = title
		blog.content = content
		blog.save()
	except:
		status = 'NO'
#	m.db.close()
	return dict(post_status = status, title = title, content = content)

def list_post(page = 0):
	page_index = int(page)
	m.db.connect()
	blogs = m.Blog.select().limit(20).order_by(m.Blog.title.desc())
	showblog = 'Blog list'
	return dict(blogs = blogs)

def show_post_form():
	return 'hi'
