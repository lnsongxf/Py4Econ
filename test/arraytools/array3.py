'''
Created on Jan 10, 2018

@author: fan
'''

# python "C:/Users/fan/Py4Econ/test/arraytools/array3.py"

import numpy as np
abc = np.random.rand(2,3,4)
print(abc[:,1])

efg = np.zeros((2,4))
abc[:,1] = efg
print(abc[:,1])
