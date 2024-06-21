#!/bin/bash
# sed -i 's/\r$//'
DIRECTORY=/opt/datax/datax/job
cd ${DIRECTORY}
#3python ../bin/datax.py filename_pre.json
#3column_name=$(cat ./csv/filename_column_name*)
#3echo '------------------------------------'
#3echo 'column_name=' $column_name
#3echo '------------------------------------'

#4python ../bin/datax.py filename.json -p "-Dcolumn_name=${column_name}"

#2echo '------------------------------------'
#2echo ${1}
#2echo '------------------------------------'
#2python ../bin/datax.py filename.json -p "-Dcolumn_name=${1}"

#1python ../bin/datax.py filename.json

