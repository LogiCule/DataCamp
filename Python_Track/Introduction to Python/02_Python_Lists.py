#Create_a_list

areas=list([hall,kit,liv,bed,bath])
print(areas)

#Create list with different types

areas = ['hallway',hall,'kitchen', kit, "living room", liv,'bedroom', bed, "bathroom", bath]
print(areas)

#List of lists

house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ['bedroom',bed],
         ['bathroom',bath]]
print(house)
print(type(house))

#Subset and calculate

eat_sleep_area=areas[3]+areas[-3]
print(eat_sleep_area)

#Slicing and dicing

downstairs=areas[:6]
upstairs=areas[6:]
print(downstairs)
print(upstairs)

#Replace list elements

areas[-1]+=1
areas[4]='chill zone'

#Extend a list

areas_1=areas+['poolhouse',24.5]
areas_2=areas_1+['garage',15.45]

