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
        first = dataservice["_source"].get("harvest")["firstHarvested"]
        dataservice2 = {"doc": {"id": dataservice["_id"],
                                "harvest": {"firstHarvested": first,
                                            "lastHarvested": dataservice["_source"].get("harvest")["lastHarvested"],
                                            "changed": mapchanged(dataservice["_source"].get("harvest")["changed"], first)
                                            }
                                }
                        }
        transformed[dataservice.get("apiSpecUrl")] = dataservice2
    print ("Total to be transformed: ", len(transformed))
    return transformed


def mapchanged(changed, first):
    array = []
    if changed:
        return changed
    return array.append(first)


inputfileName = args.outputdirectory + "dataservices.json"
outputfileName = args.outputdirectory + "dataservice_metadata.json"
with open(inputfileName) as json_file:
    data = json.load(json_file)
    # Transform the organization object to publihser format:
    with open(outputfileName, 'w', encoding="utf-8") as outfile:
        json.dump(transform(data), outfile, ensure_ascii=False, indent=4)
