import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)
print(x)
plt.plot(x,x**2, x, x**3, x, 2*x, x, 2**x)
plt.grid(True)
plt.axis([0,2, 0,8])
plt.show()


###  Add Label ####


x = np.arange(3)
print(x)
plt.plot(x,x**2, x, x**3, x, 2*x, x, 2**x)
plt.grid(True)
plt.title('Sample Plot')
plt.xlabel('x = np.arange(3)')
plt.xlim(0, 2)
plt.ylabel('y = f(x)')
plt.ylim(0, 8)
plt.show()`

### Add Legend ###

x = np.arange(3)
print(x)

plt.plot(x, x**2, label = 'x**2')
plt.plot(x, x**3, label = 'x**3')
plt.plot(x, 2*x, label = '2*x')
plt.plot(x, 2**x, label = '2**x')
plt.legend()
### or ##
plt.plot(x,x**2, x, x**3, x, 2*x, x, 2**x)
plt.legend(['x**2','x**3','2*x','2**x'])

plt.grid(True)
plt.title('Sample Plot')
plt.xlabel('x = np.arange(3)')
plt.xlim(0, 2)
plt.ylabel('y = f(x)')
plt.ylim(0, 8)
plt.show()

### Change Legend Location ###

x = np.arange(3)
print(x)
plt.plot(x,x**2, x, x**3, x, 2*x, x, 2**x)
plt.legend(['x**2','x**3','2*x','2**x'], loc = 'upper center')
plt.grid(True)
plt.title('Sample Plot')
plt.xlabel('x = np.arange(3)')
plt.xlim(0, 2)
plt.ylabel('y = f(x)')
plt.ylim(0, 8)
plt.savefig('test.png')
plt.show()