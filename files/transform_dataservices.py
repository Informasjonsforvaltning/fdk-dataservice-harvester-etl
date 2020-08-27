import json

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()


def transform(data):
    # Transforming according to rules in README
    array = data["hits"]["hits"]
    print (len(array))
    transformed = {}
    for dataservice in array:
        dataservice2 = {"doc": {"id": dataservice["_id"],
                                "uri": dataservice["_source"]["uri"],
                                "harvest": {"firstHarvested": dataservice["_source"].get("harvest")["firstHarvested"],
                                            "lastHarvested": dataservice["_source"].get("harvest")["lastHarvested"],
                                            "changed": dataservice["_source"].get("harvest")["changed"]}}}
        transformed[dataservice.get("apiSpecUrl")] = dataservice2
    print ("Total to be transformed: ", len(transformed))
    return transformed


inputfileName = args.outputdirectory + "dataservices.json"
outputfileName = args.outputdirectory + "dataservice_metadata.json"
with open(inputfileName) as json_file:
    data = json.load(json_file)
    # Transform the organization object to publihser format:
    with open(outputfileName, 'w', encoding="utf-8") as outfile:
        json.dump(transform(data), outfile, ensure_ascii=False, indent=4)
