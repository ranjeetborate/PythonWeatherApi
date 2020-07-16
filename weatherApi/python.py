#!/usr/bin/env python3

import requests

print('Hello World!')
URL = 'http://nokiaasia.siteforge.com/geographyB/rest/SFCommonAPI/getSMPTemplates'
PARAMS = {'sfInstanceName':'asia','projectId':'PR-0000086','siteType':'Radio'}
HEADERS = {'Content-type':'application/json', 'Accept':'application/json','X-XSRF-TOKEN':'f9e0a479-7e95-448d-9053-f1783dc01b72','Cookie':'XSRF-TOKEN=f9e0a479-7e95-448d-9053-f1783dc01b72; JSESSIONID=D7F75569EB4B827EC5C06C44B9C1119D.tomcatB'}
print(URL)
print(PARAMS)
r = requests.post(url = URL, data = PARAMS, headers = HEADERS, auth=('p20integration', 'Inn0123!@qw'))
print("-----------")
print(r.url)
print(r.status_code)
print("-----------")
print(r.text)
print("-----------")
# ~ data = r.json()
# ~ print(data)
