def papago(request):
    import sys
    import os
    import requests
    import json


    cliend_id = "coyooua9r9"
    client_secret = "L4HTGGetyYQTH40iFEHrAkN6QrCn20Vu0czapLH2"


    apiUrl = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"
    mothod = "POST"

    body = {
        "source":"ko",
        "target":"en",
        "text":request
    }

    body2 = json.dumps(body)

    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'X-NCP-APIGW-API-KEY-ID': cliend_id,
        'X-NCP-APIGW-API-KEY': client_secret,
    }
    response = requests.post(apiUrl, headers=headers, data=body2)
    rescode = response.status_code
    response_body = response.json()
    result = response_body
    return result['message']['result']['translatedText']

    print(res.json()) # json response일 경우 딕셔너리 타입으로 바로 변환

#print(papago("hello"))
