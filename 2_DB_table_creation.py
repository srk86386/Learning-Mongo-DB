#creating a DB, collection and adding data
from pymongo import MongoClient

democlient = MongoClient()
myclient = MongoClient('localhost', 27017)

mydb = myclient['demo'] # db name
mycoll=mydb['dbtable'] # collection name which is same as table name for sql db


mylist = [
	{'id': 1, 'name': 'Rahul Singh', 'mobile' : '8097846982'},
	{'id': 2, 'name': 'Pallavi Hankare', 'mobile' : '8693881508'},
	{'id': 3, 'name': 'Aashish Gupta', 'mobile' : '8082245459'},
	{'id': 4, 'name': 'Aashu Singh', 'mobile' : '87846982'},
	{'id': 5, 'name': 'Vivek Tivari', 'mobile' : '8097846982'},
	]

x = mycoll.insert_many(mylist) # insert query for more than 1 row. for one row 'insert_one'

dblist = myclient.list_database_names() #getting the list of available databases

if input('Enter DB') in dblist:
	print('The databse exist.')
else:
	print('Not present')

print(dblist)
