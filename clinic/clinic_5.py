'''
Use sorted list, resort and hope sorting a mostly sorted list is fast.

Use a sorted list with a dict to store indexes.
Case 1: use bisect, insert element in order, update dict to store index
Case 2: use pop
Case 3: use dict to get index, then del list[index]
'''

from sys import stdin
# from heapq import heappush, heappop, heapify
from bisect import bisect

num_queries, K = map(int, input().split())
patients = []
patients_dict = {}

for i in range(num_queries):
    line = stdin.readline().strip().split()

    if line[0] == '1':
        priority = K * int(line[1]) - int(line[3])
        item = (priority, line[2])
        patients.append(item)
        patients.sort()
        patients_dict[line[2]] = (priority, line[2])

    elif line[0] == '2':
        if patients:
            print(patients.pop(0)[1])
        else:
            print('doctor takes a break')

    else:
        try:
            del_item = patients_dict.pop(line[2])
            del_ind = bisect(patients, del_item) - 1
            del patients[del_ind]
        except KeyError:
            # print('key error')
            pass
