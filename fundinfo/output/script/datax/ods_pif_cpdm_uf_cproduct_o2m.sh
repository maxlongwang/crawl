#!/bin/bash
# sed -i 's/\r$//'
DIRECTORY=/opt/datax/datax/job
cd ${DIRECTORY}
#3python ../bin/datax.py ods_pif_cpdm_uf_cproduct_o2m_pre.json
#3nan=$(cat ./csv/ods_pif_cpdm_uf_cproduct_o2m_nan*)
#3echo '------------------------------------'
#3echo 'nan=' $nan
#3echo '------------------------------------'

#4python ../bin/datax.py ods_pif_cpdm_uf_cproduct_o2m.json -p "-Dnan=${nan}"

#2echo '------------------------------------'
#2echo ${1}
#2echo '------------------------------------'
#2python ../bin/datax.py ods_pif_cpdm_uf_cproduct_o2m.json -p "-Dnan=${1}"

python ../bin/datax.py ods_pif_cpdm_uf_cproduct_o2m.json

