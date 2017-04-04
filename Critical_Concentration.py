import pylab as pl  
import random 
import numpy as np
import time
time1 = time.time()

N = [5,10,15,20,30,50,80] # the length of sides of a grid
simulations = 50
Pc = [0.0]*len(N)

for n in range(len(N)):
    print "grid length", N[n]
    for m in range(simulations):
        print m
        grid = pl.zeros([N[n]+2,N[n]+2]) # generate an empty grid
        grid[1:(N[n]+1),0] = pl.linspace(1,N[n],N[n]) # boundary condition
        grid[0,1:(N[n]+1)] = pl.linspace(N[n]+1,2*N[n],N[n])
        grid[1:(N[n]+1),N[n]+1] = pl.linspace(2*N[n]+1,3*N[n],N[n])
        grid[N[n]+1,1:(N[n]+1)] = pl.linspace(3*N[n]+1,4*N[n],N[n])
        Check = [1, 0, 0, 0]
        clusnum = 4*N[n]
        while np.any(Check):
            Ranm = random.randint(0,N[n]**2-1) # generate a random number
            x = Ranm/N[n]+1 # xth-row
            y = Ranm%N[n]+1# yth-column
            if grid[x,y] == 0: # check whether the site (x,y) is empty
                clusnum += 1
                grid[x,y] = clusnum # put a point at site (x,y)
                Neighbor = [grid[x-1,y],grid[x+1,y],grid[x,y-1],grid[x,y+1]]
                # check neighbering sites
                if max(grid[x-1,y],grid[x+1,y],grid[x,y-1],grid[x,y+1]):
                    for i in range(N[n]+2): 
                        for j in range(N[n]+2): 
                            if grid[i,j]:
                                if np.any(Neighbor==grid[i,j]):
                                    grid[i,j] = clusnum
            Check = [clusnum-max(grid[0,:]),clusnum-max(grid[N[n]+1,:]),clusnum-max(grid[:,0]),clusnum-max(grid[:,N[n]+1])]
        Pc[n] += (clusnum-4*N[n])/float(N[n]**2*simulations)

#save
np.savetxt('pc.txt',Pc)
#Pc=np.loadtxt('pc.txt')
        
#plot
inverseN = [1.0/k for k in N]
pl.plot(inverseN,Pc,'o-b')
pl.title('Critical Concentration') 
pl.xlabel('$1/N$') 
pl.ylabel('Pc') 
pl.savefig('Critical_2.pdf') 
pl.show()  

time2 = time.time()
print time2 - time1


