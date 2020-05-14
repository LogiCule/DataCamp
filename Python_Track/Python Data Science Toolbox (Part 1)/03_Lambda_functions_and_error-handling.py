#Writing a lambda function you already know

echo_word = (lambda a,y:a*y)
result = echo_word('hey',5)
print(result)

#Map() and lambda functions

spells = ["protego", "accio", "expecto patronum", "legilimens"]
shout_spells = map(lambda a: a+'!!!', spells)
shout_spells_list=list(shout_spells)
print(shout_spells_list)

#Filter() and lambda functions

fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']
result` = filter(lambda a : len(a)>6, fellowship)
result_list = list(result)
print(result_list)

#Reduce() and lambda functions

from functools import reduce
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']
result = reduce(lambda a,x:a+x, stark)
print(result)

#Error handling with try-except

def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    echo_word, shout_words = "",""
    try:
        echo_word = word1*echo
        shout_words = echo_word+"!!!"
    except:
        print("word1 must be a string and echo must be an integer.")
    return shout_words
shout_echo("particle", echo="accelerator")

#Error handling by raising an error

def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    if echo<0:
        raise ValueError("echo must be greater than or equal to 0")
    echo_word = word1 * echo
    shout_word = echo_word + '!!!'
    return shout_word
shout_echo("particle", echo=5)

#Bringing it all together (1)

result = filter(lambda a: a[:2]=='RT',tweets_df['text'])
res_list = list(result)
for tweet in res_list:
    print(tweet)
    
#Bringing it all together (2)

def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    cols_count = {}
    try:
        col = df[col_name]
        for entry in col:
            if entry in cols_count.keys():
                cols_count[entry] += 1
            else:
                cols_count[entry] = 1
        return cols_count
    except:
        print('The DataFrame does not have a ' + col_name + ' column.')
result1 = count_entries(tweets_df, 'lang')
print(result1)

#Bringing it all together (3)

def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')
    cols_count = {}
    col = df[col_name]
    for entry in col:
        if entry in cols_count.keys():
            cols_count[entry] += 1
        else:
            cols_count[entry] = 1
    return cols_count
result1 = count_entries(tweets_df)
print(result1)

