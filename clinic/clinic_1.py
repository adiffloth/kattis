'''
Implement as list of tuples.
- Arrival: just append, don't try to maintain order.
- Doc ready: re-sort the list and pop.
- Remove: not implemented.

Too slow - fails with "Time Limit Exceeded".
'''

from sys import stdin

num_queries, K = map(int, input().split())
patients = []

for i in range(num_queries):
    line = stdin.readline().strip().split()

    if line[0] == '1':
        # print('patient arrival', end=': ')
        time, name, severity = int(line[1]), line[2], int(line[3])
        # print(time, name, severity)
        patients.append((0, name, time, severity))

    elif line[0] == '2':
        # print('doctor ready', end=': ')
        time = int(line[1])
        for j, patient in enumerate(patients):
            # print(patient)
            priority = patient[3] + (time - patient[2]) * K
            # priority = 200
            patients[j] = (priority, patient[1], patient[2], patient[3])
        # print(patients)
        patients.sort()
        if patients:
            print(patients.pop()[1])
        else:
            print('doctor takes a break')

    else:
        print('query of the third kind')
