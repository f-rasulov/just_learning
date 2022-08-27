from ipdata import ipdata
import json
import os

my_api_key  = os.environ.get('API_KEY')

ip = input("Pleae enter ip Address: ")

with open('ip_info.json', 'w') as f:
    api_key = ipdata.IPData(my_api_key)
    response = api_key.lookup(ip)
    json.dump(response, f, indent=2)

with open('ip_info.json', 'r') as f:
    print(f.read())
    