def solution(N):
    gap, max_gap = 0, 0
    binary_string = '{0:b}'.format(N)
    for v in binary_string:
        if v == '0':
            gap += 1
        else:
            if gap > max_gap:
                max_gap = gap
            gap = 0
    return max_gap

if __name__ == '__main__':
    print(solution(0))
    print(solution(1))
    print(solution(2))
    print(solution(3))
    print(solution(4))
    print(solution(5))
    print(solution(6))
    print(solution(7))
    print(solution(8))
    print(solution(9))
    print(solution(1041))
    print(solution((1 << 31) - 1))
