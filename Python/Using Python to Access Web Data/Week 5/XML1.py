import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter URL: ")
uOpen = urllib.request.urlopen(url)
data = uOpen.read()

tree = ET.fromstring(data)
results = tree.findall('comments/comment')

count = 0
sum = 0

for item in results:
    x = int(item.find('count').text)
    count = count+1
    sum = sum+x

print(f'Count: {count}\nSum: {sum}')
