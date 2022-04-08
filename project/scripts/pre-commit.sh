#!/bin/bash

#coverage run --omit */*test_*,*myoswrap.py,*customExceptions.py,*__init__.py,/usr/*,/home/lubuntu/.local/* -m unittest discover -s ./project -v
bash ./project/scripts/run-unittests.sh
if [ $? -ne 0 ]
then
	echo "Unittest failed, aborting..."
	exit 1
else
	echo "Unittest succeeded! Preparing for deployment test..."
	bash ./project/scripts/run-deploymenttests.sh
	if [ $? -ne 0 ]
	then
		echo "Deployment test failed, aborting..."
		exit 1
	else
		echo "Deployment test succeeded! Commit is possible!"
	fi
fi

