#!/bin/bash
# parameter setting
region=0/115/0/75
proj=x0.1/0.1
frame=a10f10/a10f10WeSn
vector=0.15+e-W1p
psfile1=/home/tomita/model/result/velocitydata.ps
infile1=/home/tomita/model/result/EBP222_000010_00_00
infile2=/home/tomita/model/result/EBP222_000020_00_00
infile3=/home/tomita/model/result/EBP222_000030_00_00
infile4=/home/tomita/model/result/EBP222_000040_00_00
infilet1=/home/tomita/model/result/ABP222_000010_00_00
infilet2=/home/tomita/model/result/ABP222_000020_00_00
infilet3=/home/tomita/model/result/ABP222_000030_00_00
infilet4=/home/tomita/model/result/ABP222_000040_00_00
elbfile1=/home/tomita/model/result/TBP222_000010_00_00
elbfile2=/home/tomita/model/result/TBP222_000020_00_00
elbfile3=/home/tomita/model/result/TBP222_000030_00_00
elbfile4=/home/tomita/model/result/TBP222_000040_00_00
tmpfile1=/home/tomita/model/result/velocitydata3600
tmpfile2=/home/tomita/model/result/velocitydata3690
tmpfile3=/home/tomita/model/result/velocitydata3780
tmpfile4=/home/tomita/model/result/velocitydata3870
confile1=/home/tomita/model/result/velocitydata.png
samplefile=/home/tomita/model/samplefile
grdfile1=/home/tomita/model/result/ABP222_003600.grd
grdfile2=/home/tomita/model/result/ABP222_003690.grd
grdfile3=/home/tomita/model/result/ABP222_003780.grd
grdfile4=/home/tomita/model/result/ABP222_003870.grd
grdfile5=/home/tomita/model/result/TBP222_003600.grd
grdfile6=/home/tomita/model/result/TBP222_003690.grd
grdfile7=/home/tomita/model/result/TBP222_003780.grd
grdfile8=/home/tomita/model/result/TBP222_003870.grd
samplefile2=/home/tomita/model/samplefile2
x=-13
y=-10
#
#extract record number and free-air anomaly using awk
#
#awk '{print $1,$2,$6,$5*10}' $infile >$tmpfile
awk 'NR%30==0 {print$1,$2,$6,$5*20}' $infile1 >$tmpfile1
awk 'NR%30==0 {print$1,$2,$6,$5*20}' $infile2 >$tmpfile2
awk 'NR%30==0 {print$1,$2,$6,$5*20}' $infile3 >$tmpfile3
awk 'NR%30==0 {print$1,$2,$6,$5*20}' $infile4 >$tmpfile4
makecpt -Crainbow -T0/24/2 -Z > rb.cpt
xyz2grd $infilet1 -G$grdfile1 -I1 -R$region
xyz2grd $infilet2 -G$grdfile2 -I1 -R$region
xyz2grd $infilet3 -G$grdfile3 -I1 -R$region
xyz2grd $infilet4 -G$grdfile4 -I1 -R$region
xyz2grd $elbfile1 -G$grdfile5 -I1 -R$region
xyz2grd $elbfile2 -G$grdfile6 -I1 -R$region
xyz2grd $elbfile3 -G$grdfile7 -I1 -R$region
xyz2grd $elbfile4 -G$grdfile8 -I1 -R$region
#
gmt grdimage $grdfile1 -J$proj -Crb.cpt -B$frame -Y13 -K -V > $psfile1
gmt psxy $tmpfile1 -R$region -J$proj -Sv$vector -Gblack -K -V -O >> $psfile1
#gmt pstext $samplefile2 -R$region -J$proj -N -K -V -O >> $psfile1
gmt psbasemap -R$region -J$proj -B$frame -O -V -K >> $psfile1
#gmt psxy $samplefile -R$region -J$proj -Sv0.15i+ea-W1 -Gblack -N -O -V -K >> $psfile1
gmt grdcontour $grdfile5 -C10 -A10 -R$region -J$proj -W1 -K -V -O >> $psfile1
gmt psscale -D5/-1/10/0.5h -Crb.cpt -Bf1a2 -K -O -V >> $psfile1
#convert -density 300x300 $psfile1 $confile1

gmt grdimage $grdfile2 -J$proj -Crb.cpt -B$frame -X13 -K -V -O >> $psfile1
gmt psxy $tmpfile2 -R$region -J$proj -Sv$vector -Gblack  -K -V -O >> $psfile1
gmt pstext $samplefile2 -R$region -J$proj -N -K -V -O >> $psfile1
gmt psbasemap -R$region -J$proj -B$frame -O -V -K >> $psfile1
gmt psxy $samplefile -R$region -J$proj -Sv$vector -Gblack -N -K -O -V >> $psfile1
gmt grdcontour $grdfile6 -C10 -A10 -R$region -J$proj -W1 -K -V -O >> $psfile1
gmt psscale -D5/-1/10/0.5h -Crb.cpt -Bf1a2 -O -V -K >> $psfile1
#convert -density 300x300 $psfile1 $confile1

gmt grdimage $grdfile3 -J$proj -Crb.cpt -B$frame -X$x -Y$y -K -V -O >> $psfile1
gmt psxy $tmpfile3 -R$region -J$proj -Sv$vector -Gblack -W0.7 -K -V -O >> $psfile1
#gmt pstext $samplefile2 -R$region -J$proj -N -K -V -O >> $psfile1
gmt psbasemap -R$region -J$proj -B$frame -O -V -K >> $psfile1
#gmt psxy $samplefile -R$region -J$proj -Sv0.15i+ea-W1 -Gblack -N -K -O -V >> $psfile1
gmt grdcontour $grdfile7 -C10 -A10 -R$region -J$proj -W1 -K -V -O >> $psfile1
gmt psscale -D5/-1/10/0.5h -Crb.cpt -Bf1a2 -K -O -V >> $psfile1
#convert -density 300x300 $psfile3 $confile1

gmt grdimage $grdfile4 -J$proj -Crb.cpt -B$frame -X13 -K -V -O >> $psfile1
gmt psxy $tmpfile4 -R$region -J$proj -Sv$vector -Gblack -W0.7 -K -V -O >> $psfile1
gmt pstext $samplefile2 -R$region -J$proj -N -K -V -O >> $psfile1
gmt psbasemap -R$region -J$proj -B$frame -O -V -K >> $psfile1
gmt psxy $samplefile -R$region -J$proj -Sv$vector -Gblack -N -K -O -V >> $psfile1
gmt grdcontour $grdfile8 -C10 -A10 -R$region -J$proj -W1 -K -V -O >> $psfile1
gmt psscale -D5/-1/10/0.5h -Crb.cpt -Bf1a2 -O -V >> $psfile1
convert -density 300x300 $psfile1 $confile1
# 



