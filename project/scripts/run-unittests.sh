#!/bin/bash
coverage run --omit */*test_*,*myoswrap.py,*customExceptions.py,*__init__.py,/usr/*,/home/lubuntu/.local/* -m unittest discover -s ./project -v

>./project/scripts/reporting/coverage/report.txt
coverage report >> ./project/scripts/reporting/coverage/report.txt
echo "---Report with txt done---"

coverage html -d ./project/scripts/reporting/coverage/html
echo "---Report with html done---"
