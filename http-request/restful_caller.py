#!/usr/bin/env python

import requests, json

github_url = "https://api.github.com/user/repos"
data = json.dumps({'name': 'test', 'description': 'some test repo'})
resp = requests.get(github_url, data, auth=('blood_sakura@hotmail.com','zl@1982518'))
print json.dumps(resp.json()[0])
print resp.text
