#!/user/bin python
# -*- coding:utf-8 -*- 
# Author:Bing
# Contact:amazing_bing@outlook.com
# DateTime: 2017-02-03 15:23:20
# Description:  coding 
import time,os

'''
通过api接口来更新配置
'''
def waf_config_update():
	t = open("test2.lua","w")
	with open("config.lua","r") as f:
		for i in f.readlines():
			vul = i.strip()
			t.write(vul)
			t.write("\n")
def waf_rule_update():
	pass

#更新配置和规则
def update_right():
	waf_config_update()
	#waf_rule_update()
	#os.system("/usr/local/nginx/nginx/sbin/nginx -s reload")

def damon():
	web_api = "http://www.xx.com/waf_config"
	update_status = 1

	current_time = time.localtime(time.time())
	#获取配置文件修改时间
	mtime = time.localtime(os.path.getmtime("config.lua"))
	#获取规则文件修改时间
	rtime = time.localtime(os.path.getmtime("rule-config/url.rule"))

	if((current_time.tm_year == mtime.tm_year) and (mtime.tm_mon == current_time.tm_mon) and (mtime.tm_mday == current_time.tm_mday) and (mtime.tm_hour == current_time.tm_hour)):
		pass #print "已更新"
	else:
		#及时更新
		if update_status == 1:
			update_right()
		else:
			#定时更新
			if current_time.tm_hour == 2:
				update_right()




# current_time = time.localtime(time.time())
# mtime = time.localtime(os.path.getmtime("config.lua"))
# rtime = time.localtime(os.path.getmtime("rule-config/url.rule"))
# #ctime = time.ctime(os.path.getctime("test2.lua"))
# print mtime.tm_year, mtime.tm_mon , mtime.tm_mday,mtime.tm_hour
# print current_time.tm_year, current_time.tm_mon , current_time.tm_mday,current_time.tm_hour
# print rtime.tm_hour
