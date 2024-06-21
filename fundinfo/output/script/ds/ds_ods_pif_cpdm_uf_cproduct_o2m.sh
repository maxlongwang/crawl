#!/bin/bash
# sed -i 's/\r$//'
ssh 192.168.144.43 <<eof
/opt/datax/datax/script/ods_pif_cpdm_uf_cproduct_o2m.sh ${1}

eof

exit
