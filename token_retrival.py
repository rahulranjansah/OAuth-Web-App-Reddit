# global imports
from requests.auth import HTTPBasicAuth
import requests

# local import
from auth import keys

client_id, client_secret, authorization_code, _ = keys()

redirect_uri = "http://localhost:65010/reddit_callback"

data = {
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'redirect_uri': redirect_uri,
}

response = requests.post('https://www.reddit.com/api/v1/access_token', auth=HTTPBasicAuth(client_id, client_secret), data=data)
print(response.status_code)
print(response.headers.get('X-Ratelimit-Reset'))
print(response.json())
