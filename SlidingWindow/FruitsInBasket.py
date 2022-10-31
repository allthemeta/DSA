'''
You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets,
and your goal is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

1. Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
2. You can start with any tree, but you can’t skip a tree once you have started.
3. You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both baskets.
'''

def fruitsInBasket(fruits):
    windowStart = 0
    maxLength = 0
    fruitFrequencey = {}

    #initial sweep to add fruit frequency to dictionary
    for windowEnd in range(len(fruits)):
        rightFruit = fruits[windowEnd]
        if rightFruit not in fruitFrequencey:
            fruitFrequencey[rightFruit] = 0
        fruitFrequencey[rightFruit] += 1

        #Shrink window now until length of dictionary in equal to 2
        while len(fruitFrequencey) > 2:
            leftFruit = fruits[windowStart]
            fruitFrequencey[leftFruit] -= 1
            if fruitFrequencey[leftFruit] == 0:
                del fruitFrequencey[leftFruit]
            windowStart += 1
        maxLength = max(maxLength, windowEnd - windowStart + 1)
    return maxLength


def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
