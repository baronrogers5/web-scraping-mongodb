from pymongo import MongoClient
from pprint import pprint

client = MongoClient()

# print(client)
db = client.test
dummy_data = db.dummy_data

some_test_data = {"name": "Something", "age": 200}
some_test_array = [{"name": "Something", "age": 200},
{"name": "Something1", "age": 200},{"name": "Something1", "age": 100},{"name": "Something", "age": 300}]

# result = dummy_data.insert_many(some_test_array)

# for ids in result.inserted_ids:
#    print("Inserted Id is: ", ids)

# pprint(dummy_data.find_one())

# Find based on condition
for data in dummy_data.find({ '$or': [{ 'name': 'Something1'},{'name': 'Something'}], 'age': {'$range': [100, 250]}}):
    pprint(data)


client.close()
