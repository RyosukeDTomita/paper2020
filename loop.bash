#!/bin/bash
for AA in {1..12}; do
# parameter setting
    BB=`printf %02d ${AA}`
    region=125/145/30/45
    proj=M15
    frame=f5a5g5
    psfile=/home3/tomita/tomitasoturon2020/JRA55/Yearly/${BB}.ps
    infile=/home3/tomita/tomitasoturon2020/JRA55/Yearly/${BB}.dat
    tmpfile=/home3/tomita/tomitasoturon2020/JRA55/Yearly/tmp
    insamplefile=/home3/tomita/tomitasoturon2020/JRA55/Yearly/sample.dat
    samplefile=/home3/tomita/tomitasoturon2020/JRA55/Yearly/sampledata.dat
    confile=/home3/tomita/tomitasoturon2020/JRA55/Yearly/${BB}.png
    vector=0.15+e-W1p
#
#extract record number and free-air anomaly using awk
#
    awk 'NR%100==0 {printf "%10.3f %10.3f %10.3f %10.3f\n",$2,$1,$6,$5*0.05}' $infile > dat
    awk '$2>=20.0 && $2<=45.0 && $1>=100.0 && $1<=160.0 {print}' dat > $tmpfile
    awk '{print $1,$2,$3,$4}' $insamplefile > dat2
    awk '{printf "%5.1f %5.1f %5.1f %5.1f\n", $1,$2,$3,$4*0.05 }' dat2 > $samplefile
#
    #gmt psxy $tmpfile -R$region -J$proj -Sv0.03/0.06/1.0 -Gblue -K -V > $psfile
    gmt psxy $tmpfile -R$region -J$proj -Sv$vector -Gblack -K -V > $psfile
    gmt pscoast -R$region -J$proj -Dh -Ggreen -Wthin,black -K -V -O >> $psfile
    gmt psbasemap -R$region -J$proj -B$frame -K -V -O >> $psfile
    gmt psxy $samplefile -R$region -J$proj -Sv0.03/0.06/1.0 -Gblue -O -V >> $psfile
    convert -density 300x300 $psfile $confile
done
#



