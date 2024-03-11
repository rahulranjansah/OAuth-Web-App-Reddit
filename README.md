Note: Not maintained by Reddit, one may use PRAW (Python Reddit API Wrapper) as an alternative

# OAuth-Web-App-Reddit

OAuth2 support allows you to use reddit to authenticate on non-reddit websites and application. This authentication is relevant for Web-App and (Personal Script) not for Apps.

## Getting started (Prequisites)

Before running this project, ensure that you have the following pre-requisities installed:

- Python
- Git

## Assumptions

We assume that you know how to access test-script information by going to https://www.reddit.com/prefs/apps

Here you will get client_id, client_secret that is to be replaced in the code above in keys.txt file. (Followed up below)

## Installation

To get started with the matrix calculator, follow these steps:

1. Clone this repository to your local machine using the following command:

   ```shell/terminal
   git clone https://github.com/rahulranjansah/OAuth-Web-App-Reddit.git
    ```
2. Navigate to the project directory:

   ```shell/terminal
   cd OAuth-Web-App-Reddit
   ```
3. Install the required dependencies for the running the follwing command
    ```shell/terminal
    pip install -r requirements.txt
    ```

## Authorization

### Step 1

In order to make requests to reddit's API via OAuth, you must acquire an Authorization token. In this code, open auth.py

    ```shell/terminal
    code auth.py
    ```
(Followed up) Now open keys.txt, where we have to delete the example values and add your client_id, and client_secret respectively.

Run auth.py
    ```shell
    python3 auth.py
    ```
It should redirect you to your browser and press "Accept", which will direct you to

    ```shell
    http://localhost:65010/reddit_callback?state=8800d0c5d843145288b04bbe743fda78&code=8rNNqetRauaN_wb2ACWFAABFNQb0iQ#_
    ```
In this code, copy the value of code which is our authorization key/code, not to confuse with bearer/access_token.

    ```shell
    code=8rNNqetRauaN_wb2ACWFAABFNQb0iQ
    ```
Ignore the #_ at the end, commonly known as fragment identifier is added in the link for security reasons.

### Step 2

Copy the <code> itself in the keys.txt file below client_secret, which is our authorization code.

Now open token_retrival file, which can be done by typing following command in terminal/shell.

    ```shell
    code token_retrival.py
    ```
Now run this code by update keys.txt with the new auth code,

    ```shell
    python3 token_retrival.py
    ```

## Final Output

If everything runs properly you may expect output like this:

    ```shell
    {'access_token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsM40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzEwMjA1MzA1LjA3MDQyMSwiaWF0IjoxNzEwMTE4OTA1LjA3MDQyMSwianRpIjoia2ZWb3RkYmFyTExvaXBPVGZTcG1CT2xjT19heFFRIiwiY2lkIjoielM0ZzRqdU1ZMFFfN3EtTWlacjROZyIsImxpZCI6InQyX2Nscjd3ZzVsIiwidDJfY2xyN3dnNWwiLV4UjBsRXFMazNLelN4UjBsRXFLTW9zU3l4SnpVMHRMazVNVHkxV2lnVUVBQURfXzlWVERHQSIsImZsbyI6OH0.n6B4bpjtAnl4zC0LxJaasZn2Fo8NbgKwD04r8tvcgp9gackdXmn0dR5olkuR4hQEh-F13OBU2_5XanZn0KxDnPY04g7UfnqtP_gMurJ6vKIsL8sWP9Pab8AVgYSODTa0ydHy_ChCcK8LK4ig9RGaRNU6V8246i8XdyZFCtPZklG_knOQBUdUXoz5YNQPKj6XoXWvSUP9pbfVGpcjYJdXnT3adNjPydCkOKptg', 'token_type': 'bearer', 'expires_in': 86400, 'scope': 'read submit privatemessages'}
    ```

Copy the access_token and start scrapping relevant data from Reddit. (End note explains more about capability)

## Possible Errors

Possible error you may face are:

    ```shell
    404
    None
    {'message': 'Not Found', 'error': 404}
    ```
This error means you've entered something wrong in the code.

    ```shell
    429
    None
    {'message': 'Too Many Requests', 'error': 429}
    ```
This error means you've tried too many time. Try again in 2-3 minutes or (Run again from first step)

## End Note

If you read https://github.com/reddit-archive/reddit/wiki/OAuth2, then under Authorization

They mention about the parameter named scope in the table, one may edit scope in the code in auth.py to add relevant values as per their need.
    
    ``` shell
    scope = "submit privatemessages read <add values>"
    ```

## Alternative Method
If it doesn't work and you end up with errors again and again a direct approach is shown in the file:

    ```shell
    direct_auth.py
    ```
One hs to copy all the code and print the bearer token by running the file.

