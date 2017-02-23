-- Copyright (C) Bingli

--waf core lib
require 'config'

--Get the client IP
function get_client_ip()
    CLIENT_IP = ngx.req.get_headers()["X_real_ip"]
    if CLIENT_IP == nil then
        CLIENT_IP = ngx.req.get_headers()["X_Forwarded_For"]
    end
    if CLIENT_IP == nil then
        CLIENT_IP  = ngx.var.remote_addr 
    end
    if CLIENT_IP == nil then
        CLIENT_IP  = "unknown"
    end
    return CLIENT_IP
end

--Get the client user agent
function get_user_agent()
    USER_AGENT = ngx.var.http_user_agent
    if USER_AGENT == nil then
       USER_AGENT = "unknown"
    end
    return USER_AGENT
end

--Get WAF rule
function get_rule(rulefilename)
    local io = require 'io'
    local RULE_PATH = "/usr/local/nginx/nginx/conf/waf/rule-config"
    local RULE_FILE = io.open(RULE_PATH..'/'..rulefilename,"r")
    if RULE_FILE == nil then
        return
    end
    RULE_TABLE = {}
    for line in RULE_FILE:lines() do
        table.insert(RULE_TABLE,line)
    end
    RULE_FILE:close()
    return(RULE_TABLE)
end

-- WAF record
function log_record(method,url,data,ruletag)
            local cjson = require "cjson"  
            local producer = require "resty.kafka.producer"  
            local broker_list = {  
                { host = "10.1.200.120", port = 9092 },  
            }
            local CLIENT_IP = get_client_ip()
            local USER_AGENT = get_user_agent()
            local SERVER_NAME = ngx.var.server_name
            local LOCAL_TIME = ngx.localtime()
            local log_json_obj = {
                         client_ip = CLIENT_IP,
                         local_time = LOCAL_TIME,
                         server_name = SERVER_NAME,
                         user_agent = USER_AGENT,
                         attack_method = method,
                         req_url = url,
                         req_data = data,
                         rule_tag = ruletag,  
                      }
            local io = require 'io'
            local LOG_PATH = "/tmp"
            local LOG_LINE = cjson.encode(log_json_obj)
            local LOG_NAME = LOG_PATH..'/'..ngx.today().."_waf.log"
            local file = io.open(LOG_NAME,"a")

            local bp = producer:new(broker_list, { producer_type = "async" })
            local ok, err = bp:send("waf_logger", nil, LOG_LINE)  

            if not ok then  
                file:write(err.."\n")
                file:flush()
                file:close()  
                return  
            end
end

--WAF return
function waf_output()
    if config_waf_output == "redirect" then
        ngx.redirect(config_waf_redirect_url, 301)
    else
        ngx.header.content_type = "text/html"
        ngx.status = ngx.HTTP_FORBIDDEN
        ngx.say(config_output_html)
        ngx.exit(ngx.status)
    end
end
