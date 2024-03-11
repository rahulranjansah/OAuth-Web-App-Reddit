import secrets
import webbrowser
from requests.auth import HTTPBasicAuth
import requests

# authorization code
client_id = "idjdlkdlsk_dk-aslkdmdNsk"
client_secret = "-xmdksowpasl_dklskjJSK8JS29g"
authorization_code = "8rNNqetRauaN_wb2ACWDKFKLb0iQ"
redirect_uri = "http://localhost:65010/reddit_callback"

state = secrets.token_hex(16)
scope = "submit privatemessages read"
# auth_url = f"https://ssl.reddit.com/api/v1/authorize?client_id={client_id}&response_type=code&state={state}&redirect_uri={redirect_uri}&scope={scope}"
# webbrowser.open(auth_url)


# token-retrival code

data = {
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'redirect_uri': redirect_uri,
}
response = requests.post('https://www.reddit.com/api/v1/access_token', auth=HTTPBasicAuth(client_id, client_secret), data=data)
print(response.status_code)
print(response.headers.get('X-Ratelimit-Reset'))
print(response.json())

# {'access_token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzEwMjA0MTcwLjYxOTE0OCwiaWF0IjoxNzEwMTE3NzcwLjYxOTE0OCwianRpIjoiZ3NpVjllbndTRm90TVprUi1xckstU1RpOHVwZFpBIiwiY2lkIjoielM0ZzRqdU1ZMFFfN3EtTWlacjROZyIsImxpZCI6InQyX2Nscjd3ZzVsIiwiYWlkIjoidDJfY2xyN3dnNWwiLCJsY2EiOjE2MjMxNzE4MDczMjcsInNjcCI6ImVKeUtWaXBLVFV4UjBsRXFMazNLelN4UjBsRXFLTW9zU3l4SnpVMHRMazVNVHkxV2lnVUVBQURfXzlWVERHQSIsImZsbyI6OH0.GM34B_ooojH2GAduQ84u6lD8MViaYnMxQl331TegOw7mapVVVlls6c9OadchszD53uhf4LPfgkF0SoCZR2V1VDjHLJIE_a_mmuOTuEk2Rx51ecE51fu0Jn4fHoHHNL0dnTRISpjuM3UFKaMhReGKVQY0Mnb_spy5zBGRUeKAMmqlae7xfopfBoktIzWrqCAKjm3TNxE9q2KyhlKW06qfgGKNZdUaYN-YZeit_vKy-7k-V29-Zn4_cIvtdJl5M_77ry4WhD0avqy7w99thYflTWBQiPGqqLxnlf-SApGsZEPa5zf9Qt9y_3TAEsRnwWZAuMTIvngV2t-ha0HtjALZDw',
#   'token_type': 'bearer', 'expires_in': 86400, 'scope': 'read submit privatemessages'}