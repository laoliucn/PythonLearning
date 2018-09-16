# Given an unsorted integer array, find the smallest missing positive integer.
"""
Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1

Input: [1,3,6,4,1,2]
Output: 5

Input:[1,2,3]
Output: 4

Input: [-1,-2]
Output: 1

"""

A1 = [1, 2, 0]
A2 = [3, 4, -1, 1]
A3 = [7, 8, 9, 11, 12]
A4 = [1, 2, 3]
A5 = [-1, -2, -3]
A = [1, 3, 6, 4, 1, 2]

print(range(len(A)))

def solution(A):
    length = len(A)
    for i in range(length):
        while 0 < A[i] <= length and A[i] != A[A[i] - 1]:
            temp = A[i] - 1
            A[i], A[temp] = A[temp], A[i]

    for i in range(length):
        if A[i] != i+1:
            return i + 1

    return length+1


print(solution(A5))
