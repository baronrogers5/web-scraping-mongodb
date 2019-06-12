import requests
import logging

# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


headers = {
        'authorization': 'earer eyJraWQiOiI2TW53IiwidHlwIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJhdWQiOiJodHRwczovL2FwaS51ZGFhbi5jb20vIiwic3ViIjoiVVNSRkg2MjlaQkRHRkQyU1pRNk1KQ1BXN1E5OTMiLCJyIjpbInVzZXIiXSwibmJmIjoxNTYwMzIzMTI2LCJpc3MiOiJhdXRoLnVkYWFuLmNvbSIsImV4cCI6MTU2MDMyMzcyNiwibyI6Ik9SRzdXR0tXV0ZIUzBDWEc0VFcySlFLUEM2MUZUIn0.At3RhVgahausaEMeAhrqlvSoeY69r1oOrxB9c-xiCLPwoj7KwIpD8U7iPjqWXdoEXxt1xpDRbmfIwCC59K210g',
        'Referer': 'https://udaan.com/search?q=fabfirki',
        'User-Agent': 'ozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Mobile Safari/537.36'
        }

url = 'https://udaan.com/api/search/v1?q=fabfirki'
res = requests.get(url, headers=headers)

print("\n\nStatus Code", res.status_code)
print("Text", res.text)

# token_url = 'https://udaan.com/auth/token'
# token_headers = {   'Origin': 'https://udaan.com',
#                     'Referer': "https://udaan.com/search?q=fabfirki",
#                     "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Mobile Safari/537.36",
#                     "x-csrf-token": "1YJKZdEf-lnzXq6gCulkqNdry626XJNa-7l4"}
#
# tok_res = requests.post(token_url, headers=token_headers)
#
# print("Token status code", tok_res.status_code)
# print("Token response", tok_res.text)


