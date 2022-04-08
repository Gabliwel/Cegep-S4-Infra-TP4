bash ./runDocker.sh
sleep 3
python3 -m unittest discover -s project/ -p dtest_*.py -v

