#!/user/bin python
# -*- coding:utf-8 -*- 
# Author:Bing
# Contact:amazing_bing@outlook.com
# DateTime: 2017-02-22 10:25:45
# Description:  coding 

from pykafka import KafkaClient
import MySQLdb
import json

client = KafkaClient(hosts="1.1.1.1:9092")
conn= MySQLdb.connect(host='1.1.1.1',port = 3306,user='root',passwd='mypwd',db ='test')
cur = conn.cursor()
#client.topics
topic = client.topics['waf_logger']
consumer = topic.get_simple_consumer()
for message in consumer:
	if message is not None:
		#print message.offset, message.value
		result = json.loads(message.value)
		try:
			if("req_url" in result.keys()):
				pass
			else:
				result['req_url'] = "-"
		except Exception, e:
			pass

		sql = 'insert into sec_waf_node_report values("","%s","%s","%s","%s","%s","%s","%s","%s")'

		table_list = (result['client_ip'],result['local_time'],result['server_name'],result['user_agent'],result['attack_method'],result['req_url'],result['req_data'],result['rule_tag'])

		# print sql
		cur.execute(sql,table_list)
		conn.commit()
conn.close()




#插入一条数据
#cur.execute('insert into sec_waf_node_report values("7a2ddc41b0c68ca228632783deb8c0ba","WAF-NODE-REPORT-20170220-145055",result['client_ip'],'9')')

#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
#cur.execute("delete from student where age='9'")

# cur.close()
# conn.commit()
# conn.close()







