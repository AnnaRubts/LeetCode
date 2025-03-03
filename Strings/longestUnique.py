
def lengthOfLongestSubstring(s):
    last_positions = {}
    max_substring = 0
    counter = 0
    for i,c in enumerate(s):
        if c in last_positions:
            last_i = last_positions[c]
            last_positions[c] = i #update position
            counter = i - last_i
        else:
            last_positions[c] = i
            counter += 1
            max_substring = max(max_substring, counter)
    return max_substring