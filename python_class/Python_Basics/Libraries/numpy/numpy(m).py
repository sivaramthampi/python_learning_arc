import numpy as np
".............................................................................................."
# a = np.array([1,2,3,4,5])
# print(a)
# print(type(a))
".............................................................................................."
# a = np.array([[1,2,3,4,5],[1,2,3,4,5]])
# print(a)
".............................................................................................."
# a = np.array([[[1,2,3,4,5],[1,2,3,4,5]],[[1,2,3,4,5],[1,2,3,4,5]]])
# print(a)
# print(a.ndim) # To check dimentions
".............................................................................................."
# a = np.array([[1,2,3],[5,6,7]])
# print(a)
# print(a.ndim)
# print(a.shape)   # array shape 
# print(a.itemsize) # size of memory
# print(a.size) # no of elements
# print(a.nbytes) # how many bytes
".............................................................................................."
"Array Slicing"
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
".............................................................................................."
# print(np.zeros(5))
# print(np.zeros((2,3)))  # Array only with the number 0
# print(np.zeros((2,3,2)))

# print(np.ones(4))
# print(np.ones((2,3)))  # Array only with the number 1
# print(np.ones((2,3,2)))   

# print(np.full((2,3,2),88)) # Array only with the number 88
# print(np.full((2,3),100))
".............................................................................................."
# a = np.array([[1,2,3,4,5,6,7],[18,9,10,11,12,13,14],[1,1,1,1,1,1,1]])
# print(a)
# print(np.full_like(a, 35)) # To copy the format of the array
".............................................................................................."
# print(np.random.rand(2,3)) # To create 1-D array with random numbers
".............................................................................................."
# print(np.random.randint(4,8,size=(3,3))) # To create 2-D array with random numbers (4 to 7)
".............................................................................................."
# print(np.random.randint(8,size=(3,3)))  # To create 2-D array with random numbers (0 to 7)
".............................................................................................."
# print(np.identity(5)) # To create identity mat
".............................................................................................."
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
".............................................................................................."
"To copy an array"
"ME-1"
# a = np.array([1,2,3,4]) 
# print(a)
# b = a
# print(b)
# b[1] = 100  # It will reflect all the changes to a
# print(b)
# print(a)

"ME-2"
# a = np.array([1,2,3,4]) 
# print(a)
# b = a.copy() # By using copy it wont change the original data
# print(b)
# b[1] = 100  
# print(b)
# print(a)
".............................................................................................."
# a = np.array([1,2,3,4])
# b = np.array([1,2,3,4])
# print(a + 2)    # This will add and print the values of the array
# print(a - 2)    # This will subtract and print the values of the array
# print(a / 2)    # This will divide and print the values of the array
# print(a * 2)    # This will multiply and print the values of the array
# print(a % 2)    # This will mod and print the values of the array
# print(a ** 2)   # This will power and print the values of the array
# print(a + b)    # This will add two arrays
# print(np.cos(a))  # This will give cos values and print the array
# print(np.sin(a))  # This will give sin values and print the array
# print(np.tan(a))  # This will give tan values and print the array
# a = np.ones((2,3))
# print(a)
# b = np.full((3,2),2) 
# print(b)
# print(np.matmul(a,b)) # Matrix multiplication
# arr = np.identity(3)
# print(np.linalg.det(arr))

"https://numpy.org/doc/stable/reference/routines.math.html <-- check this site to see more"
".............................................................................................."
# a = np.array([[1,2,3,4],[5,6,7,8]])
# print(np.min(a))
# print(np.max(a))
# print(np.mean(a))
# print(np.median(a))
".............................................................................................."
# a = np.array([[1,2,3,4],[5,6,7,8]])
# print(a.shape)
# print()
# print(a.reshape(8,1))
# print()
# print(a.reshape(4,2))
# print()
# print(a.reshape(2,2,2))
".............................................................................................."
# a = np.array([1,2,3,4])
# b = np.array([5,6,7,8])
# print(np.vstack([a,b]))
# print(np.vstack([a,b,b,a]))
".............................................................................................."
# a = np.ones((2,3))
# print(a)
# print()
# b = np.zeros((2,2))
# print(b)
# print()
# print(np.hstack([a,b]))
".............................................................................................."
"Range function in Numpy"
# print(np.arange(5))
# print(np.arange(1,9))
# print(np.arange(1,9,2))
".............................................................................................."
# print(np.arange(12).reshape(4,3))
".............................................................................................."
# print(np.linspace(1,3,4)) # It will print 4 values between 1 to 3 
# a = np.linspace(1,3,4)
# print(a)
# a = np.linspace(1,3,4).astype(int) # To print all integers
# print(a)
".............................................................................................."
# a = np.array([[1,2,3,4],[5,6,7,8]])
# b = a.ravel()  # to convert a 2-D array to 1-D array
# print(b)
".............................................................................................."