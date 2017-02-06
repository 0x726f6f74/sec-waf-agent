import redis

pool = redis.ConnectionPool(host='10.1.200.85', port=6379) #, password="1234qwer~",db=1
r = redis.Redis(connection_pool=pool)
r.sadd("waf_config",{"config_white_url_check" : "on","config_waf_enable" : "on"})

