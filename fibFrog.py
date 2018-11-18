"""
https://app.codility.com/programmers/lessons/13-fibonacci_numbers/fib_frog/
The Fibonacci sequence is defined using the following recursive formula:

    F(0) = 0
    F(1) = 1
    F(M) = F(M - 1) + F(M - 2) if M >= 2
A small frog wants to get to the other side of a river. The frog is initially located at one bank of the river (position −1) and wants to get to the other bank (position N). The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci number. Luckily, there are many leaves on the river, and the frog can jump between the leaves, but only in the direction of the bank at position N.

The leaves on the river are represented in an array A consisting of N integers. Consecutive elements of array A represent consecutive positions from 0 to N − 1 on the river. Array A contains only 0s and/or 1s:

0 represents a position without a leaf;
1 represents a position containing a leaf.
The goal is to count the minimum number of jumps in which the frog can get to the other side of the river (from position −1 to position N). The frog can jump between positions −1 and N (the banks of the river) and every position containing a leaf.

For example, consider array A such that:

    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0
The frog can make three jumps of length F(5) = 5, F(3) = 2 and F(5) = 5.

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the minimum number of jumps by which the frog can get to the other side of the river. If the frog cannot reach the other side of the river, the function should return −1.

For example, given:

    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
"""
import functools


@functools.lru_cache()
def fibonacci(n):
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


# input
A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
B = [1, 1, 1, 1]
C = []
D = [0, 0, 1, 0, 1, 0, 0, 1]

def solution(A):
    length = len(A)
    if length == 0:
        return 1

    # This is the objective
    arrival = length + 1

    # Frog can only jump at the following distances, it is a set that composed by fibonacci numbers.
    jumps = set()
    for i in range(arrival):
        if fibonacci(i) <= arrival:
            jumps.add(fibonacci(i))

    # Frog can only jump on the position where has leaf.
    leaves_position = set(i + 1 for i in range(length) if A[i])
    leaves_position.add(arrival)  # Target shore need to be treated as a good leaf position as well.

    print(jumps)
    print(leaves_position)

    # With the first jump, only the following position could be reached.
    required_jumps = 1
    next_places = jumps & leaves_position

    # Loops until there is a place to go and we cannot reach the arrival.
    while next_places and arrival not in next_places:
        required_jumps += 1
        next_places = {place + jump
                       for place in next_places
                       for jump in jumps
                       if place + jump in leaves_position  # There is position for next step
                       if place + jump <= arrival  # A step cannot pass the arrival
                       }
    # We got the solution if the arrival is inside the set of places we can reach with next jump
    return required_jumps if arrival in next_places else -1


print(solution(D))
#print(solution(B))
#print(solution(C))
