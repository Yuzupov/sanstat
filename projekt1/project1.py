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
import random
import matplotlib.pyplot as plt

listOfPlatonicSolids = [4, 6, 8, 12, 20]
dictWithProbabilites = {}
numOfTrials = 100000
dictOfDice = {}

# This for loop does about the same as the previous one but instead of having
# the literal value of the face, it shows the probability of a face landing up

for i in listOfPlatonicSolids:
    tempList = []
    for j in range(0, i):
        tempList.append(1)
        tempList[j] = tempList[j]/i

    dictWithProbabilites[i] = tempList

listOfDiscreteProbs = dictWithProbabilites[listOfPlatonicSolids[0]]
for i in listOfPlatonicSolids[1:]:
    listOfDiscreteProbs = numpy.convolve(listOfDiscreteProbs, dictWithProbabilites[i])


for i in listOfPlatonicSolids:
    dictOfDice[i] = list(range(1, i+1))

for item in listOfDiscreteProbs:
    print(item)



total_probability = sum(listOfDiscreteProbs)
print("Total Probability:", total_probability)



# Probability of winning
win = sum(listOfDiscreteProbs[:6]) + sum(listOfDiscreteProbs[-6:])
print(f"Probability of winning the game: {win:.5f}")


#Task 3
counter = 0
for i in range(numOfTrials):
    res = 0
    res += random.randint(1, len(dictOfDice[4]))
    res += random.randint(1, len(dictOfDice[6]))
    res += random.randint(1, len(dictOfDice[8]))
    res += random.randint(1, len(dictOfDice[12]))
    res += random.randint(1, len(dictOfDice[20]))
    if res <= 10 or res >= 45:
        counter += 1

print(f"Probability of winning the game with 1000 trials: {counter/numOfTrials:.5f}")

differentTrials = [10, 100, 1000, 10000, 100000, 1000000]
resultList = []

for i in differentTrials:
    counter = 0
    for j in range(i):
        res = 0
        res += random.randint(1, len(dictOfDice[4]))
        res += random.randint(1, len(dictOfDice[6]))
        res += random.randint(1, len(dictOfDice[8]))
        res += random.randint(1, len(dictOfDice[12]))
        res += random.randint(1, len(dictOfDice[20]))
        if res <= 10 or res >= 45:
            counter += 1
    resultList.append(counter/i)
    #print(f"Probability of winning the game with {i} trials: {counter/i:.5f}")

plt.plot(differentTrials, resultList, marker='o')
plt.xscale('log')
plt.xlabel('Number of Trials')
plt.ylabel('Probability of winning')
plt.axhline(y=win, color='r', linestyle='-')
plt.axhline(y=win*0.90, color='g', linestyle='-')
plt.axhline(y=win*1.10, color='g', linestyle='-')
plt.title('Probability of winning the game')
plt.show()

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