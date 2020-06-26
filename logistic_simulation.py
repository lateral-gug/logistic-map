import numpy as np
import pylab as pl

#diagramma di biforcazione

cycles = 100
points = 10**6
size = 0.1

r0 = np.random.uniform(2.95,4,points)
x0 = np.random.uniform(0,1,points)

def logisticmap(r,x):
    return r*x*(1-x)

def cyclic(r,x,n):
    for i in range(0,n):
        x = logisticmap(r,x)
    return x

conv = cyclic(r0,x0,cycles)

pl.figure(1)

pl.errorbar(r0,conv,fmt='.',color='black',markersize=size)
pl.xlabel('$r$')
pl.ylabel('$x_{%.0f}$'%(cycles))
pl.title('Diagramma di biforcazione')

#diagrammi di convergenza e di Moran

x = np.random.uniform(0,1,1)
r0 = np.random.uniform(2,4,1)
n = 100

pl.figure(2)

nvec = np.linspace(0,n-1,n)
iters = np.array([])
for i in range(0,n):
    iters = np.insert(iters,i,x)
    x = logisticmap(r0,x)

pl.errorbar(nvec,iters,fmt='.--',color='red',markersize=7)
pl.xlabel('$n$')
pl.ylabel('$x_n$')
pl.ylim(-0.1,1.1)
pl.grid(linestyle=':')
pl.title('Diagramma di convergenza')

pl.figure(3)

ax = np.linspace(-1,2,2)
xx = iters
for i in range(0,n):
    xx = np.insert(xx,2*i+1,iters[i])
yy = np.delete(xx,2*n-1)
yy = logisticmap(r0,yy)
yy = np.insert(yy,0,0)

camp = np.linspace(-1,2,1000)
pl.errorbar(xx,yy,fmt='.--',color='red',markersize=5)
pl.plot(camp,logisticmap(r0,camp),color='black',linestyle='-')
pl.grid(linestyle=':')
pl.plot(ax,0*ax,color='grey')
pl.plot(0*ax,ax,color='grey')
pl.plot(ax,ax,color='black',linestyle='-')
pl.xlim(-0.1,1.1)
pl.ylim(-0.1,1.1)
pl.title('Diagramma a ragnatela')

pl.show()

