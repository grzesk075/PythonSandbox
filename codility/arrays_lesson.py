a = [0] * 5
assert (len(a) == 5)
a += 'string'  # appends each char separately
a += ['string']
del (a[-7:-1])  # remove chars from a += 'string'
a.append(None)
a.reverse()
a[3] = 3


def sort_key(item):
    if item is None:
        return -2
    elif isinstance(item, str):
        return -1
    elif isinstance(item, int):
        return item
    return 0


a.sort(key=sort_key, reverse=True)

if __name__ == '__main__':
    print(a)
