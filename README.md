[![License](https://img.shields.io/:license-gpl3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)
[![platform](https://img.shields.io/badge/platform-osx%2Flinux%2Fwindows-green.svg)](https://github.com/Canbing007/sec-portscan-agent)
[![python](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/)

# sec-securtiy-waf-agent

## Introduce 
本程序是WAF AGENT端；采用LUA编写，攻击参数利用正则进行匹配，程序更新和报告数据采用python+api+mysql的方式进行传输；   

特点：   
防止sql注入，本地包含，部分溢出，fuzzing测试，xss,SSRF等web攻击      
防止svn/备份之类文件泄漏       
防止ApacheBench之类压力测试工具的攻击      
屏蔽常见的扫描黑客工具，扫描器      
屏蔽异常的网络请求            
屏蔽图片附件类目录php执行权限                
防止webshell上传          
黑白名单机制    

配合平台操作：   
动态添加节点  
配置和规则可定时和及时更新    
数据报告实时展现，实时动态报警    

## Usage

waf系统环境配置:http://www.jianshu.com/p/e474f24c0404 

```
pip install MySQLdb
pip install pykafka
```
在nginx.conf的http段添加     
```
lua_package_path "/usr/local/nginx/conf/waf/?.lua";
lua_shared_dict limit 10m;
init_by_lua_file  /usr/local/nginx/conf/waf/init.lua; 
access_by_lua_file /usr/local/nginx/conf/waf/waf.lua;
```  

update.py为节点更新文件;配置update.py文件，如下几个参数；    

```
waf_node_api      			#配置参数API，包括配置和规则
waf_node_result_api			#更新接口API
waf_node_key				#节点认证KEY
```
配置完成执行。    

pykaf.py为报告数据文件；配置如下几个参数：    
```
#配置ip
client = KafkaClient(hosts="ip:9092")   
#配置ip，用户密码
conn= MySQLdb.connect(host='ip',port = 3306,user='user',passwd='mypwd',db ='db')
cur = conn.cursor()
#配置kafka的topic于lib.lua中的" local ok, err = bp:send("waf_logger", nil, LOG_LINE) " 的waf_logger一致
topic = client.topics['waf_logger']
```

执行文件，启动数据报告，可直接从数据可以看到结果，也可以通过平台直接实时读取。




#### Issue

welcome to give me some sugguest
