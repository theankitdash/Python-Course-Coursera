import json
from urllib.request import urlopen

count = 0
sum = 0
url = input("Enter Url - ")

data = urlopen(url).read()

print (data)

info = json.loads(data)

for i in info['comments']:
    count = count+1
    sum = sum + i['count']
print ("Sum : ",sum)
print ("count : ",count)