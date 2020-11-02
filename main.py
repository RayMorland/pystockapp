import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from assets.asset_one import AssetOne

print("Welcome to the app")
plt.style.use('seaborn') 
mpl.rcParams['font.family'] = 'serif'
np.random.seed(1000)
y = np.random.standard_normal(20)
x = np.arange(len(y))
plt.plot(x, y)
# plt.show()
    
aapl = AssetOne('APPL', 100)
print('{0}\'s value is {1}'.format(aapl.name ,aapl.value))
