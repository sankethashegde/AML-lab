import numpy as np 
"""import numpy as np
mylist=[1,2,3]
x=np.array(mylist)
print(x)
"""
#n=np.arange(0,30,2)

"""np.ones((5,4))
np.zeroes((2,3))
np.eye(4)
print(np.zeroes(2,3))
print(np.eye(4))"""


"""num=np.matrix([[11,121,130],
               [603,54,13],
               [512,34,67]])
print(num)
print(type(num))

print("MAin Diagonal elements:\n",np.diag(num))
print(" Diagonal elements above main diagonal:\n",np.diag(num,1))
print(" Diagonal elements below main diagonal:\n",np.diag(num,-1))
print(" Diagonal elements above main diagonal:\n",np.diag(num,2))"""

"""x=np.array([1,2,3] *3)
print(x)"""

"""p = np.array([1, 2, 3])
x=np.vstack([p,2*p])
print(x)"""

"""p=np.ones([3,3],int)
#p = np.array([1, 2, 3])
x=np.hstack([p,2*p])
print(x)"""

"""x=np.array([1,2,3])
y=np.array([4,5,6])
print(x)
print(y)
print(x+y)
print(x-y)
print(x*y)
print(x**2)
print(x/y)
print(x@y)
x.dot(y)
print(x.dot(y))

z=np.array([y,y**2])
print(z)
print(len(z))
print(z.shape)
print(z.T)
print(z.dtype)

z=z.astype('f')
print(z.dtype)

a=np.array([-4,-2,1,3,5])
print(a.sum())
print(a.max())
print(a.min())
print(a.std())
print(a.argmax())
print(a.argmin())"""


"""s=np.arange(100)
print(s)

s=np.arange(6)**2
print(s)
print(s[0],s[4],s[-1])
print(s[1:5])
print(s[-4:])
print(s[-4:-2])"""

r=np.arange(100)
r.resize((10,10))
print(r)
print(3,4)
print(r[:3,:-1])