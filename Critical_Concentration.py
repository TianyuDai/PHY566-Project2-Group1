import pylab as pl  
import random
import time
time1 = time.time()

N = [5,10,15]#,20,30,50,80] # the length of sides of a grid
Pc = [] # a list to record critical concentrations of different grids
inverseN = [] # a list to record 1/N
for n in N:
    Pc_n = 0
    for m in range(50):
        grid = pl.zeros([n+2,n+2]) # generate an empty grid
        grid[1:(n+1),0] = pl.linspace(1,n,n) # boundary condition
        grid[0,1:(n+1)] = pl.linspace(n+1,2*n,n)
        grid[1:(n+1),n+1] = pl.linspace(2*n+1,3*n,n)
        grid[n+1,1:(n+1)] = pl.linspace(3*n+1,4*n,n)
        s = [0]*(n)+[n+1]*(n)+range(1,n+1)+range(1,n+1) # x coordinate of percolated sites
        t = range(1,n+1)+range(1,n+1)+[0]*(n)+[n+1]*(n) # y coordinate of percolated sites
        Check = [1, 0, 0, 0]
        clusnum = 4*n
        while pl.any(Check):
            Ranm = random.randint(0,n**2-1) # generate a random number
            x = Ranm/n+1 # xth-row
            y = Ranm%n+1# yth-column
            if grid[x,y] == 0: # check whether the site (x,y) is empty
                clusnum += 1
                grid[x,y] = clusnum # put a point at site (x,y)
                Neighbor = [grid[x-1,y],grid[x+1,y],grid[x,y-1],grid[x,y+1]]
                if max(grid[x-1,y],grid[x+1,y],grid[x,y-1],grid[x,y+1]): # check neighboring sites
                    for (i,j) in zip(s,t): 
                        if pl.any(Neighbor==grid[i,j]):
                            grid[i,j] = clusnum
                s.append(x)
                t.append(y)
            Check = [clusnum-max(grid[0,:]),clusnum-max(grid[n+1,:]),clusnum-max(grid[:,0]),clusnum-max(grid[:,n+1])] # decide when to stop the loop
        Pc_n += n**2+4-sum(sum(grid[i,:]==0) for i in range(n+2))
    Pc.append(Pc_n/float(n**2*50))
    inverseN.append(1.0/n)

#plot
time2 = time.time()
pl.plot(inverseN,Pc,'-bo')
pl.title('Critical Concentration\nCalculation Time = %.2fs' % (time2-time1)) 
pl.xlabel('$1/N$') 
pl.ylabel('Pc') 
pl.savefig('Critical.pdf')
pl.show() 
