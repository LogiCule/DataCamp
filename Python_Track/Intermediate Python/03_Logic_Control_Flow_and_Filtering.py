#Equality

True==False
-5*15!=75
'pyscript'=='PyScript'
True==1

#Greater and less than

print(x>=-10)
print('test'<=y)
print(True>False)

#Compare arrays

print(my_house>=18)
print(my_house<your_house)

#and, or, not (1)

print(my_kitchen>10 and my_kitchen<18)
print(my_kitchen<14 or my_kitchen>17)
print(2*my_kitchen<3*your_kitchen)

#Boolean operators with Numpy

print(np.logical_or(my_house>18.5, my_house<10))
print(np.logical_and(my_house<11,your_house<11))

#skipped the if else part

#Driving right (1)

dr = cars['drives_right']
sel= cars[dr]
print(sel)

#Driving right (2)

sel = cars[cars['drives_right']]

#Cars per capita (1)

car_maniac = cars[cars['cars_per_cap']>500]
print(car_maniac)

#Cars per capita (2)

between = np.logical_and(cpc > 100,cpc < 500)
medium= cars[between]
print(medium)


