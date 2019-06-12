from pymongo import MongoClient
import json
from bson import ObjectId, json_util
import os

client = MongoClient('mongodb+srv://udal_singh:e2cSPZxTlZ45UKLo@zoomtail-dev-cluster-xtumr.mongodb.net/test?retryWrites=true')

db = client.test

class JSONEncoder(json.JSONEncoder):
    """
    This custom json encoder class will return str(obj) if it's type is
    object id else it will return the default call to JSONEncoder
    """
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

list_of_suppliers = ['Fabfirki', 'Prachi Creation']

if not os.path.exists('./zoomtail'):
    os.makedirs('zoomtail')

for sup in list_of_suppliers:
    products = db.products.find({"suppliersData.supplierName": sup})

    # Find list of product types
    # print(sup)
    # print(set([prod['categoryName'] for prod in products]))
    with open('zoomtail/' + sup + '.json', 'w') as fp:
        # Writing only kurtis to json dump
        fp.write(json_util.dumps([prod for prod in products if prod['categoryName'] == 'Kurtis']))

client.close()

