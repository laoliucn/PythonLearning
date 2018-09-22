A = [10, 2, 5, 1, 8, 20]
sample1 = [6, 1, 6, 5, 8, 4]
sample2 = [2, 20, 7, 55, 1, 33, 12, 4]
sample3 = [33, 6, 20, 1, 8, 12, 5, 55, 4, 9]


def solution(A):
    max_peri = 0
    n = len(A)
    A.sort(reverse=True)

    for i in range(0, n - 2):
        if A[i] < (A[i + 1] + A[i + 2]):
            max_peri = max(max_peri, A[i] + A[i + 1] + A[i + 2])
            break
    if max_peri == 0:
        return -1
    else:
        return max_peri


print(solution(A))
print(solution(sample1))
print(solution(sample2))
print(solution(sample3))
