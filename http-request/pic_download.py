#!/usr/bin/env python
import requests

jpg_url = 'http://img2.niutuku.com/1312/0804/0804-niutuku.com-27840.jpg'
content = requests.get(jpg_url).content
with open('demo.jpg', 'wb') as fp:
    fp.write(content)