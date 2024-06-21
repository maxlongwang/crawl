#!/bin/bash
# sed -i 's/\r$//'
DIRECTORY=/opt/datax/datax/job
cd ${DIRECTORY}
#3python ../bin/datax.py ads_m_cabin_asset_uf_cactivity_o2m_pre.json
#3init_date=$(cat ./csv/ads_m_cabin_asset_uf_cactivity_o2m_init_date*)
#3echo '------------------------------------'
#3echo 'init_date=' $init_date
#3echo '------------------------------------'

#4python ../bin/datax.py ads_m_cabin_asset_uf_cactivity_o2m.json -p "-Dinit_date=${init_date}"

echo '------------------------------------'
echo ${1}
echo '------------------------------------'
python ../bin/datax.py ads_m_cabin_asset_uf_cactivity_o2m.json -p "-Dinit_date=${1}"

#1python ../bin/datax.py ads_m_cabin_asset_uf_cactivity_o2m.json

