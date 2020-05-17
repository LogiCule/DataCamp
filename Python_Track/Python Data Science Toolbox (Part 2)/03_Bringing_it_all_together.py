#Dictionaries for data science

zipped_lists = zip(feature_names,row_vals)
rs_dict = dict(zipped_lists)
print(rs_dict)

#Writing a function to help you

def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""
    zipped_lists = zip(list1, list2)
    rs_dict = dict(zipped_lists)
    return rs_dict
rs_fxn = lists2dict(feature_names,row_vals)
print(rs_fxn)

#Using a list comprehension

print(row_lists[0])
print(row_lists[1])
list_of_dicts = [lists2dict(feature_names,sublist) for sublist in row_lists]
print(list_of_dicts[0])
print(list_of_dicts[1])

#Turning this all into a DataFrame

import pandas as pd
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]
df = pd.DataFrame(list_of_dicts)
print(df.head())

#Processing data in chunks (1)

with open('world_dev_ind.csv') as file:
    file.readline()
    counts_dict = {}
    for j in range(1000):
        line = file.readline().split(',')
        first_col = line[0]
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1
print(counts_dict)

#Writing a generator to load data in chunks (2)

def read_large_file(file_object):
    """A generator function to read a large file lazily."""
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data
with open('world_dev_ind.csv') as file:
    gen_file = read_large_file(file)
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))
    
#Writing a generator to load data in chunks (3)

counts_dict = {}
with open('world_dev_ind.csv') as file:
    for line in read_large_file(file):
        row = line.split(',')
        first_col = row[0]
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1
print(counts_dict)
