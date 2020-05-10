#Motivation for dictionaries

ind_ger=countries.index('germany')
print(capitals[ind_ger])


#Create dictionary

europe = dict()
for i in range(len(countries)):
    europe[countries[i]]=capitals[i]
print(europe)

#Access dictionary

print(europe.keys())
print(europe['norway'])

#Dictionary Manipulation (1)

europe['italy']='rome'
print('italy' in europe)
europe['poland']='warsaw'
print(europe)

#Dictionary Manipulation (2)

europe['germany']='berlin'
del(europe['australia'])
print(europe)

#Dictionariception

print(europe['france']['capital'])
data={'capital':'rome','population':59.83}
europe['italy']=data
print(europe)

#Dictionary to DataFrame (1)

import pandas as pd
my_dict = {'country':names,'drives_right':dr,'cars_per_cap':cpc}
cars=pd.DataFrame(my_dict)
print(cars)

#Dictionary to DataFrame (2)

cars.index=row_labels
print(cars)

#CSV to DataFrame (1)

import pandas as pd
cars = pd.read_csv('cars.csv')
print(cars)

#Square Brackets (1)

print(cars['country'])
print(cars[['country']])
print(cars[['country','drives_right']])

#Square Brackets (2)

print(cars[:3])
print(cars[3:6])

#loc and iloc (1)

print(cars.loc['JPN'])
print(cars.loc[['AUS','EG']])

#loc and iloc (2)

print(cars.loc[['MOR'],['drives_right']])
print(cars.loc[['RU','MOR'],['country','drives_right']])

#loc and iloc (3)

print(cars['drives_right'])
print(cars[['drives_right']])
print(cars[['cars_per_cap','drives_right']])
