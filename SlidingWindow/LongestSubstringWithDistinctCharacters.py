def non_repeat_substring(str1):
    windowStart, maxLength, indexMap = 0, 0, {}
    for windowEnd in range(len(str1)):
        rightChar = str1[windowEnd]
        if rightChar in indexMap:
            windowStart = max(windowStart, indexMap[rightChar] + 1)
        indexMap[rightChar] = windowEnd
        maxLength = max(maxLength, windowEnd - windowStart + 1)
    return maxLength



def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()
