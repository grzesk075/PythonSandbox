from typing import List

colors = ['green', 'red', 'blue']
for id, value in enumerate(colors):
    print(id, value)
    # 0 green
    # 1 red
    # 2 blue

l: List[int] = [1, -3, 4, 8, 'k']  # typing is nothing more than a comment
filteredList = [i for i, v in enumerate(l) if isinstance(l[i], int) and l[i] > 0]
print(filteredList, type(filteredList) == list)  # [0, 2, 3] True

print(any([False, 0, None, '']))  # False

print(7//3)  # 2 (like division of int in Java)
