import numpy
import random
from tabulate import tabulate
import matplotlib.pyplot as plt

listOfPlatonicSolids = [4, 6, 8, 12, 20]
listOfDiscreteProbs = []
resultList = []
differentTrials = [10, 100, 1000, 10000, 100000, 1000000]
dictWithProbabilites = {}
dictOfDice = {}
win = 0
numOfTrials = 100000

# Below for loop populates a dictionary with probabilites. The key of the dict
# corresponds to the size of the die and the value at the key is a list
# with probability of a specific side facing up
for i in listOfPlatonicSolids:
    tempList = []
    for j in range(0, i):
        tempList.append(1)
        tempList[j] = tempList[j]/i
    dictWithProbabilites[i] = tempList

# below loop populates a dictionary with the value of each face.
# unlike the above function it has a list with the value of each face
# as opposed to the probability
for i in listOfPlatonicSolids:
    dictOfDice[i] = list(range(1, i+1))


def main():
    # main loop, allows for user input
    while True:
        print("Pick which task you want to run the code for:")
        pickTask = int(input())
        if pickTask >= 1 or pickTask <= 5:
            match pickTask:
                case 1:
                    task1()
                case 2:
                    task2()
                case 3:
                    task3()
                case 4:
                    task4()
                case 5:
                    task5()


def task1():
    global listOfDiscreteProbs, dictWithProbabilites, listOfPlatonicSolids
    listOfDiscreteProbs = dictWithProbabilites[listOfPlatonicSolids[0]]
    for i in listOfPlatonicSolids[1:]:
        listOfDiscreteProbs = numpy.convolve(listOfDiscreteProbs, dictWithProbabilites[i])
    print("s", "P(S=s)")
    for i in range(46):
        print(str(i+5), listOfDiscreteProbs[i])
    total_probability = sum(listOfDiscreteProbs)
    print("Total Probability:", total_probability)
    return


def task2():
    global win, listOfDiscreteProbs
    # Probability of winning one game
    win = sum(listOfDiscreteProbs[:6]) + sum(listOfDiscreteProbs[-6:])
    print(f"Probability of winning the game: {win:.5f}")
    return


def task3():
    counter = 0
    for _ in range(numOfTrials):
        res = 0
        res += random.randint(1, len(dictOfDice[4]))
        res += random.randint(1, len(dictOfDice[6]))
        res += random.randint(1, len(dictOfDice[8]))
        res += random.randint(1, len(dictOfDice[12]))
        res += random.randint(1, len(dictOfDice[20]))
        if res <= 10 or res >= 45:
            counter += 1
    print(f"Probability of winning the game with 1000 trials: {counter/numOfTrials:.5f}")
    return


def task4():
    counter = 0
    k = 0
    for i in differentTrials:
        k = i
        counter = 0
        for _ in range(i):
            res = 0
            res += random.randint(1, len(dictOfDice[4]))
            res += random.randint(1, len(dictOfDice[6]))
            res += random.randint(1, len(dictOfDice[8]))
            res += random.randint(1, len(dictOfDice[12]))
            res += random.randint(1, len(dictOfDice[20]))
            if res <= 10 or res >= 45:
                counter += 1
        resultList.append(counter/i)
    print(resultList)
    print(f"Probability of winning the game with {k} trials: {counter/k:.5f}")
    return


def task5():
    plt.plot(differentTrials, resultList, marker='o')
    plt.xscale('log')
    plt.xlabel('Number of Trials')
    plt.ylabel('Probability of winning')
    plt.axhline(y=win, color='r', linestyle='-')
    plt.axhline(y=win*0.90, color='g', linestyle='-')
    plt.axhline(y=win*1.10, color='g', linestyle='-')
    plt.title('Probability of winning the game')
    plt.show()
    return


main()
