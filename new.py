import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client["mydata"]
collection=db['newdata']
# .....insert one data
mydict={'name':'shyni','age':'26','address':'kanjapuram'}
x=collection.insert_one(mydict)
print(x)
# .......Right click and .run.......
# ....insert many data.....
mydict=[{'name':'shyni','age':'26','address':'kanjampuram'},
        {'name':'shalu','age':'30','address':'kollemcode'}]
x=collection.insert_many(mydict)
print(x)
print(x.inserted_ids)
for i in collection.find():
    print(i)
# # ....run....
# then open the mongodb compass ->click connect->click mydata->newdata->show all data
# # ...filter the address..
query={'address':'kollemcode'}
doc=collection.find(query)
for i in doc:
    print(i)
# # ....run.....
# # ....update the data..
oldquery={'address':'kollemcode'}
newquery={'$set':{'address':'mtm'}}
collection.update_many(oldquery,newquery)
for i in collection.find():
    print(i)
#.....run...
# # delete data one...
query={'name':'shyni'}
collection.delete_one(query)
for i in collection.find():
    print(i)
# .....run....
# # delete many data
x=collection.delete_many({})
print(x.deleted_count,"document deleted")
for i in collection.find():
    print(i)
# .....run...
# # delete database
collection.drop()
for i in collection.find():
    print(i)