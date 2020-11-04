def swap(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]


in_str = input()
cups = [1, 0, 0]
for c in in_str:
    if c == 'A':
        swap(cups, 0, 1)
    elif c == 'B':
        swap(cups, 1, 2)
    elif c == 'C':
        swap(cups, 0, 2)
    else:
        raise ValueError('Bad input.')

print(cups.index(1) + 1)
