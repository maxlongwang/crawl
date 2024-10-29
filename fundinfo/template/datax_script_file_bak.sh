#!/bin/bash
# sed -i 's/\r$//'
LOGFILE=/opt/datax/log/`date +'%Y-%m-%d'`/job_err_`date +'%Y%m%d'`.log
logtime=`date +'%Y-%m-%d %H:%m:%S'`
RESULT=0
DIRECTORY=/opt/datax/job
cd $DIRECTORY

start_date=${1}
end_date=${1}
end_date2=`date -d "$start_date +1 days" +'%Y%m%d'`
month_date=${1:0:6}
busi_date=${1}
cur_mon=`date -d $busi_date +'%-m'`
cur_year=`date -d $busi_date +'%Y'`
last_year=$(($cur_year -1))
if [[ $cur_mon -ge 0 && $cur_mon -le 3 ]]; then
        quarter=${last_year}1231
elif [[ $cur_mon -ge 4 && $cur_mon -le 6 ]]; then
        quarter=${cur_year}0330
elif [[ $cur_mon -ge 7 && $cur_mon -le 9 ]]; then
        quarter=${cur_year}0630
elif [[ $cur_mon -ge 10 && $cur_mon -le 12 ]]; then
        quarter=${cur_year}0930
fi
{content}

exit $RESULT


