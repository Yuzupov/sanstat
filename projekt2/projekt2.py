import numpy
import random

# amount of bootstraps
BOOTSTRAPS = 1000

# range, in floats since the means will be floats and makes comparisons more readable
A = -4.0
B = 6.0

# sample of ten observations:
originalObservations = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69]

# list of bootstrapped observations:
bootstrappedObservations = []

# samples are ten iid random variables from an unknown mu
# for given constraints a = -4 and b = 6
# we want to estimate following probability:
#
# p = P(a < (sum(Xi, 1, n)/n) - mu < b)
#

# Task 1: Explain how bootstrapping method can be used to estimate p,
# include pseudocode

'''
Bootstrapping can be used to make multiple samples from one original sample.
Through random selection of the first sample, new samples are created
and can be used to approximate the distribution of the sample mean.

sampleMean = mean(originalSample)

for _ in amountOfResamples
    bootstrappedSample = resample(originalSample)
    bootstrappedMean = mean(bootstrappedSample)
    adjustedMean = bootstrappedMean - sampleMean
    if a < adjustedMean < b
        success += 1
'''

# Task 2: estimate p with bootstrapping
#

# convert into a numpy array for redundancy
originalObservations = numpy.array(originalObservations)
# calculate the arithmetic mean of the array
sampleMean = numpy.mean(originalObservations)

for _ in range(BOOTSTRAPS):
    bootstrappedObservation = []
# method for resampling
# use random.choice() of the original sample to generate bootstrapped samples
# calculate the arithmetic mean of the bootstrapped sample and add to a list
    for _ in originalObservations:
        bootstrappedObservation.append(random.choice(originalObservations))
    bootstrappedObservationMean = numpy.mean(
        numpy.array(bootstrappedObservation)
    )
    bootstrappedObservations.append(bootstrappedObservationMean)
bootstrappedObservations = numpy.sort(bootstrappedObservations)

withinIntervalCounter = 0
for mean in bootstrappedObservations:
    if (A < (mean - sampleMean) < B):
        withinIntervalCounter += 1

# print the result
print(sampleMean)
proportionOfSuccess = withinIntervalCounter/BOOTSTRAPS
print(proportionOfSuccess)
