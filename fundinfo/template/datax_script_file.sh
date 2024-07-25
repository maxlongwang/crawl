#!/bin/bash
# sed -i 's/\r$//'
LOGFILE=/opt/datax/datax/log/`date +'%Y-%m-%d'`/job_err_`date +'%Y%m%d'`.log
logtime=`date +'%Y-%m-%d %H:%m:%S'`
RESULT=0
DIRECTORY=/opt/datax/datax/job
cd $DIRECTORY

start_date=${1}
end_date=${1}
end_date2=`date -d "$start_date +1 days" +'%Y%m%d'`
month_date=${1:0:6}
{content}
exit $RESULT


