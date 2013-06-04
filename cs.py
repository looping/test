import redis
import memcache
pool = redis.ConnectionPool(host='0.0.0.0', port=6379, db=0)
mc = memcache.Client(['0.0.0.0:11211'])
def useredis():
	return redis.Redis(connection_pool=pool)

def usememcache():
	return mc
