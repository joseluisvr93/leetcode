# 3. Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.
# Example 1:
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3.

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    max_len = 1
    start = 0
    end = 1
    while end < len(s):
        if s[end] not in s[start:end]:
            end += 1
        else:
            start += 1
        max_len = max(max_len, end - start)
    return max_len

s = "abcabcbb"
print(lengthOfLongestSubstring(s))
