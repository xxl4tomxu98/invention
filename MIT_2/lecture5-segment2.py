# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 11:09:36 2016

@author: guttag
"""

import random
random.seed(0)
 
def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])
 
def testRoll(n = 10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)


def runSim(goal, numTrials):
    """simulation approach to find the probability of one outcome, 'goal'
        in all trials, compare to actual statistical method"""
    total = 0
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDie())
        if result == goal:
            total += 1
    print('Actual probability =',
          round(1/(6**len(goal)), 8)) 
    estProbability = round(total/numTrials, 8)
    print('Estimated Probability  =',
          round(estProbability, 8))
    
#runSim('11111', 1000000)

def fracBoxCars(numTests):
    """simulate probability of two trials both turn out to be 6"""
    numBoxCars = 0
    for i in range(numTests):
        if rollDie() == 6 and rollDie() == 6:
            numBoxCars += 1
    return numBoxCars/numTests
print('Actual probability of double 6 =',
          str(round((1/6**2),8)*100) + '%')    
#print('Estimated Frequency of double 6 =',
      str(fracBoxCars(10000000)*100) + '%')
