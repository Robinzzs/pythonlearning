# -*- coding: utf-8 -*-

import functools

int2 = functools.partial(int, base=2)

print(int2('100000'))


import numpy as np

a = [3,4]

b = np.linalg.norm(a,2)

print(b)


arr = np.arange(12).reshape((3, 4))

print(arr)

slc = arr[1,:]
print(slc)