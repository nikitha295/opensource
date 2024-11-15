t=int(input())
for _ in range(t):
    n,m=map(int, input().split())
    if n>m:
        result = n-m
    else:
        result = 0
    print(result)
