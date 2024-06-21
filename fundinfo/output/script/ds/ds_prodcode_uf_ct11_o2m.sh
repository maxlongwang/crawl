#!/bin/bash
# sed -i 's/\r$//'
ssh 192.168.144.43 <<eof
/opt/datax/datax/script/prodcode_uf_ct11_o2m.sh ${1}

eof

exit
