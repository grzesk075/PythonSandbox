def solution(A, K):
    length = len(A)
    if length <= 1 or K % length == 0:
        return A

    def _destination_index(idx):
        return (idx + K) % length

    rotated_A = A.copy()
    for i in range(length):
        rotated_A[_destination_index(i)] = A[i]

    return rotated_A
