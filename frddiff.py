#program diffenrence ot d
import os 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
pi = math.pi
import csv
import sys
from matplotlib.colors import Normalize
#import matplotlib.font_manager as fon
#del fon.weight_dict['roman']
#matplotlib.font_manager._rebuild()
path = '/home/tomita/model/15nwtc/'
path2 = '/home/tomita/model/wtzonb/'
plt.rcParams['font.family'] = 'Times New Roman' # font family
plt.rcParams['mathtext.fontset'] = 'stix'

for i in range(14670,15030,30):
#for i in range(17910,18270,30):
    fig,ax = plt.subplots(figsize = (12,7))
#make CSV
    fname_in = 'BP222_0' + str(i).zfill(5) + '_00_00'
    fname_out = 'c{}.csv'.format(''.join(fname_in))
    #fname_in = os.path.join(path + fname_in)
    os.chdir(path)
    with open(fname_in, newline='') as fin,  \
           open(fname_out, mode='w', newline='') as fout:

        reader = csv.reader(fin, delimiter=' ', skipinitialspace=True)
        writer = csv.writer(fout)

        writer.writerows(reader)
#readfile
    file1 = os.path.join(path + 'cBP222_0' + str(i).zfill(5) + '_00_00.csv')
    data = pd.read_csv(file1,header = None,\
                       usecols=[2,5,6,7,8],names=['tb','p','uab','vab','d'])
    x = np.arange(1,1150.1,10)
    y = np.arange(1,750.1,10)
    X, Y = np.meshgrid(x,y)
    tb = data.loc[:,'tb']
    p = data.loc[:,'p']
    U = data.loc[:,'uab']
    V = data.loc[:,'vab']
    d = data.loc[:,'d']
#
    for t in range(0,8625,1):
        if tb[t] == 0.0:
            p[t] = np.nan
            U[t] = np.nan
            V[t] = np.nan
            d[t] = np.nan
            tb[t] = np.nan
    tb = tb.values.reshape(75,115)        
    p = p.values.reshape(75,115)
    U = U.values.reshape(75,115)
    V = V.values.reshape(75,115)
    d = d.values.reshape(75,115)
#read the others
#warning u havta convert txt to csv first.(Use frito.py)
    file2 = os.path.join(path2 + 'cBP222_0' + str(i).zfill(5) + '_00_00.csv')
    data2 = pd.read_csv(file2,header = None,\
                       usecols=[2,5,6,7,8],names=['tb','p','uab','vab','d'])
    tb2 = data2.loc[:,'tb']
    p2 = data2.loc[:,'p']
    U2 = data2.loc[:,'uab']
    V2 = data2.loc[:,'vab']
    d2 = data2.loc[:,'d']
#
    for t in range(0,8625,1):
        if tb2[t] == 0.0:
            p2[t] = np.nan
            U2[t] = np.nan
            V2[t] = np.nan
            d2[t] = np.nan
            tb2[t] = np.nan
    tb2 = tb2.values.reshape(75,115)        
    p2 = p2.values.reshape(75,115)
    U2 = U2.values.reshape(75,115)
    V2 = V2.values.reshape(75,115)
    d2 = d2.values.reshape(75,115)
    tb = tb2 - tb
    p = p2 - p 
    U = U2 -U 
    V = V2 - V 
    d = d2 - d 
    #gridimage
    plt.pcolormesh(X, Y, d, cmap = 'rainbow',\
    norm=Normalize(vmin=-25,vmax=25))
    pp3 = plt.colorbar(orientation='vertical')
    pp3.set_label(r"$d(m)$",fontname='Arial',fontsize=24)	
    #grdcontour
    cont3=plt.contour(X, Y, d, 10,vmin=-25,vmax=25,colors=['black'])
    cont3.clabel(fmt='%1.1f', fontsize=12)
    #label
    plt.xlabel(r"$x(km)$",fontsize=24)
    plt.ylabel(r"$y(km)$",fontsize=24)
    if (i/30)%12 ==0:
        title = r"$January$"
        tit = str(4).zfill(2) 
    elif(i/30)%12 ==1:
        title = r"$February$"
        tit = str(5).zfill(2) 
    elif (i/30)%12 ==2:
        title = r"$March$"
        tit = str(6).zfill(2)
    elif (i/30)%12 ==3:
        title = r"$April$"
        tit = str(7).zfill(2)
    elif (i/30)%12 ==4:
        title = r"$May$"
        tit = str(8).zfill(2)
    elif (i/30)%12 ==5:
        title = r"$June$"
        tit = str(9).zfill(2)
    elif (i/30)%12 ==6:
        title = r"$July$"
        tit = str(10).zfill(2)
    elif (i/30)%12 ==7:
        title = r"$August$"
        tit = str(11).zfill(2)
    elif (i/30)%12 ==8:
        title = r"$September$"
        tit = str(12).zfill(2)
    elif (i/30)%12 ==9:
        title = r"$Octover$"
        tit = str(1).zfill(2)
    elif (i/30)%12 ==10:
        title = r"$November$"
        tit = str(2).zfill(2)
    elif (i/30)%12 ==11:
        title = r"$December$"
        tit = str(3).zfill(2)
    ax.set_title(title,fontsize=24)
    #plt.show()
    figure = os.path.join(path2 + tit + 'ddiff')
    plt.savefig(figure)
