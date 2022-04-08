import json

fp = open("json.txt", "r")
s = fp.read()

j = json.loads(s)


print (j['lastName'])
print (j['address']['state'])
print (j['phoneNumbers'][0]['number'])
print (j['phoneNumbers'][1]['type'])
