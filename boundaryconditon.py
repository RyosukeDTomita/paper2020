import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fon #font setting
import math
pi = math.pi
#del fon.weight_dict['roman']
#matplotlib.font_manager._rebuild()
#sv
N = 10 ##
x = np.arange(1,13.1,1) ##
#y1 = [2.01,2.28,2.52,2.60,2.66,2.70,2.68,3.05,2.93,3.10,2.84,2.36]
y1 = np.array([1.01,1.02,1.12,1.30,1.39,1.42,1.48,1.72,1.78,1.92,1.71,1.32,1.01]) ##
y2 = np.array([1.00,1.26,1.40,1.30,1.28,1.28,1.20,1.33,1.15,1.18,1.13,1.04,1.00]) ##
y1 = y1 + y2 
sin = np.sin(2*np.pi*x/12)
sin2 = sin**2
sinsum = sin.sum(axis=0)
y1sum = y1.sum(axis=0)
y1x = y1*sin

WA = (y1x.sum(axis=0)-(y1sum/12)*sinsum)/sin2.sum(axis=0)-sinsum*sinsum/12
WB = (y1sum - WA*sinsum)/12
print(WA,WB) 

#plot
#plt.style.use('ggplot')
fig = plt.figure(figsize = (8,5)) ##
ax = fig.add_subplot(111)
plt.rcParams['font.family'] = 'Times New Roman' # font familyの設定
plt.rcParams['mathtext.fontset'] = 'stix' # math fontの設定
plt.rcParams["font.size"] =15 # 全体のフォントサイズが変更されます。
plt.rcParams['xtick.labelsize'] = 9 # 軸だけ変更されます。
plt.rcParams['ytick.labelsize'] = 24 # 軸だけ変更されます
plt.rcParams['xtick.direction'] = 'in' # x軸の向きを内側に設定（ggplotだと変化しない） 
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['axes.linewidth'] = 0.5 # 軸の太さ
plt.rcParams['axes.grid'] = True # グリット線の設定
plt.rcParams["legend.borderaxespad"] = 0. #凡例の箱をの位置をグラフに合わせて左に寄せる
plt.rcParams["legend.fancybox"] = False # 丸角
plt.rcParams["legend.framealpha"] = 1 # 透明度の指定、0で塗りつぶしなし
plt.rcParams["legend.edgecolor"] = 'gray' # edgeの色を変更
plt.rcParams["legend.handlelength"] = 1 # 凡例の線の長さを調節
plt.rcParams["legend.handletextpad"] = 2. # 凡例の線と凡例のアイコンの距離
plt.rcParams["legend.markerscale"] = 1 # 凡例の点がある場合のmarker scale
#
ax.plot(x, y1,marker='.', markersize=10, markeredgewidth=1., markeredgecolor='k', label='TotalTWC',color='b') ##
#ax.plot(x,WA*sin + WB ,marker='.', markersize=10, markeredgewidth=1., markeredgecolor='k', label='CWfit',color='g',linestyle="dashdot")
ax.set_xticks(np.linspace(0, 12, 13),minor=True) ## #目盛りの設定
ax.set_xlim(1, 12.9) ##
ax.set_yticks(np.linspace(0.0, 4.0, 41),minor=True) ##
ax.set_ylim(0,3.5) ##

ax.set_xlabel(r"$Month$") ## #斜体
ax.set_ylabel(r"$Volume transport(Sv)$") ## 
ax.set_xticks(np.linspace(1, 12,12)) ## #グリット線の間隔
ax.legend(ncol=2, bbox_to_anchor=(0., 1.02, 1., 0.102), loc=3) #ncolで同じ行に置く凡例の数　(内は左からx,yの位置,横x縦の箱)
#plt.show()
plt.savefig('sv2')
###############################################################################

#Setting for graph
fig = plt.figure(figsize = (11,7)) ##
ax = fig.add_subplot(111)
plt.rcParams['font.family'] = 'Times New Roman' # font familyの設定
plt.rcParams['mathtext.fontset'] = 'stix' # math fontの設定
plt.rcParams["font.size"] =15 # 全体のフォントサイズが変更されます。
plt.rcParams['xtick.labelsize'] = 20 # 軸だけ変更されます。
plt.rcParams['ytick.labelsize'] = 20 # 軸だけ変更されます
plt.rcParams['xtick.direction'] = 'in' # x軸の向きを内側に設定（ggplotだと変化しない）
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['axes.linewidth'] = 0.5 # 軸の太さ
plt.rcParams['axes.grid'] = True # グリット線の設定
plt.rcParams["legend.borderaxespad"] = 0. #凡例の箱をの位置をグラフに合わせて左に寄せる
plt.rcParams["legend.fancybox"] = False # 丸角
plt.rcParams["legend.framealpha"] = 1 # 透明度の指定、0で塗りつぶしなし
plt.rcParams["legend.edgecolor"] = 'gray' # edgeの色を変更
plt.rcParams["legend.handlelength"] = 1 # 凡例の線の長さを調節
plt.rcParams["legend.handletextpad"] = 2. # 凡例の線と凡例のアイコンの距離
plt.rcParams["legend.markerscale"] = 1 # 凡例の点がある場合のmarker scale

#create continuous data
t = np.arange(1,13,0.1)
y1 = -100 + 200 *np.sin((2*pi*t/12) - pi/2)
y11 = -100 + 300 *np.sin((2*pi*t/12) - pi/2)
a = t<=3#条件を満たすとTrue,満たさないとFalseを返す
a2 = t>=9
a = a.astype(np.int) + a2.astype(np.int)
y111 = y11 * a.astype(np.int)#True=1,Faule=0を返す
b = (3.0 < t) & (t < 9.0)
y1111 = y1 * b.astype(np.int)
y2 = y111 + y1111
data1 = pd.Series(y1,t)
data2 = pd.Series(y2,t)
#data3 = pd.Series(y3,t)
ax.plot(data2,label='-100 + 300sin(2πt/12-π/2)',color = 'b')
ax.plot(data1,label='-100 + 200sin(2πt/12-π/2)',color = 'r', linestyle="dashdot")
#ax.plot(data3,label='14+3.5sin(2πt/12-π)',color = 'b')

#label
ax.set_title(r'$Net heat flux$',fontsize=20)
ax.set_xlabel(r'$Month$',fontsize=20)
ax.set_ylabel(r'$Wm^-2$',fontsize=20)
ax.set_xticks(np.linspace(1, 12, 12),minor=True) ## #目盛りの設定
ax.set_yticks(np.linspace(-400,100,50),minor=True) ####
ax.set_xlim(1,12.9)
ax.legend(fontsize=15)
#plt.show()
#print(os.getcwd())
plt.savefig('wtsurf2')
###############################################################################

#Setting for graph
fig = plt.figure(figsize = (8,5)) ##
ax = fig.add_subplot(111)
plt.rcParams['font.family'] = 'Times New Roman' # font familyの設定
plt.rcParams['mathtext.fontset'] = 'stix' # math fontの設定
plt.rcParams["font.size"] =15 # 全体のフォントサイズが変更されます。
plt.rcParams['xtick.labelsize'] = 20# 軸だけ変更されます。
plt.rcParams['ytick.labelsize'] = 20 # 軸だけ変更されます
plt.rcParams['xtick.direction'] = 'in' # x軸の向きを内側に設定（ggplotだと変化しない）
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['axes.linewidth'] = 0.5 # 軸の太さ
plt.rcParams['axes.grid'] = True # グリット線の設定
plt.rcParams["legend.borderaxespad"] = 0. #凡例の箱をの位置をグラフに合わせて左に寄せる
plt.rcParams["legend.fancybox"] = False # 丸角
plt.rcParams["legend.framealpha"] = 1 # 透明度の指定、0で塗りつぶしなし
plt.rcParams["legend.edgecolor"] = 'gray' # edgeの色を変更
plt.rcParams["legend.handlelength"] = 1 # 凡例の線の長さを調節
plt.rcParams["legend.handletextpad"] = 2. # 凡例の線と凡例のアイコンの距離
plt.rcParams["legend.markerscale"] = 1 # 凡例の点がある場合のmarker scale

#create continuous data
t = np.arange(1,13.0,0.1)
y1 = 16 + 3.0*np.sin((2*pi*t/12) - pi)
data1 = pd.Series(y1,t)
ax.plot(data1,label='16+3.0sin(2πt/12-π)',color = 'g')


#label
ax.set_title(r'$TBTWC temparature$',fontsize=20)
ax.set_xlabel(r'$Month$',fontsize=20)
ax.set_ylabel('℃',fontsize=20)
ax.set_xticks(np.linspace(1, 12, 12),minor=True) ## #目盛りの設定
ax.set_yticks(np.linspace(12,20,9),minor=True) ####
ax.set_xlim(1,12.9)
ax.legend(fontsize=15)
#plt.show()
#print(os.getcwd())
plt.savefig('TBTWCtempareture')
