#coding: utf-8
from bottle import route, view, request, template
import c
@route('/')
def root():
	return 'NO ACCESS!'

@route('/auth/gentoken/<username>/<password>')
def gentoken(username, password):
	return c.gentoken_by_namepwd(username, password)

@route('/auth/testoken/<token>')
def testoken(token):
	return c.testoken(token)

@route('/requ/<token>/<key>')
def requests(token, key):
	if testoken(token) == False:
		status = 1
	else:
		return c.get_value_by_key(key)
@route('/push/<token>/<key>', method = 'post')
def pushes(token, key):
	if testoken(token) == False:
		status = 1
	else:
		value = request.forms.get('value')
		return c.set_value_by_key(key, value)

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
