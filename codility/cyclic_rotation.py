def solution(A, N):
    length = len(A)
    if length <= 1 or N % length == 0:
        return A

    def _destination_index(idx):
        return (idx + N) % length

    value = A[0]
    destination_index = _destination_index(0)
    for i in range(length):
        buffer = A[destination_index]
        A[destination_index] = value
        value = buffer
        destination_index = _destination_index(destination_index)

    return A
