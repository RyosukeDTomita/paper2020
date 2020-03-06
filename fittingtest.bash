#!/bin/bash
#parameter setting
for AA in {1..12}; do
BB=`printf %02d ${AA}`
region=/0/115/0/75
proj=x0.2/0.2
frame=a10f10/a10f10WeSn
#fmemori a mozikannkaku g keiidosenkannkaku
psfile=/home3/tomita/tomitasoturon2020/JRA55/fit/${BB}fit.ps
infile=/home3/tomita/tomitasoturon2020/JRA55/fit/${BB}fit.dat
tmp=/home3/tomita/tomitasoturon2020/JRA55/fit/tmpfile
insamplefile=/home3/tomita/tomitasoturon2020/JRA55/fit/sampledata.dat
samplefile=/home3/tomita/tomitasoturon2020/JRA55/fit/sample.dat
confile=/home3/tomita/tomitasoturon2020/JRA55/fit/${BB}fit.png
vector=0.15+e-W1p
#
#extract record number and free-air anomaly using awk↲
#
#    awk 'NR%25==0 {printf "%10.3f %10.3f %10.3f %10.3f\n",$2,$1,$6,$5*0.05' $infile > $tmp↲
 awk 'NR%25==0 {print$2,$1,$6,$5*0.1}' $infile > $tmp
 awk '{print$1,$2,$3,$4*0.1}' $insamplefile > $samplefile
#    awk '{printf "%5.1f %5.1f %5.1f %5.1f\n", $1,$2,$3,$4*0.05 }' dat1 > $samplefile↲

gmt psxy $tmp -R$region -J$proj -Sv$vector -Gblack -K -V > $psfile
#    gmt psxy $tmp -R$region -J$proj -Sv/0.1/0.1/0.1 -Gblack -K -V > $psfile↲
#    gmt pscoast -R$region -J$proj -Dh -Ggray -Wthin,black -K -V -O >> $psfile↲
gmt psbasemap -R$region -J$proj -B$frame -K -V -O >> $psfile
gmt psxy $samplefile -R$region -J$proj -Sv$vector -Gblue -O -V >> $psfile
convert -density 300x300 $psfile $confile
done
#
