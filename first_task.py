from ipdata import ipdata
from dotenv import load_dotenv
import json
import os

load_dotenv()

my_api_key  = os.getenv('API_KEY')

ip = input("Enter IP Address: ")

with open('ip_info.json', 'w') as f:
    api_key = ipdata.IPData(my_api_key)
    response = api_key.lookup(ip)
    json.dump(response, f, indent=2)

with open('ip_info.json', 'r') as f:
    print(f.read())
    