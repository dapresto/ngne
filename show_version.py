__author__ = 'dapresto'

import sys
import json
import requests

my_headers = {'content-type': 'application/json-rpc'}
url = "http://198.18.134.17/ins"
username = "admin"
password = "Cisco321"


payload = [{'jsonrpc': '2.0', 'method': 'cli', 'params': ['show version',1], 'id': '1'}]
my_data = json.dumps(payload)
response = requests.post(url, data=my_data, headers=my_headers, auth=(username, password))


kick_start_image = response.json()['result']['body']['kickstart_ver_str']
system_image = response.json()['result']['body']['kick_file_name']
host_name = response.json()['result']['body']['host_name']
cpu_type = response.json()['result']['body']['cpu_name']
mem_size = response.json()['result']['body']['memory']
mem_type = response.json()['result']['body']['mem_type']


print ("")
print ("===============================")
print ('host name:'+ host_name)
print ('kickstart image version :' + kick_start_image)
print ('system image version :s' + system_image)
print ('cpu type is :' + cpu_type)
print ('memory size is :' + str(mem_size) + mem_type)
print ("===============================")
