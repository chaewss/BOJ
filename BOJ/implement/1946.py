import sys

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    rank = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    rank_asc = sorted(rank)
    top, result = 0, 1

    for i in range(1, len(rank)):
        if rank_asc[i][1] < rank_asc[top][1]:
            top = i
            result += 1
    print(result)
