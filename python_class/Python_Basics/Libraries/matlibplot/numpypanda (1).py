import numpy as np 

# a = np.array([1,2,3,4,5])
# print(a)
# print(type(a))

# a = np.array([[1,2,3,4,5],[1,2,3,4,5]])
# print(a)

# a = np.array([[[1,2,3,4,5],[1,2,3,4,5]],[[1,2,3,4,5],[1,2,3,4,5]]])
# print(a)
# print(a.ndim) 

# a = np.array([[1,2,3],[5,6,7]])
# print(a)
# print(a.ndim)
# print(a.shape)
# print(a.itemsize) # size of memory
# print(a.size) # no of elements
# print(a.nbytes) # how many bytes

# import numpy as np 

# a = np.array([[1,2,3,4,5,6,7],[18,9,10,11,12,13,14],[1,1,1,1,1,1,1]])
# print(a)
# print()

# print(a[1])
# print(a[0])
# print(a[1,5])
# print(a[1:])
# print(a[0,:])
# print(a[0,1:5])
# print(a[:,2])
# print(a[0,1:6:2])
# print(a[:,1::2])
# print(a[1][1])
# print(a[1,1])
# print(a[1][1:4])
# print(a[1:,3:]) 
# print(a[:2,4:])


import numpy as np 

# a = np.array([[1,2,3,4,5,6,7],[18,9,10,11,12,13,14],[1,1,1,1,1,1,1]])
# print(a)
# print()

# a[0,4]=20
# print(a)
# a[:2,-1]=[8,15]
# print(a)
# a[:,-1]=[8,15,2]
# print(a)

# a = np.array([[[1,2],[3,4,]],[[5,6],[7,8]]])
# print(a)
# print()
# # print(a[0])
# # print(a[0,1])
# # print(a[1,1])
# # print(a[1,:,1])
# # print(a[0,0:2,0])
# # a[1]=[[9,9],[9,9]]
# # print(a)
# a[1,:]=[[9,9],[9,9]]
# print(a)

import numpy as np 

# print(np.zeros(5))
# print(np.zeros((2,3)))
# print(np.zeros((2,3,2)))

# print(np.ones(4))
# print(np.ones((2,3)))
# print(np.ones((2,3,2)))

# print(np.full((2,3,2),88))
# print(np.full((2,3),100))

# a = np.array([[1,2,3,4,5,6,7],[18,9,10,11,12,13,14],[1,1,1,1,1,1,1]])
# print(a)
# print(np.full_like(a, 35))


import numpy as np 
# print(np.random.rand(2,3))

# print(np.random.randint(4,8,size=(3,3)))
# print(np.random.randint(8,size=(3,3)))

# print(np.identity(5))

# a = np.array([[1,2,3]])
# print(np.repeat(a, 3,axis=0))
# print(np.repeat(a, 3,axis=1))
# print(np.repeat(a, 4,axis=0))

# one = np.ones((5,5))
# ze = np.zeros((3,3))
# ze[1,1]=9
# print(ze)
# print()
# one[1:-1,1:-1]=ze
# print(one)


import numpy as np

# a = np.array([1,2,3,4])
# print(a)

# b=a
# print(b)
# b[1]=100
# print(b)
# print(a) 

# b = a.copy()
# b[1]=100
# print(b)
# print(a)


import numpy as np
a = np.array([1,2,3,4])

# print(a+2)
# print(a-2)
# print(a*2)
# print(a**2)

# a = np.array([1,2,3,4])
# b = np.array([1,2,3,4])
# print(a+b)

# print(np.cos(a))


# a = np.ones((2,3))
# print(a)
# b = np.full((3,2),2)
# print(b)
# print(np.matmul(a,b)) 

# arr = np.identity(3)
# print(arr)
# print(np.linalg.det(arr))


# a = np.array([[1,2,3],[4,5,6]])
# print(np.min(a))
# print(np.max(a))
# print(np.mean(a))
# print(np.median(a))


# before = np.array([[1,2,3,4],[5,6,7,8]])
# print(before)
# print()
# after = before.reshape(8,1)
# print(after)

# after = before.reshape(4,2)
# print(after)

# after = before.reshape(2,2,2)
# print(after)

# a = np.array([1,2,3,4])
# b = np.array([5,6,7,8])
# print(np.vstack([a,b,a,b,b]))

# a = np.ones((2,3))
# b = np.zeros((2,2))
# print(np.hstack([a,b,b]))

# print(np.arange(5))
# print(np.arange(5,9))
# print(np.arange(1,9,2))

# print(np.arange(12).reshape(4,3))

# print(np.linspace(1,2,6).astype(int)) 

# be = np.array([[1,2,3,4],[5,6,7,8]])
# new = be.ravel()
# print(new)


##################################################################################
# matplotlib
##################################################################################
import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(0,10)
# y = np.arange(11,21)
# plt.scatter(x,y,c='r')
# plt.title('scatter plot')
# plt.xlabel('xaxis')
# plt.ylabel('yaxis')
# plt.show()


# x = np.arange(0,10)
# y = np.arange(11,21)
# plt.scatter(x,y,c='r')
# plt.title('scatter plot')
# plt.xlabel('xaxis')
# plt.ylabel('yaxis')
# plt.savefig('my.png')
# plt.show()

# x = np.arange(0,10)
# y=x*x
# plt.plot(x,y,'r*--',linewidth=5,markersize=20)
# plt.title('2d plot')
# plt.xlabel('xaxis')
# plt.ylabel('yaxis')
# plt.show()


# x = np.arange(0,10)
# y=x*x
# plt.subplot(2,1,1)
# plt.plot(x,y,'r')
# plt.subplot(2,2,2)
# plt.plot(x,y,'g--')
# plt.subplot(2,2,3)
# plt.plot(x,y,'bo')
# plt.subplot(2,2,4)
# plt.plot(x,y,'y*')
# plt.show()


# x = np.array([0,1,2,3])
# y = np.array([3,8,1,10])
# plt.subplot(2,1,1)
# plt.plot(x,y,'r')
# plt.subplot(2,2,2)
# plt.plot(x,y,'g--')
# plt.subplot(2,2,3)
# plt.plot(x,y,'bo')
# plt.subplot(2,2,4)
# plt.plot(x,y,'y*')
# plt.show() 


#plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(1, 2, 1)
# plt.plot(x,y)
# plt.title("SALES")

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.title("INCOME")

# plt.show()

# x = np.array([0,1,2,3])
# y = 3*x+5
# plt.plot(x,y)
# plt.show()

# x=np.arange(0,4*np.pi,0.1)
# y=np.sin(x)
# plt.plot(x,y)
# plt.show()

# x=np.arange(0,4*np.pi,0.1)
# y=np.cos(x)
# plt.plot(x,y)
# plt.show()

# x=[3,8,10]
# y=[11,16,9]

# x2=[3,9,11]
# y2=[11,15,7]

# plt.bar(x,y)
# plt.bar(x2,y2)
# plt.title("bar graph")
# plt.xlabel('xaxis')
# plt.ylabel('yaxis')
# plt.show() 

# a = np.array([23,4,44,4,5,6,77,55,88,35,75,23,68,98,44,67])
# plt.hist(a)
# plt.title('histogram')
# plt.show()


# data = [np.random.normal(0,std,100) for std in range(1,4)]
# print(data)
# plt.boxplot(data,vert=True)
# plt.show()


# label = ['Python','C++','Ruby','Java']
# size = [215,130,245,210]
# colors = ['gold','yellowgreen','lightcoral','lightskyblue']
# explode = (0.4,0,0,0)

# plt.pie(size,explode=None,labels=label,colors=colors,shadow=True)
# plt.axis('equal')
# plt.show()