#  O(1)
def solution(X, Y, D):
    distance = Y - X
    jumps_floor = distance // D
    jumps_rest = distance % D
    return jumps_floor if jumps_rest == 0 else jumps_floor + 1
