#!/bin/bash
# sed -i 's/\r$//'
LOGFILE=/opt/datax/datax/log/`date +'%Y-%m-%d'`/job_err_`date +'%Y%m%d'`.log
logtime=`date +'%Y-%m-%d %H:%m:%S'`
RESULT=0
DIRECTORY=/opt/datax/datax/job
cd $DIRECTORY

busi_date=${1}
{content}
exit $RESULT


