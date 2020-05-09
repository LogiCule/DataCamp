#Your First NumPy Array

import numpy as np
np_baseball = np.array(baseball)
print(type(np_baseball))

#Baseball players' height

np_height_in = np.array(height_in)
print(np_height_in)
np_height_m = np_height_in*0.0254
print(np_height_m)

#Baseball player's BMI

np_weight_kg = np.array(weight_lb)*0.453592
bmi=np_weight_kg/np_height_m**2
print(bmi)

#Lightweight baseball players

light=bmi<21
print(light)
print(bmi[light])

#Subsetting NumPy Arrays

print(np_weight_lb[50])
print(np_height_in[100:111])

#Your First 2D NumPy Array

np_baseball = np.array(baseball)
print(type(np_baseball))
print(np_baseball.shape)

#Baseball data in 2D form

np_baseball = np.array(baseball)
print(np_baseball.shape)

#Subsetting 2D NumPy Arrays

print(np_baseball[49])
np_weight_lb = np_baseball[:,1]
print(np_baseball[123,0])

#2D Arithmetic

print(np_baseball+updated)
conversion = np.array([0.0254,0.453592,1])
print(np_baseball*conversion)

#Average versus median

np_height_in = np.array(np_baseball[:,0])
print(np.mean(np_height_in))
print(np.median(np_height_in))

#Explore the baseball data

np_height_in = np.array(np_baseball[:,0])
print(np.mean(np_height_in))
print(np.median(np_height_in))

#Blend it all together

np_positions=np.array(positions)
np_heights=np.array(heights)
gk_heights=np_heights[np_positions=='GK']
other_heights=np_heights[np_positions!='GK']
print("Median height of goalkeepers: " + str(np.median(gk_heights)))
print("Median height of other players: " + str(np.median(other_heights)))


