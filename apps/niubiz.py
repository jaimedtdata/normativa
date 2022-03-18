import requests
import json
from django.conf import settings

merchantId = settings.COMERCIAL_ID
url_test_security_token = 'https://apisandbox.vnforappstest.com/api.security/v1/security'
url_test_token_session = f'https://apisandbox.vnforappstest.com/api.ecommerce/v2/ecommerce/token/session/{merchantId}'
url_test_transaction_autorization = f'https://apisandbox.vnforappstest.com/api.authorization/v3/authorization/ecommerce/{merchantId}'

url_prod_security_token = 'https://apiprod.vnforapps.com/api.security/v1/security'
url_prod_token_session = 'https://apiprod.vnforapps.com/api.security/v1/security'


def get_security_token():
    headers = {
                'Authorization': 'Basic aW50ZWdyYWNpb25lc0BuaXViaXouY29tLnBlOl83ejNAOGZG'
                }
    response = requests.request("POST", url_test_security_token, headers=headers)

    return response.text

def create_session_token(token_security):

    payload = json.dumps({
    "channel": "web",
    "amount": 22.00,
    "recurrenceMaxAmount": 8.5,
    "antifraud": {
        "clientIp": "24.252.107.29",
        "merchantDefineData": {
        "MDD15": "Valor MDD 15",
        "MDD20": "Valor MDD 20",
        "MDD33": "Valor MDD 33"
        }
    }
    })
    headers = {
    'Authorization': token_security,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
    }

    response = requests.request("POST", url_test_token_session, headers=headers, data=payload)
    res = response.json()
    token_session = res['sessionKey']
    #print(response.text)
    return token_session

def require_transaccion_autorizacion(token_security, transacion_token):

    payload = json.dumps({
            "channel": "web",
            "captureType": "manual",
            "countable": True,
            "order": {
                "tokenId": transacion_token,
                "purchaseNumber": "2020100901",
                "amount": 22.00,
                "currency": "PEN"
            }
        })

    headers = {
    'Authorization': token_security,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url_test_transaction_autorization, headers=headers, data=payload)

    print(response.text)
    #res = response.json()

    return response