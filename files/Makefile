.PHONY: test
all: extract transform load

extract:
	echo "Extracting fusekidata and dataservices..."
	python3 ./extract_dataservices.py -o ./tmp/
	python3 ./extract_fusekidata.py -o ./tmp/

transform:
	echo "Transforming dataservices...."
	python3 -u ./transform_dataservices.py -o ./tmp/

load:
	echo "Loading dataservices...."
	python3 ./load_dataservices.py -o ./tmp/

clean:
	rm ./tmp/*.json
