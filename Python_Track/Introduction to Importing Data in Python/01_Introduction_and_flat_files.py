#Importing entire text files

file = open('moby_dick.txt', 'r')
print(file.read())
print(file.closed)
file.close()
print(file.closed)

#Importing text files line by line

with open('moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    
