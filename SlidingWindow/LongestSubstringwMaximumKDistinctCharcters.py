''' Given a string, find the length of the longest substring in it with no more than K distinct characters. '''
def longest_substring_with_k_distinct(str1, k):
    windowStart = 0
    maxLength = 0
    charFrequency = {}

    # in the following loop we will extend the window.
    for windowEnd in range(len(str1)):
        rightChar = str1[windowEnd]
        if rightChar not in charFrequency:
            charFrequency[rightChar] = 0
            charFrequency[rightChar] += 1

        # shrink the sliding window, until we are left with 'k' distnct characters in the charFrequency
        while len(charFrequency) > k:
            leftChar = str1[windowStart]
            charFrequency[leftChar] -= 1
            if charFrequency[leftChar] == 0:
                del charFrequency[leftChar]
            windowStart += 1 #Shrink the window
        maxLength = max(maxLength, windowEnd-windowStart+1)
    return maxLength


def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
