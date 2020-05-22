#Loading a pickled file

import pickle
with open('data.pkl','rb') as file:
    d = pickle.load(file)
print(d)
print(type(d))

#Listing sheets in Excel files

import pandas as pd
file = 'battledeath.xlsx'
xls = pd.ExcelFile(file)
print(xls.sheet_names)

#Importing sheets from Excel files

df1 = xls.parse('2004')
print(df1.head())
df2 = xls.parse(0)
print(df2.head())

#Customizing your spreadsheet import

df1 = xls.parse(0, skiprows=1, names=['Country','AAM due to War (2002)'])
print(df1.head())
df2 = xls.parse(1, usecols=[0], skiprows=1, names=['Country'])
print(df2.head())

#Importing SAS files

from sas7bdat import SAS7BDAT
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas=file.to_data_frame()
print(df_sas.head())
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()

#Importing Stata files

df = pd.read_stata('disarea.dta')
print(df.head())

#Using h5py to import HDF5 files

import numpy as np
import h5py
file = 'LIGO_data.hdf5'
data = h5py.File(file, 'r')
print(type(data))
for key in data.keys():
    print(key)
    
#Extracting data from your HDF5 file

group = data['strain']
for key in group.keys():
    print(key)
strain = group['Strain'].value
num_samples = 10000
time = np.arange(0, 1, 1/num_samples)
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()

#Loading .mat files

import scipy.io
mat = scipy.io.loadmat('albeck_gene_expression.mat')
print(type(mat))

#The structure of .mat in Python

print(mat.keys())
print(type(mat['CYratioCyt']))
print(mat['CYratioCyt'].shape)

