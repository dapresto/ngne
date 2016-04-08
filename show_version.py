__author__ = 'cobedien'

#from an original by cobedien with cpu type and lab host
#updated by dapresto

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
memory_size = response.json()['result']['body']['memory']
memory_type = response.json()['result']['body']['memory_type']


print ("")
print ("===============================")
print ('host name:'+ host_name)
print ('kickstart image version :' + kick_start_image)
print ('system image version :s' + system_image)
print ('cpu type is :' + cpu_type)
print ('memory size is :' + memory_size + memory_type)
print ("===============================")
