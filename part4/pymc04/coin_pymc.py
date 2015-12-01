import pymc as pm
import numpy as np 
#import pylab import hist, show 

f1=open('z15N50.csv','r')
L1=[float(ii) for ii in f1]
n=len(L1)

mint =pm.Beta('Mint',alpha=1,beta=1)
coin0=pm.Bernoulli('coin01',p=mint,value=L1,observed=True)

M0=pm.Model([mint,coin0])
M=pm.MCMC(M0)
M.sample(iter=10000,burn=1000,thin=10)

M.summary() 
pm.Matplot.plot(M)
