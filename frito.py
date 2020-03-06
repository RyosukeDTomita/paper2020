#program frito.py
#-------module-------
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
#-------path setting-------
path1= '/home3/tomita/tomitasoturon2020/model/'
print('Type the directory name')
path = os.path.join(path1 + input()+'/')#stdin
plt.rcParams['font.family'] = 'Times New Roman' # font family
plt.rcParams['mathtext.fontset'] = 'stix'
for i in range(14400,15120,30):
#convert to CSV
    fname_in = 'BP222_0' + str(i).zfill(5) + '_00_00'
    fname_out = 'c{}.csv'.format(''.join(fname_in))
    os.chdir(path)
    with open(fname_in, newline='') as fin,  \
           open(fname_out, mode='w', newline='') as fout:

        reader = csv.reader(fin, delimiter=' ', skipinitialspace=True)
        writer = csv.writer(fout)

        writer.writerows(reader)
#-------read file-------
    fig,ax = plt.subplots(figsize = (12,7))
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
    #gridimage
    plt.pcolormesh(X, Y, p, cmap = 'rainbow',\
                   norm=Normalize(vmin=500,vmax=1500))
    pp = plt.colorbar(orientation='vertical')
    pp.set_label(r"$Pressure$",fontsize=24)
    #grdcontour
    cont=plt.contour(X, Y, p, 8,vmin=150,vmax=200,colors=['black'])
    cont.clabel(fmt='%1.1f', fontsize=12)
    for c in range(1,116,1):
        if c % 5 != 0:
            U[:,c] = np.nan    
            V[:,c] = np.nan
    for a in range(1,76,1):
        if a % 5 != 0:
            U[a] = np.nan
            V[a] = np.nan
    #ax.quiver(X,Y,U,V,angles='uv',scale_units='xy',scale=0.01)
    X2 = np.append(X,1170)
    Y2 = np.append(Y,0)
    U2 = np.append(U,0.05)
    V2 = np.append(V,0.0)
    ax.quiver(X2,Y2,U2,V2,angles='uv',scale_units='xy',scale=0.001)
    #label
    
    plt.xlabel(r"$x(km)$",fontsize=24)
    plt.ylabel(r"$y(km)$",fontsize=24)
    if (i/30)%12 ==0:
        title = r"$January$"
    elif(i/30)%12 ==1:
        title = r"$February$"
    elif (i/30)%12 ==2:
        title = r"$March$"
    elif (i/30)%12 ==3:
        title = r"$April$"
    elif (i/30)%12 ==4:
        title = r"$May$"
    elif (i/30)%12 ==5:
        title = r"$June$"
    elif (i/30)%12 ==6:
        title = r"$July$"
    elif (i/30)%12 ==7:
        title = r"$August$"
    elif (i/30)%12 ==8:
        title = r"$September$"
    elif (i/30)%12 ==9:
        title = r"$Octover$"
    elif (i/30)%12 ==10:
        title = r"$November$"
    elif (i/30)%12 ==11:
        title = r"$December$"
    ax.set_title(title,fontsize=24)
    #plt.show()
    figure = os.path.join(path + str(i) + 'v')
    plt.savefig(figure)

    #frito2
    fig,ax = plt.subplots(figsize = (12,7))
    plt.pcolormesh(X, Y, tb, cmap = 'rainbow',norm=Normalize(vmin=10,vmax=26))
    pp2 = plt.colorbar(orientation='vertical')
    pp2.set_label(r"$SST$",fontname='Arial',fontsize=24)	
    #grdcontour
    cont2=plt.contour(X, Y, tb, 10,vmin=150,vmax=200,colors=['black'])
    cont2.clabel(fmt='%1.1f', fontsize=12)
    #label
    plt.xlabel(r"$x(km)$",fontsize=24)
    plt.ylabel(r"$y(km)$",fontsize=24)
    if (i/30)%12 ==0:
        title = r"$January$"
    elif(i/30)%12 ==1:
        title = r"$February$"
    elif (i/30)%12 ==2:
        title = r"$March$"
    elif (i/30)%12 ==3:
        title = r"$April$"
    elif (i/30)%12 ==4:
        title = r"$May$"
    elif (i/30)%12 ==5:
        title = r"$June$"
    elif (i/30)%12 ==6:
        title = r"$July$"
    elif (i/30)%12 ==7:
        title = r"$August$"
    elif (i/30)%12 ==8:
        title = r"$September$"
    elif (i/30)%12 ==9:
        title = r"$Octover$"
    elif (i/30)%12 ==10:
        title = r"$November$"
    elif (i/30)%12 ==11:
        title = r"$December$"
    ax.set_title(title,fontsize=24)
    #plt.show()
    figure = os.path.join(path + str(i) + 'sst')
    plt.savefig(figure)

    #frito3
    fig,ax = plt.subplots(figsize = (12,7))
    plt.pcolormesh(X, Y, d, cmap = 'rainbow',norm=Normalize(vmin=100,vmax=300))
    pp3 = plt.colorbar(orientation='vertical')
    pp3.set_label(r"$d$",fontname='Arial',fontsize=24)	
    #grdcontour
    cont3=plt.contour(X, Y, d, 10,vmin=150,vmax=200,colors=['black'])
    cont3.clabel(fmt='%1.1f', fontsize=12)
    #label
    plt.xlabel(r"$x(km)$",fontsize=24)
    plt.ylabel(r"$y(km)$",fontsize=24)
    if (i/30)%12 ==0:
        title = r"$January$"
    elif(i/30)%12 ==1:
        title = r"$February$"
    elif (i/30)%12 ==2:
        title = r"$March$"
    elif (i/30)%12 ==3:
        title = r"$April$"
    elif (i/30)%12 ==4:
        title = r"$May$"
    elif (i/30)%12 ==5:
        title = r"$June$"
    elif (i/30)%12 ==6:
        title = r"$July$"
    elif (i/30)%12 ==7:
        title = r"$August$"
    elif (i/30)%12 ==8:
        title = r"$September$"
    elif (i/30)%12 ==9:
        title = r"$Octover$"
    elif (i/30)%12 ==10:
        title = r"$November$"
    elif (i/30)%12 ==11:
        title = r"$December$"
    ax.set_title(title,fontsize=24)
    #plt.show()
    figure = os.path.join(path + str(i) + 'el')
    plt.savefig(figure)
    
    #frbig
    fig,ax = plt.subplots(figsize = (7,7))
    file = os.path.join(path + 'cBP222_0' + str(i).zfill(5) + '_00_00.csv')
    data = pd.read_csv(file,header = None,\
                       usecols=[2,5,6,7],names=['tb','p','uab','vab'])
    x = np.arange(1,1150.1,10)
    y = np.arange(1,750.1,10)
    X, Y = np.meshgrid(x,y)
    #p = data.loc[:,'p'].values.reshape(75,115)
    #U = data.loc[:,'uab'].values.reshape(75,115)
    #V = data.loc[:,'vab'].values.reshape(75,115)
    tb = data.loc[:,'tb']
    p = data.loc[:,'p']
    U = data.loc[:,'uab']
    V = data.loc[:,'vab']
    
            #
    for t in range(0,8625,1):
        if tb[t] == 0.0:
            p[t] = np.nan
            U[t] = np.nan
            V[t] = np.nan
    tb = tb.values.reshape(75,115)        
    p = p.values.reshape(75,115)
    U = U.values.reshape(75,115)
    V = V.values.reshape(75,115)
    #gridimage
    plt.pcolormesh(X, Y, p, cmap = 'rainbow',\
                   norm=Normalize(vmin=0,vmax=3000))
    pp = plt.colorbar(orientation='vertical')
    pp.set_label(r"$Pressure$",fontsize=24)
    #grdcontour
    cont=plt.contour(X, Y, p, 8,vmin=150,vmax=200,colors=['black'])
    cont.clabel(fmt='%1.1f', fontsize=12)
    for c in range(1,116,1):
        if c % 5 != 0:
            U[:,c] = np.nan    
            V[:,c] = np.nan
    for a in range(1,76,1):
        if a % 5 != 0:
            U[a] = np.nan
            V[a] = np.nan
    #ax.quiver(X,Y,U,V,angles='uv',scale_units='xy',scale=0.01)
    X2 = np.append(X,1170)
    Y2 = np.append(Y,0)
    U2 = np.append(U,0.05)
    V2 = np.append(V,0.0)
    ax.quiver(X2,Y2,U2,V2,angles='uv',scale_units='xy',scale=0.001)
    #label
    
    plt.xlabel(r"$x$",fontsize=24)
    plt.ylabel(r"$y$",fontsize=24)
    if (i/30)%12 ==0:
        title = r"$January$"
    elif(i/30)%12 ==1:
        title = r"$February$"
    elif (i/30)%12 ==2:
        title = r"$March$"
    elif (i/30)%12 ==3:
        title = r"$April$"
    elif (i/30)%12 ==4:
        title = r"$May$"
    elif (i/30)%12 ==5:
        title = r"$June$"
    elif (i/30)%12 ==6:
        title = r"$July$"
    elif (i/30)%12 ==7:
        title = r"$August$"
    elif (i/30)%12 ==8:
        title = r"$September$"
    elif (i/30)%12 ==9:
        title = r"$Octover$"
    elif (i/30)%12 ==10:
        title = r"$November$"
    elif (i/30)%12 ==11:
        title = r"$December$"
    ax.set_title(title,fontsize=24)
    ax.set_xlim(0,500)
    ax.set_ylim(0,500)
    #plt.show()
    figure = os.path.join(path + str(i) + 'vbig')
    plt.savefig(figure)
