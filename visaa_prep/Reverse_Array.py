n=int(input())
arr=list(map(int, input().split()))
reversed_arr=arr[::-1]
for n in reversed_arr:
    print(n, end=" ")
