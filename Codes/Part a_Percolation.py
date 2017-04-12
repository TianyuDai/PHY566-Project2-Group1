import pylab as pl  
import random 

N = 20 # the length of sides of a grid
grid = pl.zeros([N+2,N+2]) # generate an empty grid to deal with boundary conditions
grid[1:(N+1),0] = pl.linspace(1,N,N) # label each boundary site with a number
grid[0,1:(N+1)] = pl.linspace(N+1,2*N,N) # label each boundary site with a number
grid[1:(N+1),N+1] = pl.linspace(2*N+1,3*N,N) # label each boundary site with a number
grid[N+1,1:(N+1)] = pl.linspace(3*N+1,4*N,N) # label each boundary site with a number
Percolation = pl.zeros([N,N]) # to record the grid we want
s = [0]*(N)+[N+1]*(N)+range(1,N+1)+range(1,N+1) # x coordinate of percolated sites
t = range(1,N+1)+range(1,N+1)+[0]*(N)+[N+1]*(N) # y coordinate of percolated sites
clusnum = 4*N # this is a counter. clusnum-4*N means how many sites have been occupied
Check = [1, 0, 0, 0] # a judgement
while pl.any(Check):
    Ranm = random.randint(0,N**2-1) # generate a random number
    x = Ranm/N+1 # xth-row
    y = Ranm%N+1# yth-column
    if grid[x,y] == 0: # check whether the site (x,y) is empty
        clusnum += 1 
        grid[x,y] = clusnum # put a point at site (x,y)
        Neighbor = [grid[x-1,y],grid[x+1,y],grid[x,y-1],grid[x,y+1]] # collect the mark numbers of all the four neighbors
        if max(grid[x-1,y],grid[x+1,y],grid[x,y-1],grid[x,y+1]): # check neighbering sites
            for (i,j) in zip(s, t): # if any neighboring site is occupied already, we sweep the grid
                if pl.any(Neighbor==grid[i,j]): # if the mark number of a site is equal to any mark number of the four neighbors
                    grid[i,j] = clusnum # update its mark number to the newest one, as a result we bridge clusters
        s.append(x) # since one more site is occupied, we record its coordinates in list s and t. 
        t.append(y)
    Check = [clusnum-max(grid[0,:]),clusnum-max(grid[N+1,:]),clusnum-max(grid[:,0]),clusnum-max(grid[:,N+1])]
    # this is a judgement to decide whether a spanning cluster is generated. 

for i in range(1,N+1):
    for j in range(1,N+1): # generate the grid we want
        if grid[i,j]: 
            Percolation[i-1,j-1]=(int)(grid[i,j]/clusnum) # if an occupied site is belong to the spanning cluster, we label it as 1, otherwise, 0
        else: 
            Percolation[i-1,j-1]=-1 # label empty sites as -1
pl.imshow(Percolation, interpolation='none', cmap='gist_yarg')
pl.title('Percolation N=%d' %N) 
pl.xlabel('x') 
pl.ylabel('y') 
pl.savefig('percolation_%d.pdf'%N) 
pl.show()
