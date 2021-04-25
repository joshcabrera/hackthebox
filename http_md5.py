#for HTB "emdee five for life" challenge

import hashlib
import requests

url = "http://138.68.178.56:32226/"
sesh = requests.session()
req = sesh.get(url)

string_to_hashed = req.text[167:187]
print (string_to_hashed)
result = hashlib.md5(string_to_hashed.encode()).hexdigest()
print (result)

response2 = sesh.post(url, data={'hash':result})
print (response2.text)
