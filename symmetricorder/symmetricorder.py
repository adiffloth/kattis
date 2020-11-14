from sys import stdin

num_lines = int(stdin.readline())
output = []
set_num = 1

while num_lines != 0:
    output.append(f'SET {set_num}')
    output.extend([0] * num_lines)
    for i in range(num_lines):
        line = input()
        if not i % 2:
            output[len(output) - num_lines + i // 2] = line
        else:
            output[len(output) - i // 2 - 1] = line

    num_lines = int(stdin.readline())
    set_num += 1

print('\n'.join(output))
