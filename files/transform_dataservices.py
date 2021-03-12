import json
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()
update_dates = os.environ["TO_BE_UPDATED"] == 'dates'


def transform(inputfile, inputfile_meta, failed_path):

    dataservices = openfile(inputfile)
    dataservices_meta = openfile(inputfile_meta)

    transformed = {}
    failed = {}

    for dataservice_key in dataservices:
        if dataservices[dataservice_key]["_id"] not in dataservices_meta:
            failed[dataservice_key] = (dataservices[dataservice_key]["_id"])
        else:
            transformed[dataservices[dataservice_key]["_id"]] = fields_to_change(dataservices[dataservice_key])

    with open(failed_path, 'w', encoding="utf-8") as failed_file:
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
inputfileNameMeta = args.outputdirectory + "mongo_dataservicesMeta.json"
outputfileName = args.outputdirectory + "dataservices_transformed.json"
failedfileName = args.outputdirectory + "failed_transform_dataservices.json"
with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(inputfileName, inputfileNameMeta, failedfileName), outfile, ensure_ascii=False, indent=4)

# Catalogs
inputfileName = args.outputdirectory + "mongo_catalogs.json"
inputfileNameMeta = args.outputdirectory + "mongo_catalogsMeta.json"
outputfileName = args.outputdirectory + "catalogs_transformed.json"
failedfileName = args.outputdirectory + "failed_transform_catalogs.json"
with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(inputfileName, inputfileNameMeta, failedfileName), outfile, ensure_ascii=False, indent=4)