
import json
import requests
import os

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()

url = 'http://fdk-dataservice-harvester:8080/catalogs'

print("Getting from the following url: ", url)
# Load the publisher by posting the data:
r = requests.get(url)
with open(args.outputdirectory + 'dataservices.ttl', 'w', encoding="utf-8") as outfile:
    outfile.writelines(r.text, outfile, ensure_ascii=False, indent=4)
