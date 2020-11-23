import base64
import json
import requests
import pandas as pd

a = "chavea" 
b = "chaveb"
c = a+":"+b
crt = base64.b64encode(bytes(c, 'utf-8')).decode("utf-8")
crt = "Basic "+crt
d = "chave"


headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': crt
}

data = {
  'grant_type': 'client_credentials'
}

get_token = requests.post('https://api.juno.com.br/authorization-server/oauth/token', headers=headers, data=data)

if get_token.status_code == 200:
    response_token = json.loads(get_token.content)

token = response_token['access_token']
tip ="Bearer "+token}
