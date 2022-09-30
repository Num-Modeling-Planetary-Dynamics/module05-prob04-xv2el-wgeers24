import matplotlib.pyplot as plt
import numpy as np
rMag=np.linalg.norm(x)
u=-G(m1+m2)
vMag=np.linalg.norm(v)
h=np.cross(x,v)
hMag=np.abs(np.sqrt(h**2))

a=((2/rMag)-(vMag**2)/u)**-1

e=np.sqrt(1-(h**2/(u*a)))
I=np.arccos()

plt.plot(t,a)
plt.xlabel('Time(Myr)')
plt.ylabel('semi-major axis(a)')

plt.plot(t,I)
plt.xlabel('Time(Myr)')
plt.ylabel('Inclination')


