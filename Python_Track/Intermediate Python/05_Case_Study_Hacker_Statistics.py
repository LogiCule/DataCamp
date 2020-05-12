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

for x in range(100) :
    step=random_walk[x]
    dice = np.random.randint(1,7)
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)
    random_walk.append(step)
print(random_walk)

#How low can you go?

random_walk=[0]
for x in range(100) :
    step=random_walk[x]
    dice = np.random.randint(1,7)
    if dice <= 2:
        step = max(0,step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)
    random_walk.append(step)
print(random_walk)

#Visualize the walk

import matplotlib.pyplot as plt
plt.plot(random_walk)
plt.show()

#Simulate multiple walks

for i in range(10) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)
print(all_walks)

#Visualize all walks

np_aw=np.array(all_walks)
plt.plot(np_aw)
plt.show()
plt.clf()
np_aw_t=np.transpose(np_aw)
plt.plot(np_aw_t)
plt.show()

#Plot the distribution

ends = np_aw_t[-1,:1]
plt.hist(ends)
plt.show()
