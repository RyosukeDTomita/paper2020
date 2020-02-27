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
path = '/home/tomita/model/wtpeak6to7/'
#create matrix
#It makes matrixs which can convert topography area's data '0'
example = '/home/tomita/model/def0109/cBP222_022290_00_00.csv'
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
        #print(i)
        
        file = os.path.join('BP222_0' + str(i).zfill(5) + '_00_00')

        if __name__=='__main__':
            mkcsv.conver(file)
        cfile = os.path.join(path + 'cBP222_0' + str(i).zfill(5) + '_00_00.csv')
        data = pd.read_csv(cfile,header = None,\
        usecols=[0,1,2,4,5,6,7,8],names=\
                           ['i','j','tb','elb','p','uab','vab','d'])
        d = data.loc[:,'d']
        #elb = data.loc[:,'elb']
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
        #i = i.values.reshape(75,115)
        #j = j.values.reshape(75,115)
        #print(i[[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],1])
        #print(j[[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],1])
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
fig = plt.figure(figsize = (8,5))
#plt.rcParams['font.family'] = 'Times New Roman' # font familyの設定
#plt.rcParams['mathtext.fontset'] = 'stix' # math fontの設定
#plt.rcParams["font.size"] =15 # 全体のフォントサイズが変更されます。
#plt.rcParams['xtick.labelsize'] = 9 # 軸だけ変更されます。
#plt.rcParams['ytick.labelsize'] = 24 # 軸だけ変更されます
#plt.rcParams['xtick.direction'] = 'in' # x軸の向きを内側に設定（ggplotだと変化しない） 
#plt.rcParams['ytick.direction'] = 'in'
#plt.rcParams['axes.linewidth'] = 0.5 # 軸の太さ
#plt.rcParams['axes.grid'] = True # グリット線の設定
#plt.rcParams["legend.borderaxespad"] = 0. #凡例の箱をの位置をグラフに合わせて左に寄せる
#plt.rcParams["legend.fancybox"] = False # 丸角
#plt.rcParams["legend.framealpha"] = 1 # 透明度の指定、0で塗りつぶしなし
#plt.rcParams["legend.edgecolor"] = 'gray' # edgeの色を変更
#plt.rcParams["legend.handlelength"] = 1 # 凡例の線の長さを調節
#plt.rcParams["legend.handletextpad"] = 2. # 凡例の線と凡例のアイコンの距離
#plt.rcParams["legend.markerscale"] = 1 # 凡例の点がある場合のmarker scale
ax = fig.add_subplot(111)
ax.plot(data,marker='.', markersize=10, markeredgewidth=1., markeredgecolor='k', label = 'Sv',color = 'b')
#ax.set_title(r"$Sv$")
ax.set_xlabel(r"$day$")
ax.set_ylabel(r"$Sv$")
ax.set_xticks(np.linspace(10,24000,240),minor=True)###
ax.set_yticks(np.linspace(0,2.5,25),minor=True)
ax.set_xlim(3600,7200)
ax.legend()
figure = os.path.join(path + 'testSv')
plt.savefig(figure)
#plt.subplots_adjust(bottom=0.2) # 下余白調整(default=0.1)
#
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
#
t = np.arange(10,24001,10) ###
data = pd.Series(zp,t)
#plt.style.use('ggplot')
fig = plt.figure(figsize = (8,5))
ax = fig.add_subplot(111)
ax.plot(data,label = 'z',color = 'b')
ax.set_title('z')
ax.set_xlabel('day')
ax.set_ylabel('z')
ax.set_xticks(np.linspace(10,24001,240),minor=True)###
#ax.set_yticks(np.linspace(0,2.5,25),minor=True)
ax.set_xlim(10,24000)
ax.legend()
figure = os.path.join(path + 'testz')
plt.savefig(figure)
ax.set_xlim(10800,18000)
figure2 = os.path.join(figure + 'big')
plt.savefig(figure2)
#
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
#tb
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
#tb2
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
