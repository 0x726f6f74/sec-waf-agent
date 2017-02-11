#!/user/bin python
# -*- coding:utf-8 -*- 
# Author:Bing
# Contact:amazing_bing@outlook.com
# DateTime: 2017-02-03 15:23:20
# Description:  coding 

import time,os

# current_time = time.localtime(time.time())
# mtime = time.localtime(os.path.getmtime("config.lua"))
# rtime = time.localtime(os.path.getmtime("rule-config/url.rule"))
# #ctime = time.ctime(os.path.getctime("test2.lua"))
# print mtime.tm_year, mtime.tm_mon , mtime.tm_mday,mtime.tm_hour
# print current_time.tm_year, current_time.tm_mon , current_time.tm_mday,current_time.tm_hour
# print rtime.tm_hour

from requests import get,post

#session = login();
web_api = http://xx.xx.com/main/waf_node


def upate():
	#获取更新
	waf_update = post(url=web_api,data={"obj":"waf_node_update","waf_key":"sdffsdf234234","session":"session_id234234"})
	#return   {"status":1,"data":[{"waf_node_id":"WAF-NODEID-2323","status":0}]}
	#return   {"status":1,"data":[{"waf_node_id":"WAF-NODEID-2323","status":2,"time":2}]}
	#status  0 不更新	1    及时更新	2    定时更新	3	初始化配置
	# if waf_update["data"][0]["status"] == 0:
	# 	pass
	# elif waf_update["data"][0]["status"] == 1:
	# 	update()


try:
	#获取配置
	waf_conf = post(url=web_api,data={"obj":"waf_node_conf","waf_key":"sdffsdf234234","session":"session_id234234"})
	#return   {"status":1,"data":[{"waf_node_id":"WAF-NODEID-2323","config_waf_enable":1,"config_white_url_check":1 ....}]}

	#获取规则
	waf_rule = post(url=web_api,data={"obj":"waf_node_rule","waf_key":"sdffsdf234234","session":"session_id234234"})
	#return   {"status":1,"data":[{"waf_node_id":"WAF-NODEID-2323","type":1,"rule_math":"\.\./etc/passwd"}]}
	#1 args 2 blackip 3 cookie  一一对应参数
except:
	print "error:web_api "

# waf_config_in = vul["data"]
# rule_args = vul1["data"]
# rule_blackip = vul2["data"]
# rule_cookie = vul3["data"]
# rule_post = vul4["data"]
# rule_url = vul5["data"]
# rule_useragent = vul6["data"]
# rule_whiteip = vul7["data"]
# rule_whiteurl = vul8["data"]

# #print waf_config_in,rule_args

# #本地保存配置
# conf_file = open("config2.lua","w")
# conf_files = open("config2.lua","r")

# #本地保存规则
# path = "rule-config/"
# rule_args_file = open(path+"args.rule","w")
# rule_args_files = open(path+"args.rule","r")
# rule_blackip_file = open(path+"blackip.rule","w")
# rule_cookie_file = open(path+"cookie.rule","w")
# rule_post_file =  open(path+"post.rule","w")
# rule_url_file =  open(path+"url.rule","w")
# rule_useragent_file =  open(path+"useragent.rule","w")
# rule_whiteip_file = open(path+"whiteip.rule","w")
# rule_whiteurl_file =  open(path+"whiteurl.rule","w")


# #配置写入文件
# current_time = time.localtime(time.time())
# #获取配置文件修改时间
# mtime = time.localtime(os.path.getmtime("config.lua"))
# #获取规则文件修改时间
# rtime = time.localtime(os.path.getmtime("rule-config/url.rule"))

# def update_config(waf_config_in):
# 	try:
# 		for  waf_conf in waf_config_in:
# 			for k,v in waf_conf.items():
# 				if str(k) == "config_output_html" :
# 					conf_file.write(k+"="+"[["+v+"]]")
# 					conf_file.write("\n")
# 				else:
# 					conf_file.write(k+"="+"\'"+v+"\'")
# 					conf_file.write("\n")
# 	except:
# 		print "配置更新失败"

# def update_rule(rule_args):
# 	try:
# 		for  rule in rule_args:
# 			if rule["rule_type"] == "1":
# 				for k,v in rule.items():
# 					if str(k) == "rule_matchs" :
# 						rule_args_file.write(v)
# 						rule_args_file.write("\n")
# 			elif rule["rule_type"] == "2":
# 				for k,v in rule.items():
# 					if str(k) == "rule_matchs" :
# 						rule_blackip_file.write(v)
# 						rule_blackip_file.write("\n")
# 			elif rule["rule_type"] == "3":
# 				for k,v in rule.items():
# 					if str(k) == "rule_matchs" :
# 						rule_cookie_file.write(v)
# 						rule_cookie_file.write("\n")
# 			elif rule["rule_type"] == "4":
# 				for k,v in rule.items():
# 					if str(k) == "rule_matchs" :
# 						rule_post_file.write(v)
# 						rule_post_file.write("\n")
# 			elif rule["rule_type"] == "5":
# 				for k,v in rule.items():
# 					if str(k) == "rule_matchs" :
# 						rule_url_file.write(v)
# 						rule_url_file.write("\n")
# 			elif rule["rule_type"] == "6":
# 				for k,v in rule.items():
# 					if str(k) == "rule_matchs" :
# 						rule_useragent_file.write(v)
# 						rule_useragent_file.write("\n")
# 			elif rule["rule_type"] == "7":
# 				for k,v in rule.items():
# 					if str(k) == "rule_matchs" :
# 						rule_whiteip_file.write(v)
# 						rule_whiteip_file.write("\n")
# 			elif rule["rule_type"] == "8":
# 				for k,v in rule.items():
# 					if str(k) == "rule_matchs" :
# 						rule_whiteurl_file.write(v)
# 						rule_whiteurl_file.write("\n")
# 			else:
# 				pass
# 	except:
# 		print "规则更新失败"



# #更新配置文件;1及时更新 0 定时更新
# def waf_config_update(conf):
# 	status = 0
# 	try:
# 		for  waf_conf in conf:
# 			if waf_conf["config_update_status"] == "1" :
# 				status = 1
# 			elif conf_files.read() == "" :
# 				status = 1
# 			else:
# 				pass
# 	except:
# 		pass
		
# 	#print status
# 	if status == 1 :
# 		update_config(conf)
# 	else:
# 		if current_time.tm_hour == 2:
# 			update_config(conf)
# 		else:
# 			pass


# #更新规则文件;1及时更新 0 定时更新
# def waf_rule_update(rule_args):
# 	status = 0
# 	try:
# 		for  rule in rule_args:
# 			if rule["rule_update_status"] == "1" :
# 				status = 1
# 			elif rule_args_files.read() == "" :
# 				status = 1
# 			else:
# 				pass
# 	except:
# 		pass

# 	#print status
# 	if status == 1 :
# 		update_rule(rule_args)
# 	else:
# 		if current_time.tm_hour == 2:
# 			update_rule(rule_args)
# 			print "定时更新"
# 		else:
# 			pass


# #更新配置和规则
# def update_right():
# 	waf_config_update(waf_config_in)
# 	waf_rule_update(rule_args)
# 	waf_rule_update(rule_blackip)
# 	waf_rule_update(rule_cookie)
# 	waf_rule_update(rule_post)
# 	waf_rule_update(rule_url)
# 	waf_rule_update(rule_useragent)
# 	waf_rule_update(rule_whiteip)
# 	waf_rule_update(rule_whiteurl)
# 	#os.system("/usr/local/nginx/nginx/sbin/nginx -s reload")


# #更新配置文件
# def run():
# 	if((current_time.tm_year == mtime.tm_year) and (mtime.tm_mon == current_time.tm_mon) and (mtime.tm_mday == current_time.tm_mday) and (mtime.tm_hour == current_time.tm_hour)):
# 		return False		 #print "已更新"
# 	else:
# 		update_right()
# 		return True


# while True:
# 	result = run()
# 	time.sleep(3)
# 	print "continue"




#关闭文件			
# conf_file.close()
# rule_args_file.close()
# rule_blackip_file.close()
# rule_cookie_file.close()
# rule_post_file.close()
# rule_url_file.close()
# rule_useragent_file.close()
# rule_whiteip_file.close()
# rule_whiteurl_file.close()
