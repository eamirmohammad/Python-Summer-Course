#EX_10.3 Amir Mohammad Eslami
import numpy as np
import matplotlib.pyplot as plt
#3.1:
print ('3.1')
x = np.linspace (0,10, num = 500)
y1 =  np.exp(-(x)/10) * np.sin( np.pi *x )
y2 = x*np.exp(-(x)/3)

plt.figure()
plt.plot(x, y1, label = 'f(x)')

plt.plot(x, y2, label = 'g(x)')
plt.legend(['f(x)','g(x)'])

plt.axhline(y=0, label = 'x')
plt.axvline(x=0, label = 'y')
plt.xlabel("X axis ")
plt.ylabel("Y axis ")



#3.2:
print ('3.2')

theta = np.linspace (0,2*np.pi, 500)
#r0 = 0.8
r0 = 0.8
r1 = r0 + np.cos(theta)
x1 = r1 * np.cos (theta)
y1 = r1 * np.sin (theta)

#r0 = 1
r0 = 1
r2 = r0 + np.cos(theta)
x2 = r2 * np.cos (theta)
y2 = r2 * np.sin (theta)

#r0 = 1.2
r0 = 1.2
r3 = r0 + np.cos(theta)
x3 = r3 * np.cos (theta)
y3 = r3 * np.sin (theta)

plt.figure()
plt.plot (x1,y1, label = 'r0 = 0.8')
plt.plot (x2,y2, label = 'r0 = 1')
plt.plot (x3,y3, label = 'r0 = 1.2')

plt.legend(['r0 = 0.8','r0 = 1','r0 = 1.2'])

plt.axhline(y=0, label = 'x')
plt.axvline(x=0, label = 'y')
plt.xlabel("X axis ")
plt.ylabel("Y axis ")


plt.show()







