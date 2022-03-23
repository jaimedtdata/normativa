import requests
import json
from django.conf import settings
from apps.models import NiubizTransaction, Order_payment
import datetime
from django.utils import timezone

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

def create_session_token(token_security, price):

    payload = json.dumps({
    "channel": "web",
    "amount": price,
    "antifraud": {
        #"clientIp": "24.252.107.29",
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

def require_transaccion_autorizacion(token_security, transacion_token, price, purchase_number):
    #purchase_number (numero de pedido, debe ser unico y lo debe proporcionar el negocio)
    #price

    payload = json.dumps({
            "channel": "web",
            "captureType": "manual",
            "countable": True,
            "order": {
                "tokenId": transacion_token,
                "purchaseNumber": purchase_number,
                "amount": price,
                "currency": "PEN"
            }
        })

    headers = {
    'Authorization': token_security,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url_test_transaction_autorization, headers=headers, data=payload)
    res = response.json()

    data = {
        "ecoreTransactionUUID": res['header']['ecoreTransactionUUID'],
        'channel': res['fulfillment']['channel'],
        "signature": res['fulfillment']['signature'],
        "tokenId": res['order']['tokenId'],
        "purchaseNumber": res['order']['purchaseNumber'],
        "amount": res['order']['amount'],
        "installment": res['order']['installment'],
        "currency": res['order']['currency'],
        "authorizedAmount": res['order']['authorizedAmount'],
        "authorizationCode": res['order']['authorizationCode'],
        "traceNumber": res['order']['traceNumber'],
        "transactionDate": res['order']['transactionDate'],
        "card": res['dataMap']['CARD'],
        "action_description": res['dataMap']['ACTION_DESCRIPTION'],
        "brand": res['dataMap']['BRAND'],
    }
    
    return data

def create_order_payment(user,email,niubiz_id, price, type_membership):
    #check if not exist any order
    exist_order = Order_payment.objects.filter(identity=user.identity).exists()
    if not exist_order:
        orden=Order_payment(
                member= user,
                names=user.names,
                first_surname=user.first_surname,
                second_surname=user.second_surname,
                email=email,
                identity=user.identity,
                paid = True,
                niubiz_id= niubiz_id,
                pay_import = price,
                validity_date_start = timezone.now() ,
                validity_date_finish = (timezone.now() + timezone.timedelta(days=30))
            )
        orden.save()
        return orden
    else:
    #if exist update dates
    #get the last created date
        last_order = Order_payment.objects.filter(identity=user.identity).latest('created')
        created = last_order.created
        date_start = last_order.validity_date_start
        date_finish = last_order.validity_date_finish
        
        actual_day_of_purchase = timezone.now()

        if type_membership == "Plan mensual":
            if actual_day_of_purchase > date_finish:
                validity_date_start = timezone.now()
                validity_date_finish = (validity_date_start + timezone.timedelta(days=30))
            else:
                validity_date_start = date_finish
                validity_date_finish = (date_finish + timezone.timedelta(days=30))
        if type_membership == "Plan anual":
            if actual_day_of_purchase > date_finish:
                validity_date_start = timezone.now()
                validity_date_finish = (validity_date_start + timezone.timedelta(days=365))
            else:
                validity_date_start = date_finish
                validity_date_finish = (date_finish + timezone.timedelta(days=365))

        orden=Order_payment(
                member= user,
                names=user.names,
                first_surname=user.first_surname,
                second_surname=user.second_surname,
                email=email,
                identity=user.identity,
                paid = True,
                niubiz_id= niubiz_id,
                pay_import = price,
                validity_date_start = validity_date_start ,
                validity_date_finish = validity_date_finish
            )
        orden.save()
        return orden


def create_niubiz_transaction(data, orden):

    NiubizTransaction.objects.create(
        order_pyment = orden,
        ecoreTransactionUUID = data['ecoreTransactionUUID'],
        channel = data['channel'],
        signature =  data['signature'],
        tokenId = data['tokenId'],
        purchaseNumber = data['purchaseNumber'],
        amount = data['amount'],
        installment = data['installment'],
        currency =  data['currency'],
        authorizedAmount =  data['authorizedAmount'],
        authorizationCode = data['authorizationCode'],
        traceNumber = data['traceNumber'],
        #transactionDate =  res['order']['transactionDate'],
        card = data['card'],
        action_description = data['action_description'],
        brand = data['brand'],
    )



