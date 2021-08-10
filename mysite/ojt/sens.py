import sys
import os
import hashlib
import hmac
import base64
import requests
import time, json

def sens(request):
    timestamp = int(time.time() * 1000)
    timestamp = str(timestamp)
    url = "https://sens.apigw.ntruss.com"
    requestUrl = "/sms/v2/services/"
    serviceId = "ncp:sms:kr:268188413649:test"
    requestUrl2 = "/messages"
    access_key = "Akjg8MwJAnMlqtS1xay2"				# access key id (from portal or sub account)
    uri = requestUrl + serviceId + requestUrl2

    apiUrl = url+ uri


    def	make_signature(uri, timestamp):
        access_key = "Akjg8MwJAnMlqtS1xay2"				# access key id (from portal or sub account)
        secret_key = "X4n0F6MmrzRimRdWJBKbM3iXtFVXwuy2Jva7NmMU"				# secret key (from portal or sub account)
        secret_key = bytes(secret_key, 'UTF-8')

        method = "POST"

        message = method + " " + uri + "\n" + timestamp + "\n" + access_key
        message = bytes(message, 'UTF-8')
        signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
        return signingKey

    body = {
        "type":"SMS",
        "contentType":"COMM",
        "countryCode":"82",
        "from":"01072232876",
        #"subject":"string",
        "content":request,
        "messages":[
            {
            "to":"01072232876",
            }
        ],
    }

    body2 = json.dumps(body)

    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'x-ncp-apigw-timestamp': timestamp,
        'x-ncp-iam-access-key': access_key,
        'x-ncp-apigw-signature-v2': make_signature(uri, timestamp)
    }
    res = requests.post(apiUrl, headers=headers, data=body2)


    print(res.json()) # json response일 경우 딕셔너리 타입으로 바로 변환
