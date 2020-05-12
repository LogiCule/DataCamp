#Random float

np.random.seed(123)
print(np.random.rand())

#Roll the dice

print(np.random.randint(1,7))
print(np.random.randint(1,7))

#Determine your next move

dice = np.random.randint(1,7)
if dice <= 2 :
    step = step - 1
elif dice<=5 :
    step=step+1
else:
    step = step + np.random.randint(1,7)
print(dice)
print(step)

#The next step

