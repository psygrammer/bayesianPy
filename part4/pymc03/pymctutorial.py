"""
PyMC Tutorial
"""

from pymc import DiscreteUniform, Exponential, Deterministic, Poisson, Uniform
import numpy as np
from pymc.examples import disaster_model as dm

print("sp p: ",dm.switchpoint.parents)
print("d p: ", dm.disasters.parents)
print("r c: ", dm.rate.children)

print("da len: ", len(dm.disasters_array))

print("d v: ", dm.disasters.value)
print("d: ", dm.disasters)

print("sp v: ", dm.switchpoint.value)
print("em v: ", dm.early_mean.value)
print("lm v: ", dm.late_mean.value)
print("r v: ", dm.rate.value)

print("sp logp: ", dm.switchpoint.logp)
print("d logp: ", dm.disasters.logp)
print("em logp: ", dm.early_mean.logp)
print("lm logp: ", dm.late_mean.logp)

print("sp p v: ",dm.switchpoint.parents.value)
print("d p v: ", dm.disasters.parents.value)
# print("r c v: ", dm.rate.children.value)

from pymc import MCMC
from pylab import hist, show
from pymc.Matplot import plot
from pymc import Metropolis

def analizeM():
	M = MCMC(dm)
	print("M: ", M)

	M.sample(iter=10000, burn=1000, thin=10)
	print("M t: ", M.trace('switchpoint')[:])

	hist(M.trace('late_mean')[:])
	# show()

	plot(M)
	# show()

	print("M smd dm sp: ", M.step_method_dict[dm.switchpoint])
	print("M smd dm em: ", M.step_method_dict[dm.early_mean])
	print("M smd dm lm: ", M.step_method_dict[dm.late_mean])

	M.use_step_method(Metropolis, dm.late_mean, proposal_sd=2.)

analizeM()

x = np.array([ 4, 5, 4, 0, 1, 4, 3, 4, 0, 6, 3, 3, 4, 0, 2, 6,
3, 3, 5, 4, 5, 3, 1, 4, 4, 1, 5, 5, 3, 4, 2, 5,
2, 2, 3, 4, 2, 1, 3, None, 2, 1, 1, 1, 1, 3, 0, 0,
1, 0, 1, 1, 0, 0, 3, 1, 0, 3, 2, 2, 0, 1, 1, 1,
0, 1, 0, 1, 0, 0, 0, 2, 1, 0, 0, 0, 1, 1, 0, 2,
3, 3, 1, None, 2, 1, 1, 1, 1, 2, 4, 2, 0, 0, 1, 4,
0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1])

import disaster_model_with_missing as dmwm

def analizeMwm():
	masked_values = np.ma.masked_equal(x, value=None)
	print("m v: ", masked_values)

	print("dmwm da: ", dmwm.disasters_array)

	Mwm = MCMC(dmwm)
	Mwm.sample(iter=10000, burn=1000, thin=10)

	print("Mwm t: ", Mwm.trace('switchpoint')[:])

	hist(Mwm.trace('late_mean')[:])
	# show()

	plot(Mwm)
	# show()

# analizeMwm()

# show()
