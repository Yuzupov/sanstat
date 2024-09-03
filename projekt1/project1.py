'''
Notes from background knowledge part of the assignment for easier referencing

distribution of a sum of two independent discrete random variables S = X + Y
can be determined through:
    if S = s and X 0 i, then Y = s - i, since X and Y are independent
    the probability is a long fucking expression

By adding up all the possible values for i, we obtain the probability of
S = s as follows:
    P(S = s) = pfS(s) = SIGMApfX(s-i)pfY(i)

The above sum is called a convoloution sum. The operation of convolution is
usually denoted by an asterisk such that
pfS(s) = (pfX * pfX)(s)
convolution of two independent random variables X and Y following
binominal distributions:

    X e Bin(5, 0.3)
    Y e Bin(8, 0.6)
    S = X + Y

    if we have more than two random variables we obtain the probability of
    the third by taking the convolution sum of the first two, and use that
    as a parameter for the second convolution sum

    python specific is "numpy.convolve"
'''

listToTurnIntoTupleOfPolygons = []
dictTableFromProbabilityFunction = {}
for i in range(5, 51):
    dictTableFromProbabilityFunction[i] = 0

for i in range(3, 51):
    listToTurnIntoTupleOfPolygons.append(i)

tupleOfPolygons = tuple(listToTurnIntoTupleOfPolygons)

dictWithTuplesAsKeys = dict.fromkeys(tupleOfPolygons, None)


print(f'\ntable from probability function {dictTableFromProbabilityFunction}\n')
print(f'\ndict with tuples {dictWithTuplesAsKeys}\n')
print(f'\ntuple of polygons {tupleOfPolygons}\n')
