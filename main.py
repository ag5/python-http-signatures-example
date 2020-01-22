import json

import requests
from requests_http_signature import HTTPSignatureAuth

key_id = "squirrel"
key_secret = b"monorail_cat"
url = "https://matrix.ag5.com/api/[endpoint]/serviceIsAvailable"

get_headers = ('(request-target)', 'date', 'host')
post_headers = get_headers + ('content-type', 'digest')

# Example GET request
response = requests.post(
    url,
    auth=HTTPSignatureAuth(
        key=key_secret,
        algorithm='hmac-sha256',
        key_id=key_id,
        headers=get_headers,
    ),
)

# Example POST request
response = requests.post(
    url,
    headers={'Content-Type': 'application/json'},
    data=json.dumps({"hello": "world"}).encode('utf-8'),
    auth=HTTPSignatureAuth(
        key=key_secret,
        algorithm='hmac-sha256',
        key_id=key_id,
        headers=post_headers,
    ),
)




