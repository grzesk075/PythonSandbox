def solution(a):
    n = len(a)
    if n == 1:
        return a[0]
    a.sort()
    if a[0] != a[1]:
        return a[0]
    if a[-2] != a[-1]:
        return a[-1]
    for i in range(1, n - 2):
        if a[i - 1] != a[i] != a[i + 1]:
            return a[i]
