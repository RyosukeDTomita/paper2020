#pomtest
#import module
import os
import sys
import csv
import mkcsv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fon
path = '/home3/tomita/tomitasoturon2020/model/soturonwtave/'
#create matrix
#It makes matrixs which can convert topography area's data '0'
example = '/home3/tomita/tomitasoturon2020/model\
/example/cBP222_022900_00_00.csv'
ff = pd.read_csv(example,header = None,usecols = [2],names = ['tb'])
tb = ff.loc[:,'tb']
tb = tb.values.reshape(75,115)
zerof = tb.copy()
for a in range(0,115,1):
    for b in range(0,75,1):
        if zerof[b,a] != 0.0:
            zerof[b,a] = 1.0
#print(zerof)
##############################################################################
#**************************read data and Calculate*************************
count =int(0)
os.chdir(path)
with open('energ.csv','w') as f:
    svp = np.zeros(2400)###
    enegyp = np.zeros(2400)###
    zp = np.zeros(2400)###
    dp = np.zeros(2400)###
    tbp = np.zeros(2400)###
    tbp2 = np.zeros(2400)
    for i in range (10,24001,10):###
        
        file = os.path.join('BP222_0' + str(i).zfill(5) + '_00_00')

        if __name__=='__main__':
            mkcsv.conver(file)
        cfile = os.path.join(path + 'cBP222_0' + str(i).zfill(5) + '_00_00.csv')
        data = pd.read_csv(cfile,header = None,\
        usecols=[0,1,2,4,5,6,7,8],names=\
                           ['i','j','tb','elb','p','uab','vab','d'])
        d = data.loc[:,'d']
        tb = data.loc[:,'tb']
        p = data.loc[:,'p']
        U = data.loc[:,'uab']
        V = data.loc[:,'vab']
        i = data.loc[:,'i']
        j = data.loc[:,'j']
        U = U.values.reshape(75,115)
        V = V.values.reshape(75,115)
        d = d.values.reshape(75,115)
        tb = tb.values.reshape(75,115)
        U = U *zerof 
        V = V * zerof
        d = d *zerof 
        tb = tb * zerof
        z = (U**2 + V**2)**0.5
        z1 = z[[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],1]#cut not important
        d1 = d[[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],1]
        tb2 = tb[[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],1]
        sv = 0.01 * d1 *z1
        enegy = 1000* 10000 * 0.5 * 10000 * d * z**2
        sumenegy = enegy.sum(axis=None)/8625
        sumsvw = sv.sum(axis =0)
        sumtb = np.mean(tb2,axis = 0)
        tbp2[count] = sumtb
        svp[count] = sumsvw
        enegyp[count] = sumenegy
        #zp[count] = np.mean(z1,axis = 0)
        z = z.reshape(75*115,1)##
        d = d.reshape(75*115,1)
        tb = tb.reshape(75*115,1)
        ##
        tbp[count] = np.sum(tb,axis = 0)/(8625-528)
        zp[count] = np.mean(z,axis = 0)
        dp[count] = np.mean(d,axis = 0)
        count = count + int(1)
#
t = np.arange(10,24001,10) ###
data = pd.Series(svp,t)
#plt.style.use('ggplot')

#**************************Create graph************************************
#Sv
fig = plt.figure(figsize = (8,5))
ax = fig.add_subplot(111)
ax.plot(data,marker='.', markersize=10, markeredgewidth=1., markeredgecolor='k', label = 'Sv',color = 'b')
ax.set_xlabel(r"$day$")
ax.set_ylabel(r"$Sv$")
ax.set_xticks(np.linspace(10,24000,240),minor=True)###
ax.set_yticks(np.linspace(0,2.5,25),minor=True)
ax.set_xlim(3600,7200)
ax.legend()
figure = os.path.join(path + 'testSv')
plt.savefig(figure)
#************************************************

#energy
data = pd.Series(enegyp,t)
fig = plt.figure(figsize = (8,5))
ax = fig.add_subplot(111)
ax.plot(data,label = 'enegy',color = 'b')
ax.set_title(r"$enegy$")
ax.set_xlabel(r"$day$")
ax.set_ylabel(r"$enegy$")
ax.set_xticks(np.linspace(0,24000,240),minor=True)###
ax.set_yticks(np.linspace(0,2.5,25),minor=True)
ax.set_xlim(10,24001)
ax.legend()
figure = os.path.join(path + 'testenegy')
plt.savefig(figure)
ax.set_xlim(3600,7200)
figure2 = os.path.join(figure + 'big')
plt.savefig(figure2)
#**********************************************

#velocity average
t = np.arange(10,24001,10) ###
data = pd.Series(zp,t)
fig = plt.figure(figsize = (8,5))
ax = fig.add_subplot(111)
ax.plot(data,label = 'z',color = 'b')
ax.set_title('z')
ax.set_xlabel('day')
ax.set_ylabel('z')
ax.set_xticks(np.linspace(10,24001,240),minor=True)###
ax.set_xlim(10,24000)
ax.legend()
figure = os.path.join(path + 'testz')
plt.savefig(figure)
ax.set_xlim(10800,18000)
figure2 = os.path.join(figure + 'big')
plt.savefig(figure2)
#****************************************

# 1layer depth
t = np.arange(10,24001,10) ###
data = pd.Series(dp,t)
#plt.style.use('ggplot')
fig = plt.figure(figsize = (8,5))
ax = fig.add_subplot(111)
ax.plot(data,label = 'd',color = 'b')
ax.set_title('d')
ax.set_xlabel('day')
ax.set_ylabel('d')
ax.set_xticks(np.linspace(10,24000,240),minor=True)#
#ax.set_yticks(np.linspace(0,2.5,25),minor=True)
ax.set_xlim(10,24000)
ax.legend()
figure = os.path.join(path + 'testd')
plt.savefig(figure)
ax.set_xlim(3600,7200)
figure2 = os.path.join(figure + 'big')
plt.savefig(figure2)
#***********************************************

#sea surface temparature average
data = pd.Series(tbp,t)
fig = plt.figure(figsize = (8,5))
ax = fig.add_subplot(111)
ax.plot(data,label = 'tb',color = 'b')
ax.set_title(r"$tb$")
ax.set_xlabel(r"$day$")
ax.set_ylabel(r"$tb$")
ax.set_xticks(np.linspace(0,24000,240),minor=True)###
ax.set_yticks(np.linspace(0,2.5,25),minor=True)
ax.set_xlim(10,24001)
ax.legend()
figure = os.path.join(path + 'testtb')
plt.savefig(figure)
ax.set_xlim(3600,7200)
figure2 = os.path.join(figure + 'big')
plt.savefig(figure2)
#***************************************************

#sea surface temperature (Tsushima Strait)
data = pd.Series(tbp2,t)
fig = plt.figure(figsize = (8,5))
ax = fig.add_subplot(111)
ax.plot(data,label = 'tb',color = 'b')
ax.set_title(r"$tb2$")
ax.set_xlabel(r"$day$")
ax.set_ylabel(r"$tb2$")
ax.set_xticks(np.linspace(0,24000,240),minor=True)###
ax.set_yticks(np.linspace(0,2.5,25),minor=True)
ax.set_xlim(10,24001)
ax.legend()
figure = os.path.join(path + 'testtb2')
plt.savefig(figure)
ax.set_xlim(3600,7200)
figure2 = os.path.join(figure + 'big')
plt.savefig(figure2)
#plt.show()
