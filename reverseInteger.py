"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when
the reversed integer overflows.
"""
import math


a = 123
b = -123
c = 120


def reverse(x):
    result = str()
    negative = False
    if x < 0:
        negative = True
    x = abs(x)
    xstring = str(x)
    for c in reversed(xstring):
        result += c
    if negative:
        result = '-' + result

    if -math.pow(2, 31) <= int(result) <= math.pow(2, 31) - 1:
        return int(result)
    else:
        return 0


print(reverse(a), reverse(b), reverse(c))
