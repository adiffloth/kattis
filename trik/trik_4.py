ball = 1
for move in input():
    if move == 'A' and ball != 3:
        ball = 3 - ball
    elif move == 'B' and ball != 1:
        ball = 5 - ball
    elif move == 'C' and ball != 2:
        ball = (ball + 2) % 4

print(ball)
