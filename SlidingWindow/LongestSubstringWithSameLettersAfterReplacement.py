def length_of_longest_substring(str1, k):
    start, maxLength, maxRepeating, freq = 0, 0, 0, {}

    # Initial roll through to populate the dictionary.
    for end in range(len(str1)):
        rightChar = str1[end]
        if rightChar not in freq:
            freq[rightChar] = 0
        freq[rightChar] += 1

        #update the max repeating
        maxRepeating = max(maxRepeating, freq[rightChar])

        # Current window size is from window_start to window_end, overall we have a letter which is
        # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
        # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
        # if the remaining letters are more than 'k', it is the time to shrink the window as we
        # are not allowed to replace more than 'k' letters
        if (end - start + 1 - maxRepeating) > k:
            leftChar = str1[start]
            freq[leftChar] -= 1
            start += 1

        maxLength = max(maxLength, end - start + 1)
    return maxLength
