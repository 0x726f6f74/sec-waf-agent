#!/user/bin python
# -*- coding:utf-8 -*- 
# Author:Bing
# Contact:amazing_bing@outlook.com
# DateTime: 2017-02-03 15:23:20
# Description:  coding 
import time,os,re

from requests import get,post

######################     basic parameter configure   ######################################
#请求参数信息
waf_node_api = "http://1.1.1.1/sec-security-apiservice/index.php/inter/waf_config"
waf_node_key = "test"
waf_login_session = "bing"

#完成之后,请求更改状态API
waf_node_result_api = "http://1.1.1.1/sec-security-apiservice/index.php/inter/waf_update"


#配置规则路径
current_dir = str(os.getcwd())
current_dirs = current_dir.replace('\\','/')
rule_path = current_dirs+"/rule-config/"



#获取处理配置函数
def lamb(test):
	if test == "1":
		return "on"
	elif test == "0":
		return "off"
	else:
		pass

#获取节点状态和规则数据
def waf_api_init():
	try:
		data = {}
		
		waf_node_data = eval(post(url=waf_node_api,data={"key":waf_node_key}).content)

		data["waf_node_status"] = waf_node_data["waf_monitor"]["waf_node_status"]
		data["waf_node_conf_status"] = waf_node_data["waf_monitor"]["waf_conf_updata_status"]
		data["waf_node_rule_status"] = waf_node_data["waf_monitor"]["waf_rule_update_status"]

		waf_node_conf_data = waf_node_data["waf_config"]
		data["waf_node_rule_data"] = waf_node_data["waf_reg"]

		waf_conf_data = {}
		waf_conf_data["config_waf_enable"] =  lamb(waf_node_conf_data["config_waf_enable"])
		waf_conf_data["config_white_url_check"] = lamb(waf_node_conf_data["config_white_url_enable"])
		waf_conf_data["config_white_ip_check"] = lamb(waf_node_conf_data["config_white_ip_enable"])
		waf_conf_data["config_black_ip_check"] = lamb(waf_node_conf_data["config_black_ip_enable"])
		waf_conf_data["config_url_check"] = lamb(waf_node_conf_data["config_url_enable"])
		waf_conf_data["config_url_args_check"] = lamb(waf_node_conf_data["config_url_args_enable"])
		waf_conf_data["config_user_agent_check"] = lamb(waf_node_conf_data["config_user_agent_enable"])
		waf_conf_data["config_cookie_check"] = lamb(waf_node_conf_data["config_cookie_enable"])
		waf_conf_data["config_cc_check"] = lamb(waf_node_conf_data["config_cc_enable"])
		waf_conf_data["config_cc_rate"] = waf_node_conf_data["config_cc_rate"]
		waf_conf_data["config_post_check"] =  lamb(waf_node_conf_data["config_post_enable"])
		waf_conf_data["config_waf_output"] = "html"
		waf_conf_data["waf_rule_dir"] = rule_path
		waf_conf_data["config_waf_redirect_url"] = "http://www.jianshu.com/users/d484ac7f2c2c/latest_articles"
		waf_conf_data["config_output_html"] = '''[[
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
		]]'''


		return data,waf_conf_data
	except Exception as e:
		print e



######################     write operation      ######################################
def waf_conf_file_write(conf_data):
	conf_file = open("config.lua","w")
	try:
		for k,v in conf_data.items():
			if str(k) == "config_output_html" :
				conf_file.write(k+"="+v)
				conf_file.write("\n")
			else:
				conf_file.write(k+"="+"\'"+v+"\'")
				conf_file.write("\n")
		conf_file.close()
		print "config_write Success"
	except:
		print "config_write False"

def waf_rule_file_write(rule_data):
	rule_args_file = open(rule_path+"args.rule","w")
	rule_blackip_file = open(rule_path+"blackip.rule","w")
	rule_cookie_file = open(rule_path+"cookie.rule","w")
	rule_post_file =  open(rule_path+"post.rule","w")
	rule_url_file =  open(rule_path+"url.rule","w")
	rule_useragent_file =  open(rule_path+"useragent.rule","w")
	rule_whiteip_file = open(rule_path+"whiteip.rule","w")
	rule_whiteurl_file =  open(rule_path+"whiteurl.rule","w")
	try:
		for  rule in rule_data:
			if rule["waf_rule_type"] == "1":
				waf_node_rule_reg = rule["waf_rule_reg"].replace('\\\\','\\')
				rule_args_file.write(waf_node_rule_reg)
				rule_args_file.write("\n")
			elif rule["waf_rule_type"] == "2":
				waf_node_rule_reg = rule["waf_rule_reg"].replace('\\\\','\\')
				rule_blackip_file.write(waf_node_rule_reg)
				rule_blackip_file.write("\n")
			elif rule["waf_rule_type"] == "3":
				waf_node_rule_reg = rule["waf_rule_reg"].replace('\\\\','\\')
				rule_cookie_file.write(waf_node_rule_reg)
				rule_cookie_file.write("\n")
			elif rule["waf_rule_type"] == "4":
				waf_node_rule_reg = rule["waf_rule_reg"].replace('\\\\','\\')
				rule_post_file.write(waf_node_rule_reg)
				rule_post_file.write("\n")
			elif rule["waf_rule_type"] == "5":
				waf_node_rule_reg = rule["waf_rule_reg"].replace('\\\\','\\')
				rule_url_file.write(waf_node_rule_reg)
				rule_url_file.write("\n")
			elif rule["waf_rule_type"] == "6":
				waf_node_rule_reg = rule["waf_rule_reg"].replace('\\\\','\\')
				rule_useragent_file.write(waf_node_rule_reg)
				rule_useragent_file.write("\n")
			elif rule["waf_rule_type"] == "7":
				waf_node_rule_reg = rule["waf_rule_reg"].replace('\\\\','\\')
				rule_whiteip_file.write(waf_node_rule_reg)
				rule_whiteip_file.write("\n")
			elif rule["waf_rule_type"] == "8":
				waf_node_rule_reg = rule["waf_rule_reg"].replace('\\\\','\\')
				rule_whiteurl_file.write(waf_node_rule_reg)
				rule_whiteurl_file.write("\n")

		rule_args_file.close()
		rule_blackip_file.close()
		rule_cookie_file.close()
		rule_post_file.close()
		rule_url_file.close()
		rule_useragent_file.close()
		rule_whiteip_file.close()
		rule_whiteurl_file.close()
		print "rule_write Success"
	except:
		print "rule_write False"

######################     rule operation      ######################################

#初始化操作
def waf_node_conf_init(data):
	waf_conf_file_write(data)
	print "conf init start"

#定时更新操作
def waf_node_conf_set(data):
	current_time = time.localtime(time.time())
	if current_time.tm_hour == 2:
		waf_conf_file_write(data)
		print "conf set time start"
	else:
		pass

#及时更新操作
def waf_node_conf_update(data):
	waf_conf_file_write(data)
	print "conf update start"


#初始化操作
def waf_node_rule_init(data):
	waf_rule_file_write(data)
	os.system("/usr/local/nginx/nginx/sbin/nginx -s reload")
	print "rule init start"

#定时更新操作
def waf_node_rule_set(data):
	current_time = time.localtime(time.time())
	if current_time.tm_hour == 2:
		waf_rule_file_write(data)
		os.system("/usr/local/nginx/nginx/sbin/nginx -s reload")
		print "rule set time start"
	else:
		pass

#及时更新操作
def waf_node_rule_update(data):
	waf_rule_file_write(data)
	os.system("/usr/local/nginx/nginx/sbin/nginx -s reload")
	print "rule update start"



######################     main entrance  operation      ######################################


'''
根据API，判断节点是否开启
'''



while True:
	data, waf_conf_data=waf_api_init()
	if(data['waf_node_status'] == '1'):
		data_conf = {}
		data_rule = {}

		if(data['waf_node_conf_status'] == "1"):
			waf_node_conf_update(waf_conf_data)
			data_conf['conf_status']  = "1"
		elif(data['waf_node_conf_status'] == "0"):
			waf_node_conf_set(waf_conf_data)
			data_conf['conf_status']  = "1"
		elif(data['waf_node_conf_status'] == "3"):
			waf_node_conf_init(waf_conf_data)
			data_conf['conf_status']  = "1"
		else:
			pass
		
		if(data['waf_node_rule_status'] == "1"):
			waf_node_rule_update(data["waf_node_rule_data"])
			data_rule['rule_status']  = "1"
		elif(data['waf_node_rule_status']  == "0"):
			waf_node_rule_set(data["waf_node_rule_data"])
			data_rule['rule_status']  = "1"
		elif(data['waf_node_rule_status']  == "3"):
			waf_node_rule_init(data["waf_node_rule_data"])
			data_rule['rule_status']  = "1"
		else:
			pass

		dictMerged=dict(data_conf)
		dictMerged.update(data_rule)
		dictMerged["key"] = waf_node_key
		# dictMerged["waf_node_key"] = waf_node_key
		info = eval(post(url= waf_node_result_api,data=dictMerged).content)

		if(info["status"] == 1):
			print "stauts is ok"
		elif(info["status"] == 0 ):
			print "status was changed"
		else:
			print "status false"
	else:
		print "node close"
	time.sleep(5)




'''
{
    "status": 1,
    "waf_config": {
        "config_waf_enable": "1",
        "config_white_url_enable": "1",
        "config_white_ip_enable": "1",
        "config_black_ip_enable": "1",
        "config_url_enable": "1",
        "config_url_args_enable": "1",
        "config_user_agent_enable": "1",
        "config_cookie_enable": "1",
        "config_cc_enable": "1",
        "config_cc_rate": "100/60",
        "config_post_enable": "1",
        "config_waf_output": "1",
        "config_waf_redirect_url": "http://www.test.com",
        "config_waf_key": "test"
    },
    "waf_monitor": {
        "waf_node_status": "1",
        "waf_conf_updata_status": "3",
        "waf_rule_update_status": "3",
        "waf_node_ruleid": "WAF-RULE-20170207-110833,WAF-RULE-20170207-122956"
    },
    "waf_reg": [
        {
            "waf_rule_reg": "wqearste",
            "waf_rule_type": "2"
        },
        {
            "waf_rule_reg": "\.\\./",
            "waf_rule_type": "1"
        }
    ]
}
'''
