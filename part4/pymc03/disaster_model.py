"""
A model for the disasters data with a changepoint

changepoint ~ U(0, 110)
early_mean ~ Exp(1.)
late_mean ~ Exp(1.)
disasters[t] ~ Po(early_mean if t <= switchpoint, late_mean otherwise)

"""

from pymc import *
from numpy import array, empty
from numpy.random import randint

__all__ = [
    'disasters_array',
    'switchpoint',
    'early_mean',
    'late_mean',
    'rate',
    'disasters']

disasters_array = array([4, 5, 4, 0, 1, 4, 3, 4, 0, 6, 3, 3, 4, 0, 2, 6,
                         3, 3, 5, 4, 5, 3, 1, 4, 4, 1, 5, 5, 3, 4, 2, 5,
                         2, 2, 3, 4, 2, 1, 3, 2, 2, 1, 1, 1, 1, 3, 0, 0,
                         1, 0, 1, 1, 0, 0, 3, 1, 0, 3, 2, 2, 0, 1, 1, 1,
                         0, 1, 0, 1, 0, 0, 0, 2, 1, 0, 0, 0, 1, 1, 0, 2,
                         3, 3, 1, 1, 2, 1, 1, 1, 1, 2, 4, 2, 0, 0, 1, 4,
                         0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1])

# Define data and stochastics

switchpoint = DiscreteUniform(
    'switchpoint',
    lower=0,
    upper=110,
    doc='Switchpoint[year]')
early_mean = Exponential('early_mean', beta=1.)
late_mean = Exponential('late_mean', beta=1.)

@deterministic(plot=False)
def rate(s=switchpoint, e=early_mean, l=late_mean):
    ''' Concatenate Poisson means '''
    out = empty(len(disasters_array))
    out[:s] = e
    out[s:] = l
    return out

disasters = Poisson('disasters', mu=rate, value=disasters_array, observed=True)
