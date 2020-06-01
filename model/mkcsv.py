import sys
import csv

def conver(self):
    fname_in = self
    fname_out = 'c{}.csv'.format(''.join(fname_in))

    with open(fname_in, newline='') as fin, \
        open(fname_out, mode='w', newline='') as fout:

        reader = csv.reader(fin, delimiter=' ', skipinitialspace=True)
        writer = csv.writer(fout)

        writer.writerows(reader)
   
