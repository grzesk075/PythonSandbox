def solution(A):
    A.sort()
    occurrences_count = 0
    previous_v = None
    for v in A:
        if previous_v == v:
            occurrences_count += 1
        elif occurrences_count % 2 == 1:
            return previous_v
        else:
            occurrences_count = 1
            previous_v = v
    return previous_v
