import json
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()
update_dates = os.environ["TO_BE_UPDATED"] == 'dates'


def transform(inputfile, inputfile_meta):

    dataservices = openfile(inputfile)
    dataservices_meta = openfile(inputfile_meta)

    transformed = {}
    failed = {}
    failed_transform = args.outputdirectory + "failed_transform.json"
    for dataservice in dataservices:
        if dataservice["_id"] not in dataservices_meta:
            failed_transform.append(dataservice["_id"])
        else:
            transformed[dataservice["_id"]] = fields_to_change(dataservice)

    with open(failed_transform, 'w', encoding="utf-8") as failed_file:
        json.dump(failed, failed_file, ensure_ascii=False, indent=4)
    return transformed


def openfile(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


def fields_to_change(dataservice):
    if update_dates is True:
        return {"issued": dataservice["issued"],
                "modified": dataservice["modified"]}
    else:
        return {"fdkId": dataservice["fdkId"]}


# Dataservices
inputfileName = args.outputdirectory + "mongo_dataservices.json"
inputfileNameMeta = args.outputdirectory + "mongo_dataservices_meta.json"
outputfileName = args.outputdirectory + "dataservices_transformed.json"
with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(inputfileName, inputfileNameMeta), outfile, ensure_ascii=False, indent=4)

# Catalogs
inputfileName = args.outputdirectory + "mongo_catalogs.json"
inputfileNameMeta = args.outputdirectory + "mongo_catalogsMeta.json"
outputfileName = args.outputdirectory + "catalogs_transformed.json"
with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(inputfileName, inputfileNameMeta), outfile, ensure_ascii=False, indent=4)