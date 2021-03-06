import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0

while True:
    url = input('Enter location:')
    if len(url) < 1: break
    print('Retrieving',url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read().decode()
    print('Retrieved',len(data),'characters')
    try:
        js = json.loads(data)
    except:
        js = None

    info = json.loads(data)
    print("Count:",len(info))

    for item in info["comments"]:
        number = item['count']
        sum = sum + int(number)
    break

print("Sum:",sum)
