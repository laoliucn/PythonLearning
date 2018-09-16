# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from extratypes import Tree  # library with types used in the task


def solution(T):
    # write your code in Python 3.6
    if T is None:
        return 0
    # root value
    root = T.x
    count = 0

    # Counting recursively
    count_left = solution(T.l, root);
    count_right = solution(T.r, root);

    return 1 + count_left + count_right;
