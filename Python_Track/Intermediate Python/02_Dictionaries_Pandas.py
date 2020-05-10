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

