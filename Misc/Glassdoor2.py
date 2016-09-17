import urllib, sys
import urllib.request as request

url = "http://api.glassdoor.com/api/api.htm?v=1&format=json&t.p=94453&t.k=eJHCDB4oK3a&action=employers&q=pharmaceuticals&userip=192.168.43.42&useragent=Mozilla/%2F4.0"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url,headers=hdr)
response = urllib.request.urlopen(req)
for x in response:
	print(x)