in_str = input()
ret = 1
for c in in_str:
    if c == 'A':
        if ret == 1:
            ret = 2
        elif ret == 2:
            ret = 1
    elif c == 'B':
        if ret == 2:
            ret = 3
        elif ret == 3:
            ret = 2
    else:
        if ret == 1:
            ret = 3
        elif ret == 3:
            ret = 1

print(ret)
