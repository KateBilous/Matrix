from datadog import initialize, api
from datadog import initialize, api

options = {
    'api_key': 'be41af01cb43989c16e44bcad453cedb',
    'app_key': 'ae2a543f73a7d9ce2faeb043e369b85282e1a82f'
}

initialize(**options)

title = "Something big happened!"
text = 'And let me tell you all about it here!'
tags = ['version:1', 'application:web']

api.Event.create(title=title, text=text, tags=tags)