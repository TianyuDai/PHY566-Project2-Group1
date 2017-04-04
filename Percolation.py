import pylab as pl  
import random 

N = 80 # the length of sides of a grid
grid = pl.zeros([N+2,N+2]) # generate an empty grid
grid[1:(N+1),0] = pl.linspace(1,N,N) # boundary condition
grid[0,1:(N+1)] = pl.linspace(N+1,2*N,N)
grid[1:(N+1),N+1] = pl.linspace(2*N+1,3*N,N)
grid[N+1,1:(N+1)] = pl.linspace(3*N+1,4*N,N)
Percolation = pl.zeros([N,N])
s = [0]*(N)+[N+1]*(N)+range(1,N+1)+range(1,N+1) # x coordinate of percolated sites
t = range(1,N+1)+range(1,N+1)+[0]*(N)+[N+1]*(N) # y coordinate of percolated sites
clusnum = 4*N
Check = [1, 0, 0, 0]
while pl.any(Check):
    Ranm = random.randint(0,N**2-1) # generate a random number
    x = Ranm/N+1 # xth-row
    y = Ranm%N+1# yth-column
    s.append(x)
    t.append(y)
    if grid[x,y] == 0: # check whether the site (x,y) is empty
        clusnum += 1
        grid[x,y] = clusnum # put a point at site (x,y)
        Neighbor = [grid[x-1,y],grid[x+1,y],grid[x,y-1],grid[x,y+1]]
        if max(grid[x-1,y],grid[x+1,y],grid[x,y-1],grid[x,y+1]): # check neighbering sites
            for (i,j) in zip(s, t): 
                if pl.any(Neighbor==grid[i,j]):
                    grid[i,j] = clusnum
    Check = [clusnum-max(grid[0,:]),clusnum-max(grid[N+1,:]),clusnum-max(grid[:,0]),clusnum-max(grid[:,N+1])]

counter = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        Percolation[i-1,j-1]=grid[i,j]         
pl.imshow(Percolation, cmap='gist_yarg')
pl.title('Percolation N=%d' %N) 
pl.xlabel('x') 
pl.ylabel('y') 
pl.savefig('percolation_7.pdf') 
pl.show()
