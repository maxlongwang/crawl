#!/bin/bash
# sed -i 's/\r$//'
DIRECTORY=/opt/datax/datax/job
cd ${DIRECTORY}
python ../bin/datax.py MF_NetValuePerformance_jydb_jydb_o2m_pre.json
id=$(cat ./csv/MF_NetValuePerformance_jydb_jydb_o2m_id*)
echo '------------------------------------'
echo 'id=' $id
echo '------------------------------------'

python ../bin/datax.py MF_NetValuePerformance_jydb_jydb_o2m.json -p "-Did=${id}"

#2echo '------------------------------------'
#2echo ${1}
#2echo '------------------------------------'
#2python ../bin/datax.py MF_NetValuePerformance_jydb_jydb_o2m.json -p "-Did=${1}"

#1python ../bin/datax.py MF_NetValuePerformance_jydb_jydb_o2m.json

