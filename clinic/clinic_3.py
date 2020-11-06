'''

'''
# TODO: Read the file in all at once.

from sys import stdin
# from heapq import heappush, heappop, heapify

num_queries, K = map(int, input().split())
patients = []
d = {}

for i in range(num_queries):
    line = stdin.readline().strip().split()

    if line[0] == '1':
        priority = K * int(line[1]) - int(line[3])
        d[line[2]] = (priority, line[2])

    elif line[0] == '2':
        if d:
            print(d.pop(min(d, key=d.get), None)[1])
        else:
            print('doctor takes a break')

    else:
        if d:
            d.pop(line[2], None)
