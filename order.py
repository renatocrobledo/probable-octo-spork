
a = [
    'qwerqwtasg 4',
    'vcxbxcb 2',
    'fdsgsdg 5',
    'hshhash 6',
    'gdsg 1',
]


def order_by_last_int(element):
    return int(element.split().pop())


print(sorted(a, key=order_by_last_int))

