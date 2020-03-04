#!bin/bash
#parameter setting
for AA in {1..12}; do
    BB=`printf %02d ${AA}`
    region=/0/115/0/75
    proj=M15
    frame=f10a10g10
    psfile=/home3/tomita/tomitasoturon2020/JRA55/fit/$(BB)fit.ps
    infile=/home3/tomita/tomitasoturon2020/JRA55/fit/$(BB)fit.dat
    tmp=/home3/tomita/tomitasoturon2020/JRA55/fit/tmpfile
    insamplefile=/home3/tomita/soturon2020/JRA55/fit/sample.dat
    samplefile=/home3/tomita/tomitasoturon2020/JRA55/fit/outsample.dat
    confile=/home3/tomita/tomitasoturon2020/JRA55/fit/$(BB)fit.png
    #
    #extract record number and free-air anomaly using awk↲
    #
    awk 'NR%25==0 {printf "%10.3f %10.3f %10.3f %10.3f\n",  $2,$1,$6,$5*0.00025' $infile > $tmp↲
    awk '{print $1,$2,$3,$4}' $insamplefile > dat1↲
    awk '{printf "%5.1f %5.1f %5.1f %5.1f\n", $1,$2,$3,$4*0.05 }' dat1 > $samplefile↲

    gmt psxy $tmp -R$region -J$proj -Sv0.03/0.06/1.0 -Gblue -K -V > $psfile↲
    gmt pscoast -R$region -J$proj -Dh -Ggray -Wthin,black -K -V -O >> $psfile↲
    gmt psbasemap -R$region -J$proj -B$frame -K -V -O >> $psfile↲
    gmt psxy $samplefile -R$region -J$proj -Sv0.03/0.06/1.0 -Gblue -O -V >> $psfile↲
    convert -density 300x300 $psfile $confile↲
done
