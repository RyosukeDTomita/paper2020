#!/bin/bash
#create japan map
#parameter setting
region=128/143/34/46
proj=M15
frame=f1g0a5
psfile=/home/tomita/model/coastbasemap2.ps
confile=/home/tomita/model/japan.png
#
gmt psbasemap -R$region -J$proj -B$frame -K -V > $psfile
gmt pscoast -R$region -J$proj -Di -Ggray -Wthin,black -O -V >> $psfile
convert -density 300x300 $psfile $confile
