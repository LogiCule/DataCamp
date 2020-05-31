#Numeric data or ... ?

print(ride_sharing.info())
print(ride_sharing['user_type'].describe())

print(ride_sharing.info())
print(ride_sharing['user_type'].describe())
ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype('category')
assert ride_sharing['user_type_cat'].dtype == 'category'
print(ride_sharing['user_type_cat'].describe())

#Summing strings and concatenating numbers

ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip("minutes")
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')
assert ride_sharing['duration_time'].dtype == 'int'
print(ride_sharing[['duration','duration_trim','duration_time']])
import numpy as np
print(np.mean(ride_sharing['duration_time']))

#
