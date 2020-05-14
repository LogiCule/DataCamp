#The keyword global

team = "teen titans"
def change_team():
    """Change the value of the global variable team."""
    global team
    team="justice league"
print(team)
change_team()
print(team)

#Nested Functions I

def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'
    return (inner(word1),inner(word2), inner(word3))

#Nested Functions II

def echo(n):
    """Return the inner_echo function."""
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word
    return inner_echo
twice = echo(2)
thrice = echo(3)
print(twice('hello'), thrice('hello'))

#The keyword nonlocal and nested functions

def echo_shout(word):
    """Change the value of a nonlocal variable"""
    echo_word=word*2
    print(echo_word)
    def shout():
        """Alter a variable in the enclosing scope"""    
        nonlocal echo_word
        echo_word = echo_word+"!!!"
    shout()
    print(echo_word)
echo_shout("hello")

#Functions with one default argument

def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""
    echo_word = word1*echo
    shout_word = echo_word + '!!!'
    return shout_word
no_echo = shout_echo("Hey")
with_echo = shout_echo("Hey",5)
print(no_echo)
print(with_echo)

#Functions with multiple default arguments

def shout_echo(word1,echo=1, intense=False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    echo_word = word1 * echo
    if intense is True:
        echo_word_new = echo_word.upper() + '!!!'
    else:
        echo_word_new = echo_word + '!!!'
    return echo_word_new
with_big_echo = shout_echo("Hey",5,True)
big_no_echo = shout_echo("Hey",intense=True)
print(with_big_echo)
print(big_no_echo)

#Functions with variable-length arguments (*args)

def gibberish(*args):
    """Concatenate strings in *args together."""
    hodgepodge=""
    for word in args:
        hodgepodge += word
    return hodgepodge
one_word = gibberish("luke")
many_words = gibberish("luke", "leia", "han", "obi", "darth")
print(one_word)
print(many_words)

#Functions with variable-length keyword arguments (**kwargs)

def report_status(**kwargs):
    """Print out the status of a movie character."""
    print("\nBEGIN: REPORT\n")
    for i,j in kwargs.items():
        print(i + ": " + j)
    print("\nEND REPORT")
report_status(name="luke",affiliation="jedi",status="missing")
report_status(name="anakin", affiliation="sith lord", status="deceased")

#Bringing it all together (1)

def count_entries(df, col_name):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    cols_count = {}
    col = df[col_name]
    for entry in col:
        if entry in cols_count.keys():
            cols_count[entry] += 1
        else:
            cols_count[entry] = 1
    return cols_count
result1 = count_entries(tweets_df,"lang")
result2 = count_entries(tweets_df,"source")
print(result1)
print(result2)

#Bringing it all together (2)

def count_entries(df, *args):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    cols_count = {}
    for col_name in args:
        col = df[col_name]
        for entry in col:
            if entry in cols_count.keys():
                cols_count[entry] += 1
            else:
                cols_count[entry] = 1
    return cols_count
result1 = count_entries(tweets_df,'lang')
result2 = count_entries(tweets_df, 'lang', 'source')
print(result1)
print(result2)

