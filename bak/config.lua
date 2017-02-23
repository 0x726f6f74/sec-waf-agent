-- Copyright (C) Bingli
--WAF config file,enable = "on",disable = "off"

--waf status
config_waf_enable = "on"
--enable/disable white url
config_white_url_check = "on"
--enable/disable white ip
config_white_ip_check = "on"
--enable/disable block ip
config_black_ip_check = "on"
--enable/disable url filtering
config_url_check = "on"
--enalbe/disable url args filtering
config_url_args_check = "on"
--enable/disable user agent filtering
config_user_agent_check = "on"
--enable/disable cookie deny filtering
config_cookie_check = "on"
--enable/disable cc filtering
config_cc_check = "on"
--cc rate the xxx of xxx seconds
config_cc_rate = "100/60"
--enable/disable post filtering
config_post_check = "on"
--config waf output redirect/html
config_waf_output = "html"
--if config_waf_output ,setting url
config_waf_redirect_url = "http://www.jianshu.com/users/d484ac7f2c2c/latest_articles"
config_output_html=[[
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="Content-Language" content="zh-cn" />
<title>403</title>
</head>
<body>
<h1 align="center"> Forbidden !!! Please contact:<a href="mailto:security@lagou.com ">Lagou-Sec</a></h1>
</body>
</html>
]]


--[[
--this is configure and rule information
function get_config()
	local redis = require "resty.redis"
	local red = redis.new()
	red:set_timeout(200)
	-- red.connect(red, '127.0.0.1', '6379')
	local ok, err = red:connect("10.1.200.85", 6379)
	if not ok then
	    ngx.say(ngx.WARN, "Redis connection error retrieving banned_ips: " .. err)
	else
	    local updated_banned_ips, errs = red:smembers('waf_config')
	    if not errs then
	        ngx.say(updated_banned_ips)
	    else
	        ngx.say(errs)
	    end
	end
end
--]]
