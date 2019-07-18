#  O(1)
def solution(X, Y, K):
    distance = Y - X
    jumps_floor = distance // K
    jumps_rest = distance % K
    return jumps_floor if jumps_rest == 0 else jumps_floor + 1
