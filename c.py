#coding: utf-8
import cs
import conf
def gentoken_by_namepwd(username, password):
	return 'Gentoken, done'

def testoken(token):
	return token

def get_value_by_key(key):
	return 'value'

def set_value_by_key(key, value):
	return 'Set k-v, done!'
##
#Just a cache tester, Memcached, Redis...
##
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
