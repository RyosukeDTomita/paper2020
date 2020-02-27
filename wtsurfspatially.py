#wtsurf spatially
import os
import sys
import csv
import mkcsv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
#path = '/home/tomita/model/result/'
path = '/home/tomita/model/wtspatilaly/' 
count =int(0)
os.chdir(path)


wtp = np.zeros(24000)
file = os.path.join('wt')

if __name__=='__main__':
    mkcsv.conver(file)
cfile = os.path.join(path + 'cwt.csv')
data = pd.read_csv(cfile,header = None,\
usecols=[0,1,2,3],names=['time','i','j','wt'])
time = data.loc[:,'time'].values
i = data.loc[:,'i'].values.reshape(113,73)
j = data.loc[:,'j'].values.reshape(113,73)
i = 10*i
j = 10*j
wt = data.loc[:,'wt'].values.reshape(113,73)
wt = wt+300

t = np.arange(10,10001,10)
#plt.style.use('ggplot')
fig = plt.figure(figsize = (11.5,7.5))
ax = fig.add_subplot(111)
plt.pcolormesh(i,j,wt,cmap = 'rainbow',norm=Normalize(vmin=-100,vmax=20))
pp = plt.colorbar(orientation='vertical')
pp.set_label('wtsurf',fontname = 'Arial',fontsize = 24) 
ax.set_title('wtsurf')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()
plt.show()
#plt.savefig('wtsaptially')
