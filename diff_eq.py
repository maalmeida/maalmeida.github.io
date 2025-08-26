import numpy as np
import matplotlib. pyplot as plt
from scipy.integrate import odeint

# Solve dv/dt = [y, - cx] for v = [x,y]

def odefn(v,t, c):

    x, y = v

    dvdt = [y, -c*x ]

    return dvdt

v0 = [1.0, 0.0]

t = np.arange(0.0, 10.0, 0.1)

c = 5;

sol = odeint(odefn, v0, t,args=(c,))

plt.plot(t, sol[:,0],"b")

plt.xlabel("Time (sec)")

plt.ylabel("Position")

plt.title("Position vs Time")

plt.show()