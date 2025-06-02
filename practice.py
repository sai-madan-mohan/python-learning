# accessing an element in a list
a=[1,2,3,4,5]
print(a[2])

# modify an element in a lissy
a=[1,2,3,4,5]
a[3]=10
print(a)
# adding an element in a alist
a=[1,10,12,34]
a.append(45)
print(a)
a.extend([38,44])
print(a)
# remoiving an element in a list
a=[1,12,32,12,25]
a.remove(12)
a.pop()
print(a)

# slicing a list
a=[1,2,3,4,5]
print(a[1:4])

# copying a list
a=[1,2,3,4,5]
b=a.copy()
print(b)

