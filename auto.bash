
#speedtest
#starttime
starttime=$(date)
starttimeh=$(date +'%H')
starttimem=$(date +'%M')
starttimes=$(date +'%S')
starttimej=$(date +'%j')
#execute job
#dclfrt copyr2.f && ./a.out && python notify.py && python frito.py 
#dclfrt ito.f && ./a.out && python notify.py && python frito.py 
dclfrt windfitting.f90 && ./a.out
#
#output how long does it take to execute jobs
endtimeh=$(date +'%H')
endtimem=$(date +'%M')
endtimes=$(date +'%S')
endtimej=$(date +'%j')

j=$(($endtimej-$starttimej))
h=$(($endtimeh-$starttimeh))
m=$(($endtimem-$starttimem))
s=$(($endtimes-$starttimes))
if [ $((s)) -lt 0 ]; then
    m=$(($m-1))
    s=$(($s+60))
fi
if [ $((m)) -lt 0 ]; then
    m=$(($m+60))
    h=$(($h-1))
fi
if [ $((h)) -lt 0 ]; then
    j=$(($j-1))
    h=$(($h+24))
fi
echo "starttime=$starttime"
echo "endtime=$(date)"
echo "caltime=$j(days)$h(hours)$m(min)$s(s)"

# source ./auto.bash
