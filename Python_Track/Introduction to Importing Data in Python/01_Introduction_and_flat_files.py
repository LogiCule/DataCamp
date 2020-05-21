#Importing entire text files

file = open('moby_dick.txt', 'r')
print(file.read())
print(file.closed)
file.close()
print(file.closed)

#Importing text files line by line

with open('moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    
#Using NumPy to import flat files

import numpy as np
file = 'digits.csv'
digits = np.loadtxt(file, delimiter=',')
print(type(digits))
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

#Customizing your NumPy import

import numpy as np
file = 'digits_header.txt'
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0,2])
print(data)

#Importing different datatypes

file = 'seaslug.txt'
data = np.loadtxt(file, delimiter='\t', dtype=str)
print(data[0])
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)
print(data_float[9])
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()

#Working with mixed datatypes (2)

file = 'titanic.csv'
d = np.recfromcsv(file)
print(d[:3])

#Using pandas to import flat files as DataFrames (1)

file = 'titanic.csv'
df = pd.read_csv(file)
print(df.head())

#Using pandas to import flat files as DataFrames (2)

data=pd.read_csv(file,nrows=5,header=None)
data_array=np.array(data)

#Customizing your pandas import

data = pd.read_csv(file, sep='\t', comment='#', na_values='Nothing')

