## Integração API JUNO com Python

Este mecanismo foi desenvolvido a partir da documentação técnica disponibilizada pela [Juno](https://dev.juno.com.br/junoAPI20Integration.pdf).

## Requisitos

Ambiente Python 3 e as bibliotecas: base64, json, requests e pandas

## Integração

A comunicação é feita com modelo e parânetros JSON

## Ambientes

Temos dois Ambientes:
Produção e Sandbox



##### Importando as Bibliotecas e Definindo Parâmetros Globais das requisições

```c#
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

```

### Gerando o Token

O `Token` é necessário para as demais requisições. Cada Token tem o prazo de Validade.
[referência](https://www.boletobancario.com/boletofacil/integration/integration.html#cobrancas). 


```c#
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
```



## Suporte Juno

[equipe de implantação Juno](mailto:implantacao@juno.com.br).




