"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def length_of_longest_substring(s):
    result = []
    best = []
    if len(s) == 1:
        return 1
    for char in s:
        if char in result:
            index = result.index(char)
            result = result[index+1:]
        result.append(char)
        if len(best) < len(result):
            best = list(result)
    return len(best)




print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring(("bbbbb")))
print(length_of_longest_substring(("pwwkew")))
