def find_averages_of_subarrays(k, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] # add the next element.
        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if windowEnd >= k - 1:
            result.append(windowSum/k)
            windowSum -= arr[windowStart]
            windowStart += 1
    return results


def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()
