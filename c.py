#coding: utf-8
import m
import cs
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

def test_redis_set(key = ' ', value = ' '):
	r = cs.useredis()
	r.set(key, value)
	return r.get(key)

def test_redis_get(key):
	r = cs.useredis()
	return r.get(key)

def test_memcache_set(key = ' ', value = ' '):
	m = cs.usememcache()
	m.set(key, value)
	return m.get(key)

def test_memcache_get(key):
	m = cs.usememcache()
	m.disconnect_all()
	return m.get(key)
