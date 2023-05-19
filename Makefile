# Run this target only the first time you need to build the web app

export PYTHONPATH=${PWD}/lib/:$PYTHONPATH

buildfirstime: installreq
	python3.10 platform/feedwebapp.py

buildrun:
	python3.10 platform/feedwebapp.py

cleandata:
	rm -rf etc/data.csv

gendatacsv:
	python3.10 sbin/random_gen.py >> ${PWD}/etc/data.csv

installreq:
	pip install -r etc/requirements.txt
