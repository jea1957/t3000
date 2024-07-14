#!/usr/bin/env python3

import os
import urllib.parse

ALLOWED_KEYS = ['mute', 'down', 'up', 'ph', 'tp', 'p1', 'p2', 'p3', 'p4', 'p5', 'standby']
response = '1' # default error response

try:
    if os.environ.get('REQUEST_METHOD') == 'GET':
        key = urllib.parse.parse_qs(os.environ.get('QUERY_STRING'))['button'][0]
        if key in ALLOWED_KEYS:
            os.system(f'ir-ctl --duty-cycle=30 --send cgi-bin/{key}')
            response = f'0 key={key}'
finally:
    print('Content-Type: text/html\n\n')
    print(response)
