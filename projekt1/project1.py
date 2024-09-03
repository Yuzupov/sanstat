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
import numpy

tupleOfPlatonicSolids = (4, 6, 8, 12, 20)
dictWithProbabilites = {}
dictOfDice = {}

# The for loop below creates a dictionary where the key is the amount
# of sides the shape has. The value is a list containing the possible value
# for each of the faces

for i in tupleOfPlatonicSolids:
    dictOfDice[i] = list(range(1, i+1))

# This for loop does about the same as the previous one but instead of having
# the literal value of the face, it shows the probability of a face landing up

for i in tupleOfPlatonicSolids:
    tempList = []
    for j in range(0, i):
        tempList.append(1)
        tempList[j] = tempList[j]/i

    dictWithProbabilites[i] = tempList


# For the actual rolling we are supposed to assume all 5 dice are rolled
# (which is why the lowest score we can get is 5 i.e. all dice face up with 1)
# and why the highest score is 50 i.e. 20 + 12 + 8 + 6 + 4


def task1():
    return


def task2():
    return


def task3():
    return


def task4():
    return


def task5():
    return


print(f'\nprobabilites of each platonic solid: {dictWithProbabilites}\n')
print(f'\ntable from probability function {dictOfDice}\n')
