import cdalib


''' variables for Access Token and refresh Token START '''
surl = "https://coca-cola.janraincapture.com/oauth/auth_native_traditional"
refresh_url = 'https://coca-cola.janraincapture.com/oauth/refresh_access_token'
''' variables for Access Token and refresh Token END '''

''' variables for Janrain ID START '''
janrainurl = "https://test.barcodeservices.ccnag.com/rest/v1/janrainScanner"
''' variables for Janrain IDEND '''


argaccess_token = cdalib.getaccess_token(surl)
#argaccess_token = "8vc58pu4agu4ujht"
#print('argaccess_token' + argaccess_token)
#ftest = cdalib.refreshtoken(argaccess_token, refresh_url)
# print(ftest)
