from matplotlib import pyplot as plt
import random
import traceback
from enum import Enum

class Coin(Enum):
    HEAD = 0
    TAIL = 1

class Trials(Enum):
    FIRST = 10
    SECOND = 100
    THRID = 100_000
    FOURTH = 1_000_000

def drawGraph(firstList, secondList, thirdList, fourthList):
    headsAndTailsLists = []
    # labels = ['Heads', 'Tails']
    listOfNumbers = [firstList, secondList, thirdList, fourthList]

    figure = plt.figure()

    graphOne = figure.add_subplot(221)
    graphTwo = figure.add_subplot(222)
    graphThree = figure.add_subplot(223)
    graphFour = figure.add_subplot(224)

    for number in listOfNumbers:

        count = []

        headsCnt = number.count('HEAD')
        tailsCnt = number.count('TAIL')
        count.append(headsCnt)
        count.append(tailsCnt)

        headsAndTailsLists.append(count)

    numBars = len(headsAndTailsLists[0])
    positions = range(1,numBars+1)

    graphOne.barh(positions, headsAndTailsLists[0], align = 'center')
    graphTwo.barh(positions, headsAndTailsLists[1], align = 'center')
    graphThree.barh(positions, headsAndTailsLists[2], align = 'center')
    graphFour.barh(positions, headsAndTailsLists[3], align = 'center')

    # graphOne.yticks(positions, labels)
    # graphTwo.yticks(positions, labels)
    # graphThree.yticks(positions, labels)
    # graphFour.yticks(positions, labels)

    plt.grid()
    plt.show()


def flipCoin():
    result = random.randint(0, 1)
    return(result)

#def getLists()

def doTrials(times):
    counter = 0
    trialList = []

    while((counter:=counter+1)<times):
        trialList.append(Coin(flipCoin()).name)
    
    return(trialList)


if __name__ == "__main__":
    try:
        firstList = (doTrials(Trials.FIRST.value))
        secondList = (doTrials(Trials.SECOND.value)) 
        thirdList = (doTrials(Trials.THRID.value))
        fourthList = (doTrials(Trials.FOURTH.value))

        drawGraph(firstList,secondList,thirdList,fourthList)


    except Exception as error:
        traceback.print_exc()


    finally:
        print(f':)')