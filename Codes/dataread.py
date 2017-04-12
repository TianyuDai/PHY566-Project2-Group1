import numpy as np
import matplotlib.pyplot as plt
import math
## For time saving consideration, we separete the calculation to 4 part. (0.61-0.635,0.64-0.67,0.675-0.7,0.705-0.71)
## Therefore, we store data in 4 txt files.
N=100
f1=np.loadtxt('0.61-0.635.txt')   # load data from txt
f2=np.loadtxt('0.64-0.67.txt')
f3=np.loadtxt('0.675-0.7.txt')
f4=np.loadtxt('0.705-0.71.txt')
f5=np.append(f1,f2)              # combine all the data
f5=np.append(f5,f3)
f5=np.append(f5,f4)
delta=np.linspace(0.61,0.71,21)   
delta=delta-0.6                  # calculate (P-Pc)
#deltat=np.linspace(0.61,0.635,6)  
ff5=np.log(f5)                   # calculate ff5 = log(P)
deltaP=np.log(delta)             # calculate deltaP = log(P-Pc)
slope=np.polyfit(deltaP,ff5,1)   # fit (deltaP,ff5) into equation log(P)=beta*log(P-Pc)+log(P0)
crv=np.poly1d(slope)             # get fitting equation
print crv
P0=np.exp(slope[1])              # calculate P0
beta=slope[0]                    # calculate beta
y=crv(deltaP)                    # calculate fitting curve
plt.plot(deltaP,ff5,'o-b')       # plot data curve
plt.plot(deltaP,y,'r')           # plot fitting curve
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

