import requests
import json

res = requests.get("https://jsonplaceholder.typicode.com/posts")
final = res.text
ss = json.loads(final)
print(ss[0]["title"])
