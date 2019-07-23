def solution(A):
    N = len(A)
    existent = [False] * (N + 1)
    anyExistent = False
    for i in A:
        if i < 1 or i > N:
            continue
        existent[i] = True
        anyExistent = True
    if not anyExistent:
        return 1
    for i in range(1, N + 1):
        if existent[i] == False:
            return i
    return N + 1
