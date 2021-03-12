import json
import os
from pymongo import MongoClient
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()
connection = MongoClient(
    f"""mongodb://{os.environ['MONGO_USERNAME']}:{os.environ['MONGO_PASSWORD']}@mongodb:27017/dataServiceHarvester?authSource=admin&authMechanism=SCRAM-SHA-1""")

# Old dataservices
db = connection.dataServiceHarvester
dict_list = list(db.dataservice.find())
dataservices = {}
for id_dict in dict_list:
    dataservice = {}
    id_str = id_dict["_id"]
    fdkId_str = id_dict["fdkId"]
    issued_str = id_dict["issued"]
    modified_str = id_dict["modified"]
    dataservice["_id"] = id_str
    dataservice["fdkId"] = fdkId_str
    dataservice["issued"] = issued_str
    dataservice["modified"] = modified_str
    dataservices[id_str] = dataservice


with open(args.outputdirectory + 'mongo_dataservices.json', 'w', encoding="utf-8") as outfile:
    json.dump(dataservices, outfile, ensure_ascii=False, indent=4)

# New dataservices
db = connection.dataServiceHarvester
dict_list = list(db.dataserviceMeta.find({}, {"_id": 1}))
dataservices = []
for id_dict in dict_list:
    dataservices.append(id_dict["_id"])

with open(args.outputdirectory + 'mongo_dataservicesMeta.json', 'w', encoding="utf-8") as outfile:
    json.dump(dataservices, outfile, ensure_ascii=False, indent=4)

# Old catalogs
db = connection.dataServiceHarvester
dict_list = list(db.catalog.find())
catalogs = []
for id_dict in dict_list:
    catalog = {}
    id_str = id_dict["_id"]
    fdkId_str = id_dict["fdkId"]
    issued_str = id_dict["issued"]
    modified_str = id_dict["modified"]
    catalog["_id"] = id_str
    catalog["fdkId"] = fdkId_str
    catalog["issued"] = issued_str
    catalog["modified"] = modified_str
    catalogs[id_str] = catalog

with open(args.outputdirectory + 'mongo_catalogs.json', 'w', encoding="utf-8") as outfile:
    json.dump(catalogs, outfile, ensure_ascii=False, indent=4)

# New catalogs
db = connection.dataServiceHarvester
dict_list = list(db.catalogMeta.find({}, {"_id": 1}))
catalogs = []
for id_dict in dict_list:
    catalogs.append(id_dict["_id"])

with open(args.outputdirectory + 'mongo_catalogsMeta.json', 'w', encoding="utf-8") as outfile:
    json.dump(catalogs, outfile, ensure_ascii=False, indent=4)