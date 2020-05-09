#Line plot (1)

print(year[-1])
print(pop[-1])
import matplotlib.pyplot as plt
plt.plot(year,pop)
plt.show();

#Line plot (3)

print(gdp_cap[-1])
print(life_exp[-1])
plt.plot(gdp_cap,life_exp)
plt.show()

#Scatter Plot (1)

plt.scatter(gdp_cap, life_exp)
plt.xscale('log')
plt.show()

#Scatter plot (2)

import matplotlib.pyplot as plt
plt.scatter(pop,life_exp)
plt.show()

#Build a histogram (1)

plt.hist(life_exp,bins=10)
plt.show();

#Build a histogram (2): bins

plt.hist(life_exp,bins=5)
plt.show()
plt.clf()
plt.hist(life_exp,bins=20)
plt.show()
plt.clf()

#Build a histogram (3): compare

plt.hist(life_exp,bins=15)
plt.show()
plt.clf()
plt.hist(life_exp1950,bins=15)
plt.show()
plt.clf()

#Labels

plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)
plt.show()

#Ticks

plt.xticks(tick_val,tick_lab)
plt.show()

#Sizes

import numpy as np
np_pop=np.array(pop)
np_pop*=2

#
