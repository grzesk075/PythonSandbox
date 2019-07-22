def solution(A):
    N = len(A)
    existent = [False] * (N + 2)
    for i in A:
        existent[i] = True
    for v in range(1, N + 2):
        if existent[v] == False:
            return v
    assert False
