#coding: utf-8
import m

from bottle import template

def hello():
#	m.db.connect()
	users = m.Blog().select().limit(10)
#	m.db.close()
	username = ''
	for user in users:
		 username = username + user.username		
	
	return template('<b>Hello {{name}}</b>!', name=username)

def save_post(title = ' ', content = ' '):
	m.db.connect()
	blog = m.Blog()
	blog.title = title
	blog.content = content
	blog.save()
	m.db.close()
	return 'saved'

def show_post(page = 0):
	page_index = int(page)
	m.db.connect()
	#blogs = m.Blog.select().limit(20)
	showblog = 'Blog list'
	for blog in m.Blog.raw('select * from blog limit %d, 10'% page_index):
		showblog = showblog + "<br />" + blog.title + " | " + blog.content
	return showblog

