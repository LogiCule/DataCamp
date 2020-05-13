#Write a simple function

def shout():
    """Print a string with three exclamation marks"""
    shout_word = "congratulations"+"!!!"
    print(shout_word)
shout()

#Single-parameter functions

def shout(word):
    """Print a string with three exclamation marks"""
    shout_word = word + '!!!'
    print(shout_word)
shout('congratulations')

#Functions that return single values

def shout(word):
    """Return a string with three exclamation marks"""
    shout_word = word+'!!!'
    return shout_word
yell = shout('congratulations')
print(yell)

#Functions with multiple parameters

def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    shout1 = word1+"!!!"
    shout2 = word2+"!!!"
    new_shout=shout1+shout2
    return new_shout
yell = shout("congratulations","you")
print(yell)

#A brief introduction to tuples

num1,num2,num3 = nums
even_nums = (2,num2,num3)

#Functions that return multiple values

def shout_all(word1, word2):
    """Concatenate strings with three exclamation marks"""
    shout1 = word1+"!!!"
    shout2 = word2+"!!!"
    new_shout=(shout1,shout2)
    return new_shout
yell1,yell2 = shout_all("congratulations","you")
print(yell1)
print(yell2)

#Bringing it all together (1)

import pandas as pd
df = pd.read_csv("tweets.csv")
langs_count = {}
col = df['lang']
for entry in col:
    if entry in langs_count.keys():
        langs_count[entry]+=1
    else:
        langs_count[entry]=1
print(langs_count)

#Bringing it all together (2)


def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""
    langs_count = {}
    col = df[col_name]
    for entry in col:
        if entry in langs_count.keys():
            langs_count[entry]+=1
        else:
            langs_count[entry]=1
    return langs_count
result=count_entries(tweets_df,'lang')
print(result)

