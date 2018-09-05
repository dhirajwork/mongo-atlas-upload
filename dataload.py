from pymongo import MongoClient
from pprint import pprint
print("Enter your mongo string")
address=raw_input()
client = MongoClient(address)
db=client['thedata']
collect=db['collection']

field=[]
with open("field.csv") as infile:
	for line in infile:
		word=line.split(',')
		field.append(word[1])
field.pop(0)

listdict=[]

with open("data.csv") as infile:
	for line in infile:
		word=line.split(',')
		dict={}
		for i in range(0,len(field)):
			try:
				dict[field[i]]=int(word[i].strip('\n'))
			except:
				dict[field[i]]=word[i].strip('\n')            #collect.insert_one(dict)
		listdict.append(dict)
		if len(listdict) ==1000:
			collect.insert_many(listdict)
			listdict.clear()


collect.insert_many(listdict)
listdict.clear()
