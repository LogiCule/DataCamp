#Writing list comprehensions

squares = [i**2 for i in range(10)]

#Nested list comprehensions

matrix = [[col for col in range(5)] for row in range(5)]
for row in matrix:
    print(row)

#Using conditionals in comprehensions (1)

fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
new_fellowship = [member for member in fellowship if(len(member)>=7)]
print(new_fellowship)

#Using conditionals in comprehensions (2)

fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
new_fellowship = [member if len(member) >= 7 else '' for member in fellowship]
print(new_fellowship)

#Dict comprehensions

new_fellowship = {member:len(member) for member in fellowship}

#Write your own generator expressions

result = (num for num in range(31))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
for value in result:
    print(value)

#Changing the output in generator expressions

lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']
lengths = (len(person) for person in lannister)
for value in lengths:
    print(value)
    
#Build a generator

lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""
    for person in input_list:
        yield len(person)
for value in get_lengths(lannister):
    print(value)
    
#List comprehensions for time-stamped data

tweet_time = df['created_at']
tweet_clock_time = [entry[11:19] for entry in tweet_time]
print(tweet_clock_time)

#Conditional list comprehensions for time-stamped data

tweet_time = df['created_at']
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']
print(tweet_clock_time)

