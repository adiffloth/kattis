input()
answers = list(input())
ad_ans = ['A', 'B', 'C']
br_ans = ['B', 'A', 'B', 'C']
go_ans = ['C', 'C', 'A', 'A', 'B', 'B']

ad_correct = 0
br_correct = 0
go_correct = 0

for i, answer in enumerate(answers):
    if answer == ad_ans[i % 3]:
        ad_correct += 1
    if answer == br_ans[i % 4]:
        br_correct += 1
    if answer == go_ans[i % 6]:
        go_correct += 1

max_correct = max(ad_correct, br_correct, go_correct)
print(max_correct)
if ad_correct == max_correct:
    print('Adrian')
if br_correct == max_correct:
    print('Bruno')
if go_correct == max_correct:
    print('Goran')
