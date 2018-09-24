"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


def if_palindrome(s):
    result = True

    length = len(s)
    i = 0
    j = length - 1
    for l in range(length // 2):

        if i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                result = False
                break
        else:
            break
    return result


"""
Approach 1: Longest Common Substring
Reverse S and become S' Find the longest common substring between S and S', which must also be the 
longest palindromic substring.

This seemed to work, let’s see some examples below.

For example, S = "caba", S'= "abac".

The longest common substring between S and S' is "aba", which is the answer.

Let’s try another example: S = "abacdfgdcaba", S' = "abacdgfdcaba".

The longest common substring between S and S' is "abacd". Clearly, this is not a valid palindrome.

Algorithm

We could see that the longest common substring method fails when there exists a reversed copy of 
a non-palindromic substring in some other part of SS. To rectify this, each time we find a longest 
common substring candidate, we check if the substring’s indices are the same as the reversed substring’s 
original indices. If it is, then we attempt to update the longest palindrome found so far; 
if not, we skip this and find the next candidate.

Refer to the link "https://blog.csdn.net/u010397369/article/details/38979077" about the longest common string.

This gives us an O(n^2) Dynamic Programming solution which uses O(n^2) space (could be improved to use O(n)O(n) space).
"""


def longest_palindrome1(s):
    reversed_string = s[::-1]
    length = len(s)

    longest_sub_len = 0
    max_end = 0

    # Generate a two dimension list
    temp = [[0] * length for k in range(length)]
    for i in range(length):
        for j in range(length):
            if s[i] == reversed_string[j]:
                if i > 0 and j > 0:
                    temp[i][i] = temp[i - 1][j - 1] + 1
                else:
                    temp[i][j] = 1
                if temp[i][j] > longest_sub_len:
                    before_reverse = length - 1 - j
                    if before_reverse + temp[i][j] - 1 == i:
                        longest_sub_len = temp[i][j]
                        max_end = i
            else:
                temp[i][j] = 0

    return s[max_end - longest_sub_len + 1: max_end + 1]


"""
Approach 2 Dynamic Programming
If we already knew that "bab" is a palindrome, it is obvious that "ababa" must be a palindrome since the two left and 
right end letters are the same.
P(i,j)=(P(i+1,j−1) and Si==Sj)
"""


def longest_palindrome2(s):
    n = len(s)
    result = ""
    dp = [[False] * n for i in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            dp[i][j] = (s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]))
            if dp[i][j] and j - i + 1 > len(result):
                result = s[i: j + 1]
    return result


"""
Approach 3: Expand Around Center
We observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center, 
and there are only 2n - 12n−1 such centers.

You might be asking why there are 2n - 12n−1 but not nn centers? The reason is the center of a palindrome can be in 
between two letters. Such palindromes have even number of letters (such as "abba") and its center are 
between the two 'b's.

"""


def expand_around_center(s: str, left: int, right: int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left = left - 1
        right = right + 1
    return right - left - 1


def longest_palindrome3(s: str) -> str:
    if not s:
        return ""
    start = 0
    end = 0
    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i + 1)
        length = max(len1, len2)
        if length > end - start:
            start = i - (length - 1) // 2
            end = i + length // 2
    return s[start:end + 1]


print(longest_palindrome3("babad"))
