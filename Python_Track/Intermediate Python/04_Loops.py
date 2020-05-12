#Basic while loop

offset = 8
while offset>0:
    offset-=1
    print("correcting...")
    print(offset)
    
#Add conditionals

while offset != 0 :
    print("correcting...")
    if offset>0 :
        offset-=1
    else : 
        offset+=1
    print(offset)
#Loop over a list

for i in areas:
    print(i)
#Indexes and values (1)

for i,a in enumerate(areas) :
    print("room "+str(i)+": "+str(a))
    
#Loop over list of lists

for i in house:
    print("the "+i[0]+" is "+str(i[1])+" sqm")

#Loop over dictionary

for i,j in europe.items():
    print("the capital of "+i+" is "+j)
    
#Loop over Numpy array

for i in np.nditer(np_height):
    print(str(i)+" inches")
for i in np.nditer(np_baseball):
    print(i)

#Loop over DataFrame (1)

for i,j in cars.iterrows():
    print(i)
    print(j)

#Loop over DataFrame (2)

for lab, row in cars.iterrows() :
    print(lab+": "+str(cars.loc[lab,'cars_per_cap']))
    
#Add column (1)

for i,j in cars.iterrows():
    cars.loc[i,"COUNTRY"]=j["country"].upper()

#Add column (2)

cars["COUNTRY"] = cars["country"].apply(str.upper)
