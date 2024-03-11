import secrets
import webbrowser

# outputs authorization code
def keys():
    with open("keys.txt", "r") as f:
        lines = f.readlines()
        
    client_id = lines[0].strip()
    client_secret = lines[1].strip()
    authorization_code = lines[2].strip()
    redirect_uri = "http://localhost:65010/reddit_callback"
    return client_id, client_secret, authorization_code, redirect_uri

if __name__ == "__main__":

    client_id, client_secret, authorization_code, redirect_uri = keys()
    
    state = secrets.token_hex(16)
    scope = "submit privatemessages read"
    auth_url = f"https://ssl.reddit.com/api/v1/authorize?client_id={client_id}&response_type=code&state={state}&redirect_uri={redirect_uri}&scope={scope}"
    webbrowser.open(auth_url)
