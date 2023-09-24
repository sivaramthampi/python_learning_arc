
import numpy as np
import matplotlib.pyplot as mpl
".............................................................................................."
# x = np.arange(0,10)
# y = np.arange(11,21)
# mpl.scatter(x,y,c="r")
# mpl.title('scatter points')
# mpl.xlabel('x')
# mpl.ylabel('y')
# mpl.show()
".............................................................................................."
# x = np.arange(0,10)
# y = np.arange(11,21)
# mpl.scatter(x,y,c="r")  # c is represented as color - here it is set as red (r)
# mpl.title('scatter points')
# mpl.xlabel('x')
# mpl.ylabel('y')
# mpl.savefig("myfig(matlib).png")
# mpl.show()
".............................................................................................."
# a = np.arange(0,10)
# b = a * a
# mpl.plot(a,b,'r*--',linewidth=5,markersize=20)  # c is represented as color - here it is set as red (r)
# mpl.title("2D PLOT")
# mpl.xlabel('x')
# mpl.ylabel('y')
# mpl.show()
".............................................................................................."
# x = np.arange(0,10)
# y = x * x
# mpl.subplot(2,2,1)
# mpl.plot(x,y,'r')
# mpl.subplot(2,2,2)
# mpl.plot(x,y,'g--')
# mpl.subplot(2,2,3)
# mpl.plot(x,y,'bo')
# mpl.subplot(2,2,4)
# mpl.plot(x,y,'y*')
# mpl.subplot(2,2,4)
# mpl.plot(x,y,'y*')
# mpl.show()
".............................................................................................."
# x = np.array([0,1,2,3])
# y = np.array([3,8,1,10])
# mpl.subplot(2,2,1)
# mpl.plot(x,y,'r') # Red
# mpl.subplot(2,2,2)
# mpl.plot(x,y,'g--') # Green
# mpl.subplot(2,2,3)
# mpl.plot(x,y,'b--') # Blue
# mpl.subplot(2,2,4)
# mpl.plot(x,y,'k-') # Black
# mpl.show() 
".............................................................................................."
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

# Plotting 1 (Sales)
mpl.subplot(1, 2, 1)
mpl.plot(x,y)
mpl.title("SALES")


# Plotting 2 (Income)
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
mpl.subplot(1, 2, 2)
mpl.plot(x,y)
mpl.title("INCOME")
mpl.show()
".............................................................................................."