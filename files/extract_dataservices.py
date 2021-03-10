import json
import os
import re
from pymongo import MongoClient
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()

connection = MongoClient(
    f"""mongodb://{os.environ['MONGO_USERNAME']}:{os.environ['MONGO_PASSWORD']}@mongodb:27017/dataServiceHarvester?authSource=admin&authMechanism=SCRAM-SHA-1""")
db = connection.dataServiceHarvester
dict_list = list(db.dataservice.find({}, {"_id": 1}))
dataservices = {}
for id_dict in dict_list:
    id_str = id_dict["_id"]
    fdkId_str = id_dict["fdkId"]
    issued_str = id_dict["issued"]
    modified_str = id_dict["modified"]
    dataservices[id_str] = id_str
    dataservices[issued_str] = issued_str
    dataservices[modified_str] = modified_str

with open(args.outputdirectory + 'mongo_dataservices.json', 'w', encoding="utf-8") as outfile:
    json.dump(dataservices, outfile, ensure_ascii=False, indent=4)

connection = MongoClient(
    f"""mongodb://{os.environ['MONGO_USERNAME']}:{os.environ['MONGO_PASSWORD']}@mongodb:27017/dataServiceHarvester?authSource=admin&authMechanism=SCRAM-SHA-1""")
db = connection.dataServiceHarvester
dict_list = list(db.dataserviceMeta.find({}, {"_id": 1}))
dataservices = []
for id_dict in dict_list:
    dataservices.append(id_dict["_id"])

with open(args.outputdirectory + 'mongo_dataservicesMeta.json', 'w', encoding="utf-8") as outfile:
    json.dump(dataservices, outfile, ensure_ascii=False, indent=4)
