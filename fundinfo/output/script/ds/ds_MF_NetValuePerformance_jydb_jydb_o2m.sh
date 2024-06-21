#!/bin/bash
# sed -i 's/\r$//'
ssh 192.168.144.43 <<eof
/opt/datax/datax/script/MF_NetValuePerformance_jydb_jydb_o2m.sh ${1}

eof

exit
