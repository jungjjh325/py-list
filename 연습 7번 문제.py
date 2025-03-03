T = int(input())

a = list(map(int, input().split()))

F = int(input())

if len(a) != T:
    print("error")
else:
    if F in a:
        print(a.index(F) + 1)
    else:
        print(-1)


