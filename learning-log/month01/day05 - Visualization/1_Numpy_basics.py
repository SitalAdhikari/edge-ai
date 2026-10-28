import numpy as np

measurements = np.array([10,20,30])
print(measurements*2)
print(type(measurements))


value1 = np.zeros(5)
value2 = np.zeros(5, dtype = int)
print(value2)

print(np.arange(10))
print(np.arange(2,14,3))

a = np.array([12.5,23.5,76.2,23.4,55,33.5,70.1])
b = np.array([[1,2],[2,3]])
print(a.shape)
print(b.shape)
print(a.size)
print(b.size)
print(a.ndim)
print(b.ndim)
print(a.dtype)

# it also supports the indexing
print(a[0])

#to print last value:
print(a[-1])

#sorting
print(np.sort(a))

#largest 5 values:
sorted_value = np.sort(a)
print(sorted_value[-5:])



# few more exercise:
nparr = np.array([5,10,15,20])
nparr2 = np.zeros(6, dtype=int)
nparr3 = np.arange(2,11,2)
print(nparr3)
print(nparr3.shape)

#select first 3 in nparr:
print(nparr[:3])

#largest in nparr
sort_nparr = np.sort(nparr)
print(sort_nparr[-1])
