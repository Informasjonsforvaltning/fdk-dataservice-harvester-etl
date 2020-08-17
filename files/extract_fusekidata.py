
import json
import requests
import os

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()

url = 'http://fdk-dataservice-harvester:8080/catalogs'

print("Posting to the following url: ", url)
# Load the publisher by posting the data:
r = requests.post(url)
with open(args.outputdirectory + 'dataservices.ttl', 'w', encoding="utf-8") as outfile:
    json.dump(r.json(), outfile, ensure_ascii=False, indent=4)
