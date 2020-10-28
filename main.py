import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from people.person import Person

print("Welcome to the app")
plt.style.use('seaborn') 
mpl.rcParams['font.family'] = 'serif'
np.random.seed(1000)
y = np.random.standard_normal(20)
x = np.arange(len(y))
plt.plot(x, y)
# plt.show()
    
bill = Person('Bill', 100)
print('{0}\'s height is {1}'.format(bill.name ,bill.height))
