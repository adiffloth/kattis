'''
Go back to heapq.
Use dict to track removes, but don't change the heapq.
On pop, check the dict to see if it has been removed already.
'''

from sys import stdin
from heapq import heappush, heappop

K = int(stdin.readline().split()[1])
patients = []
patients_dict = {}

for query in stdin:
    line = query.split()

    if line[0] == '1':
        priority = K * int(line[1]) - int(line[3])
        heappush(patients, (priority, line[2]))
        patients_dict[line[2]] = (priority, line[2])

    elif line[0] == '2':
        if patients:
            p = heappop(patients)
            while not patients_dict.pop(p[1], None):
                p = heappop(patients)
            print(p[1])
        else:
            print('doctor takes a break')

    else:
        patients_dict.pop(line[2], None)
