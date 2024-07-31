#!/bin/bash
# sed -i 's/\r$//'
#parameter: start_date,end_date,type: 1 day,2 month,3 year,4 week  json_file
startdate=${1}
enddate=${2}
type=${3}
json_file=${4}

directory=/opt/datax/datax/job
cd $directory

while [ $startdate -lt $enddate ]; do

    if [ $type -eq 1 ]; then
        end_date=`date -d "$startdate +1 days" +'%Y%m%d'`
        python ../bin/datax.py $json_file -p "-Dstart_date=$startdate -Dend_date=$end_date"
        startdate=`date -d "$end_date +1 days" +'%Y%m%d'`

    elif [ $type -eq 2 ]; then
        end_date=`date -d "$startdate +1 month" +'%Y%m%d'`
        end_date=$(( $end_date< $enddate ? $end_date:$enddate ))
        python ../bin/datax.py $json_file -p "-Dstart_date=$startdate -Dend_date=$end_date"
        startdate=`date -d "$end_date +1 days" +'%Y%m%d'`

    elif [ $type -eq 3 ]; then
        end_date=`date -d "$startdate +1 year" +'%Y%m%d'`
        end_date=$(( $end_date< $enddate ? $end_date:$enddate ))
        python ../bin/datax.py $json_file -p "-Dstart_date=$startdate -Dend_date=$end_date"
        startdate=`date -d "$end_date +1 days" +'%Y%m%d'`

    elif [ $type -eq 4 ]; then
        end_date=`date -d "$startdate +1 week" +'%Y%m%d'`
        end_date=$(( $end_date< $enddate ? $end_date:$enddate ))
        python ../bin/datax.py $json_file -p "-Dstart_date=$startdate -Dend_date=$end_date"
        startdate=`date -d "$end_date +1 days" +'%Y%m%d'`

    fi

done