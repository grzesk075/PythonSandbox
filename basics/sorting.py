class MyItem:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def __str__(self):
        return "MyItem of " + str(self.value)


my_list = [MyItem(9), MyItem(2)]

sorted_list = sorted(my_list)
copied_list = sorted_list.copy()

print(MyItem(5))
print('Sorted list: ', sorted_list)

(a, b, c, _) = list(range(4))
print(a)
print(b)
print(c)
