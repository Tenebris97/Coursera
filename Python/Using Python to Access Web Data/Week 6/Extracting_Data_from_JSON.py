import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
sum = 0

url = input('Enter Url: ')

print('Retrieving ' + url)
data = urllib.request.urlopen(url, context=ctx).read()

info = json.loads(data)

for item in info["comments"]:
    count += 1
    sum += item["count"]

print(f'Count: {count}\nSum: {sum}')
