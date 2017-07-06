import requests
import xml.etree.ElementTree as ET
'''
Created on Dec 25, 2016

@author: prashantpukale@gmail.com
'''


def getaccess_token(surl):
    print('Start')
    headers = {}
    headers['Content-Language'] = "en-US"
    headers[
        'User-Agent'] = "CC Freestyle/507000 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G930F Build/MMB29K)"
    headers['Content-Type'] = "application/x-www-form-urlencoded"
    headers['Content-Length'] = "361"
    headers['Host'] = "coca-cola.janraincapture.com"
    headers['Connection'] = "Keep-Alive"
    headers['Accept-Encoding'] = "gzip"

    payload = {}
    payload['flow'] = "freestyle_v2"
    payload['response_type'] = "token"
    payload['refresh_secret'] = "bc4cd4c92cfef0e51ab63d538508ffcafbc2178f"
    payload['form'] = "userInformationForm"
    payload['redirect_uri'] = "http://android.library"
    payload['flow_version'] = "e98b985f-e235-4ad8-a84a-6ad04d8519c6"
    payload['flow_version'] = "20161222233041855736"
    payload['client_id'] = "tthvk4y4kqesjykrprvazcrdx82ngrht"
    payload['locale'] = "en-US"
    payload['traditionalSignIn_password'] = "Igate@1234"
    payload['traditionalSignIn_emailAddress'] = "ccfstest100@gmail.com"

    test = requests.post(surl, data=payload, headers=headers, verify=False)
    content = test.json()

    # for key, value in content.items():
    #    print(key, value)
    #testtoken = content['stat']
    # print(testtoken)
    argaccess_token = content['access_token']
    #print(        'This argaccess_token is inside if main token function:====' + argaccess_token)
    print('End with Access token' + argaccess_token)
    return(argaccess_token)


def refreshtoken(argaccess_token, refresh_url):
    print('Start2' + argaccess_token)

    headers = {}
    headers['Host'] = "coca-cola.janraincapture.com"
    headers['Connection'] = "Keep-Alive"
    headers['Accept'] = "*/*"
    # "CC Freestyle/507000 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G930F Build/MMB29K)"
    headers['User-Agent'] = "CCFS/6.0.4.362 CFNetwork/808.0.2 Darwin/16.0.0"
    headers['Content-Language'] = "en-US"
    headers['Accept-Encoding'] = "gzip"
    headers['Content-Length'] = "209"
    headers['Content-Type'] = "application/x-www-form-urlencoded"

    payload = {}
    payload['locale'] = "en-US"
    payload['signature'] = "d7CqrbaXZdySUIh31Ywq38yhYK4="
    payload['date'] = "2017-01-01 04:18:01"
    payload['flow'] = "freestyle_v2"
    payload['flow_version'] = "e98b985f-e235-4ad8-a84a-6ad04d8519c6"
    #payload['flow_version'] = "20161222233041855736"
    payload['access_token'] = argaccess_token
    payload['client_id'] = "tthvk4y4kqesjykrprvazcrdx82ngrht"
    # payload['response_type'] = "token"
    #payload['refresh_secret'] = "bc4cd4c92cfef0e51ab63d538508ffcafbc2178f"
    #payload['form'] = "userInformationForm"
    #payload['redirect_uri'] = "http://android.library"
    #payload['flow_version'] = "e98b985f-e235-4ad8-a84a-6ad04d8519c6"
    #payload['client_id'] = "tthvk4y4kqesjykrprvazcrdx82ngrht"
    #payload['locale'] = "en-US"
    #payload['signature'] = "onECu6v8zPs1jqSwnHgZCwA4/2w="
    #payload['access_token'] = argaccess_token
    #payload['date'] = "2016-12-29 15:29:32"
    #payload['traditionalSignIn_password'] = "Igate@1234"
    #payload['traditionalSignIn_emailAddress'] = "ccfstest100@gmail.com"
    refresh_test = requests.post(
        refresh_url, data=payload, headers=headers, verify=False)
    content = refresh_test.json()
    #argaccess_token = content['stat']
    # print(argaccess_token)

    for key, value in content.items():
        print(key, value)
    testtoken = content['stat']
    # print(testtoken)
    print('End2')


def getjanid(janrainurl, mcremail, userudid):
    print('Start')
    headers = {}
    headers['Host'] = "coca-cola.janraincapture.com"
    headers[
        'User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
    headers[
        'Accept'] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    headers['Accept-Language'] = "en-US,en;q=0.5"
    headers['Accept-Encoding'] = "gzip, deflate, br"
    #headers['Cookie'] = "uuid=c1133e7c-2209-478f-a5d6-92a4c88ca287"
    headers['Connection'] = "keep-alive"
    headers['Upgrade-Insecure-Requests'] = '1'
    headers['Cache-Control'] = "max-age=0"

    payload = {}
    payload['email'] = mcremail
    payload['handle'] = ""
    payload['UUID'] = userudid
    payload['search'] = "Search Janrain"
    print(headers)
    janrainurl = janrainurl + \
        '?email=prashantpukale@gmail.com&handle=&UUID=&search=Search+Janrain'
    response = requests.request(
        "GET", janrainurl, headers=headers, verify=False)
    print(response.text)

    '''userinfo = requests.get(
        janrainurl, headers=headers, verify=False)
    tree = ET.parse(userinfo.text)  # userinfo.json()
    root = tree.getroot()

    for key, value in root.items():
        print(key, value)
    testtoken = root['status']
    # print(testtoken)
    print('End2')'''
