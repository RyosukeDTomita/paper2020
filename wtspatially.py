#wtsurf spatially
import os
import sys
import csv
import mkcsv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
path = '/home3/tomita/model//'
#path = '/home/tomita/model/result/' 
count =int(0)
os.chdir(path)
file = os.path.join('wt')

if __name__=='__main__':
    mkcsv.conver(file)
cfile = os.path.join(path + 'cwt.csv')
data = pd.read_csv(cfile,header = None,\
usecols=[0,1,2,3],names=['time','i','j','wt'])
i = data.loc[:,'i'].values
j = data.loc[:,'j'].values
i = 10*i.reshape(115,75)
j = 10*j.reshape(115,75)
wt = data.loc[:,'wt'].values.reshape(115,75)
#wt = wt+300

#plt.style.use('ggplot')
fig = plt.figure(figsize = (11.5,7.5))
ax = fig.add_subplot(111)
plt.pcolormesh(i,j,wt,cmap = 'rainbow',norm=Normalize(vmin=-400,vmax=0))
pp = plt.colorbar(orientation='vertical')
#pp.set_label('wtsurf',fontname = 'Arial',fontsize = 24) 
#ax.set_title('wtsurf')
ax.set_ylim =(0,750)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()
#plt.show()
plt.savefig('wtsaptially2')
