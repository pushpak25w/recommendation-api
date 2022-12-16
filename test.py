import requests
BASE="http://127.0.0.1:5000/"
response=requests.put(BASE+"category/test",{'title':'"Only you" - The Flying Pickets || lyrics || Fallen Angels 1995'})
data=response.json()
print(data)
