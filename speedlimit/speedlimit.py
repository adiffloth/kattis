i = int(input())
while i != -1:
    dist_traveled = 0
    prev_time = 0
    for _ in range(i):
        speed, time = map(int, input().split())
        elapsed_time = time - prev_time
        prev_time = time
        dist_traveled += speed * elapsed_time
    i = int(input())

    print(f'{str(dist_traveled)} miles')
