import pymongo
myclient =pymongo.MongoClient('url')
mydb=myclient['db_name'] # gets the database
print(myclient.list_database_names()) #list the database names
colle = mydb['collection_name']  # creates collection if not there
list_of_colle = mydb.list_collections()
mydict = { "name": "John", "address": "Highway 37" }
mydict1 = [{ "name": "John", "address": "Highway 37" }]
x= colle.insert_one(mydict) # inserts the data
print(x.inserted_id) # returns the inserted id
x2=colle.insert_many(mydict1)
find_in_coll= colle.find_one() # return the first occurance
find_in_coll1 = colle.find() # returns all occurances in selection
myquery = { "address": "Park Lane 38" }

mydoc = colle.find(myquery) # When finding documents in a collection, you can filter the result by using a query object.
sorting=colle.find().sort('name')#Use the sort() method to sort the result in ascending or descending order.
sorting=colle.find().sort('name',-1)#this sorts in descending order
myquery1 = { "address": "Mountain 21" }
delete_one=colle.delete_one(myquery1) # deletes one document
colle.delete_many({}) # deletes many docs
colle.drop() # it returns true , if collection dropped successfully
x = { "address": { "$regex": "^S" } }
y = { "$set": { "name": "Minnie" } }
colle.update_one(x,y) # updates one record
colle.update_many(x,y) #updates many documents
myresult = colle.find().limit(5) # limits the documents in collection





