import requests


LOGINURL = 'https://news.ycombinator.com/login'
DATAURL = 'https://data.example.com/secure_data.html'

SUBMIT_POST_URL= 'https://news.ycombinator.com/submit'
session = requests.session()

req_headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

formdata = {
    'goto': "news",
    'acct': USERNAME,
    'pw' : PASSWORD
}


# Authenticate
r = session.post(LOGINURL, data=formdata, headers=req_headers)
submit_page = session.get(SUBMIT_POST_URL)
# print(r.headers)
# print(r.status_code)
print(submit_page.status_code)