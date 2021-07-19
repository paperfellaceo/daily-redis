import redis
redis = redis.Redis(host='localhost', port=6379, db=0)
redis.smembers('circle:jdoe:soccer')
redis.sadd('circle:jdoe:soccer', 'users:fred')
redis.smembers('circle:jdoe:soccer')
