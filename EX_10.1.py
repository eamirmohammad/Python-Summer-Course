# EX_10.1:
import numpy as np
import matplotlib.pyplot as plt

#1.1:
print ('1.1:')
x = 10
print ('x is equal to ', x, '\n')

#1.2:
print ('1.2:')
xx = np.power (x ,2 )
print ('square of x is equal to ',xx, '\n')

#1.3:
print ('1.3:')
theta = 30
print ('Angle is equal to ',theta, '\n')

#1.4:
print ('1.4:')
Sin_t = None
Cos_t = None
Sin_t = np.sin (theta)
Cos_t = np.cos (theta)
print ('Sin of theta = ', Sin_t)
print ('Cos of theta = ', Cos_t, '\n')

if Sin_t == 0.5:
    print ('Angles are measured with degrees')
else:
    print ('Angles are measured with Radians')

#1.5:
print ('1.5:')
meshPoints = np.linspace (-1,1,500)

#1.6:
print ('1.6:')
num53 = None
num53 = meshPoints[53-1]
print ('53th element = ',num53,'\n')

#1.7:
print ('1.7:')
y = np.sin(2*np.pi*meshPoints)
plt.plot(meshPoints, y)
plt.show()

