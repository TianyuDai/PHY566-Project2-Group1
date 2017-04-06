import numpy as np
import matplotlib.pyplot as plt
import math
N=100
f1=np.loadtxt('0.61-0.635.txt')
f2=np.loadtxt('0.64-0.67.txt')
f3=np.loadtxt('0.675-0.7.txt')
f4=np.loadtxt('0.705-0.71.txt')
f5=np.append(f1,f2)
f5=np.append(f5,f3)
f5=np.append(f5,f4)
delta=np.linspace(0.61,0.71,21)
delta=delta-0.6
#deltat=np.linspace(0.61,0.635,6)
ff5=np.log(f5)
deltaP=np.log(delta)
slope=np.polyfit(deltaP,ff5,1)
crv=np.poly1d(slope)
print crv
F0=np.exp(slope[1])
beta=slope[0]
y=crv(deltaP)
plt.plot(deltaP,ff5,'o-b')
plt.plot(deltaP,y,'r')
equation = 'y = ' + str(round(slope[0],4)) + 'x' ' + ' + str(round(slope[1],4))         
plt.plot()
plt.title('Fraction N=%d' %N) 
plt.xlabel('$log(P-Pc)$') 
plt.ylabel('$log(F)$') 
plt.annotate(equation, xy=(deltaP[6], y[6]), xytext=(-3.5,-0.2),
            arrowprops=dict(arrowstyle='->')
            )
plt.savefig('fraction_all.pdf') 
plt.show()

