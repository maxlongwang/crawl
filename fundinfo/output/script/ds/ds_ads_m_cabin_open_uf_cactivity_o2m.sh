#!/bin/bash
# sed -i 's/\r$//'
ssh 192.168.144.43 <<eof
/opt/datax/datax/script/ads_m_cabin_open_uf_cactivity_o2m.sh ${1}

eof

exit
