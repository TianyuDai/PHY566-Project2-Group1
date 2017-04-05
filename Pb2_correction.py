import pylab as pl  
import random
import math

N = 50 # the length of sides of a grid
simulations = 5
P = pl.linspace(0.65,0.7,6) # a list to record different Ps
Fraction = [] # a list to record different fractions
Pc = 0.6
cont=0
# loop
for p in P:
    print p
    for m in range(simulations):
        print m
        grid = pl.zeros([N+2,N+2]) # generate an empty grid
        grid[1:(N+1),0] = pl.linspace(1,N,N) # boundary condition
        grid[0,1:(N+1)] = pl.linspace(N+1,2*N,N)
        grid[1:(N+1),N+1] = pl.linspace(2*N+1,3*N,N)
        grid[N+1,1:(N+1)] = pl.linspace(3*N+1,4*N,N)
        s = [0]*(N)+[N+1]*(N)+range(1,N+1)+range(1,N+1) # x coordinate of percolated sites
        t = range(1,N+1)+range(1,N+1)+[0]*(N)+[N+1]*(N) # y coordinate of percolated sites
        judge = 0
        clusnum = 4*N
        while (clusnum-4*N) < p*N**2:
            Ranm = random.randint(0,N**2-1) # generate a random number
            x = Ranm/N+1 # xth-row
            y = Ranm%N+1# yth-column
            if not grid[x,y]: # check whether the site (x,y) is empty
                clusnum += 1
                grid[x,y] = clusnum # put a point at site (x,y)
                Neighbor = [grid[x-1,y],grid[x+1,y],grid[x,y-1],grid[x,y+1]]
                if max(grid[x-1,y],grid[x+1,y],grid[x,y-1],grid[x,y+1]): # check neighbering sites
                     for (i,j) in zip(s,t):
                        if pl.any(Neighbor==grid[i,j]):
                            grid[i,j] = clusnum
                s.append(x)
                t.append(y)
            Check = [clusnum-max(grid[0,:]),clusnum-max(grid[N+1,:]),clusnum-max(grid[:,0]),clusnum-max(grid[:,N+1])]   
            if not pl.any(Check):
                judge = clusnum
                
        counter=sum(sum((grid[i,:]==judge) for i in range(1,N+1))[j] for j in range(1,N+1))# number of sites in spanning cluster          
        Fraction.append(counter/float(N**2*p*simulations))
deltaP = [Pn-Pc for Pn in P]

pl.savetxt('Fraction_1.txt',Fraction)

pl.plot([math.log(i) for i in deltaP],[math.log(j) for j in Fraction],'o-b')         
pl.title('Fraction N=%d' %N) 
pl.xlabel('$log(P-Pc)$') 
pl.ylabel('$log(F)$') 
pl.savefig('fraction.pdf') 
pl.show()
