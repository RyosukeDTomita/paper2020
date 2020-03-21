#!/bin/bash
# parameter setting
for n in {1..24}; do
#14400..15120
DAY=$((14370+$n*30))#bashの算術展開
region=0/115/0/75 #x,y
proj=x0.2/0.2
frame=a10f10/a10f10WeSn
vector=0.15+e-W1p
path="/home3/tomita/tomitasoturon2020/model/"
directry="soturonwtave/"
psfile1="${path}${directry}0${DAY}v.ps" #vectordiagram
psfile2="${path}${directry}0${DAY}t.ps" #watertemparature
psfile3="${path}${directry}0${DAY}d.ps" #upper layer height
confile1="${path}${directry}0${DAY}v.png"
confile2="${path}${directry}0${DAY}t.png"
confile3="${path}${directry}0${DAY}d.png"
infile="${path}${directry}BP222_0${DAY}_00_00" #created by ito.f
tmpfile1="${path}${directry}tmp1" #vectorfile
tmpfile2="${path}${directry}tmp2" #pressure file
tmpfile3="${path}${directry}tmp3" #seasurface temparature
tmpfile4="${path}${directry}tmp4" #1layer height
grdfile2="${tmpfile2}.grd"
grdfile3="${tmpfile3}.grd"
grdfile4="${tmpfile4}.grd"
#
#extract record number and free-air anomaly using awk
#
awk 'NR%25==0 {print $1,$2,(180/3.14)*atan2($8,$7),sqrt($7^2+$8^2)*10}' $infile >$tmpfile1
awk '{print $1,$2,$6}' $infile >$tmpfile2 #pressure file
awk '{print $1,$2,$3}' $infile >$tmpfile3 #seasurface temparature
awk '{print $1,$2,$9}' $infile >$tmpfile4 #1layer height
#
makecpt -Crainbow -T0/1200/800 -Z > rb.cpt
xyz2grd $tmpfile2 -G$grdfile2 -I1 -R$region
#

#vector and pressure
gmt grdimage $grdfile2 -J$proj -Crb.cpt -B$frame  -K -V > $psfile1
gmt psxy $tmpfile1 -R$region -J$proj -Sv$vector -Gblack -K -V -O >> $psfile1
gmt psbasemap -R$region -J$proj -B$frame -O -V -K >> $psfile1
gmt grdcontour $grdfile2 -C50 -A100 -R$region -J$proj -W1 -K -V -O >> $psfile1
gmt psscale -D5/-1/10/1.0h -Crb.cpt -Bf1a2 -O -V >> $psfile1
convert -density 300x300 $psfile1 $confile1
##

#sea surface temperature
makecpt -Crainbow -T0/24/2 -Z > rb.cpt
xyz2grd $tmpfile3 -G$grdfile3 -I1 -R$region
gmt grdimage $grdfile3 -J$proj -Crb.cpt -B$frame -K -V > $psfile2
gmt psbasemap -R$region -J$proj -B$frame -O -V -K >> $psfile2
gmt grdcontour $grdfile3 -C1 -A1 -R$region -J$proj -W1 -K -V -O >> $psfile2
gmt psscale -D5/-1/10/0.5h -Crb.cpt -Bf1a2 -O -V >> $psfile2
convert -density 300x300 $psfile2 $confile2
##

#1layer depth
makecpt -Crainbow -T0/300/100 -Z > rb.cpt
xyz2grd $tmpfile4 -G$grdfile4 -I1 -R$region
gmt grdimage $grdfile4 -J$proj -Crb.cpt -B$frame -K -V > $psfile3
gmt psbasemap -R$region -J$proj -B$frame -O -V -K >> $psfile3
gmt grdcontour $grdfile4 -C10 -A10 -R$region -J$proj -W1 -K -V -O >> $psfile3
gmt psscale -D5/-1/10/0.5h -Crb.cpt -Bf1a2 -O -V -K >> $psfile3
convert -density 300x300 $psfile3 $confile3
done


