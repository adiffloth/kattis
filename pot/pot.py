sum = 0
for _ in range(int(input())):
    line = input()
    sum += int(line[:-1]) ** int(line[-1])

print(sum)
