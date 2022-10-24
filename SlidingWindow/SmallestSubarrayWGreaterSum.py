'''
Given an array of positive integers and a number ‘S,’
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
Return 0 if no such subarray exists.
'''

import math


def smallest_subarray_sum(s, arr):
    minLen = math.inf
    windowSum = 0
    windowStart = 0
    for windowEnd in range(lend(arr)):
        windowSum += arr[windowEnd]
        while windowSum >= s:
            minLen = min(minLen, windowEnd - windowStart + 1)
            windowSum -= arr[windowStart]
            windowStart += 1
    if minLen == math.inf:
        return 0
    return minLen

def main():
  print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [2, 1, 5, 2, 3, 2])))


main()
