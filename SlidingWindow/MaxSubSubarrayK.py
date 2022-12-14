'''
Given an array of positive numbers and a positive number âk,â
find the maximum sum of any contiguous subarray of size âkâ.
'''

def max_sub_array_of_size_k(k, arr):
    maxSum, windowSum, windowStart = 0, 0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if windowEnd >= k-1:
            maxSum = max(maxSum, windowSum)
            maxSum -= arr[windowStart]
            windowStart += 1
    return maxSum


def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()
