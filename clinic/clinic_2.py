'''
Made the priority a fixed number rather than something that must be recalculated every time.
Implemented Case 3.

Main data structure is a heapq. Cases 1 and 2 use push and pop.
Case 3 uses a dict to help find the item in the heapq, but the actual
removal is done with a list.remove(). Then re-heapify.

Passes everything except the last three scenarios - time limit exceeded.
'''

from sys import stdin
from heapq import heappush, heappop, heapify

num_queries, K = map(int, input().split())
patients = []
patients_dict = {}

for i in range(num_queries):
    line = stdin.readline().strip().split()

    if line[0] == '1':
        priority = K * int(line[1]) - int(line[3])
        heappush(patients, (priority, line[2]))
        patients_dict[line[2]] = (priority, line[2])

    elif line[0] == '2':
        if patients:
            print(heappop(patients)[1])
        else:
            print('doctor takes a break')

    else:
        try:
            patients.remove(patients_dict.pop(line[2]))
        except KeyError:
            pass
        heapify(patients)
