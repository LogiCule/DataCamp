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

