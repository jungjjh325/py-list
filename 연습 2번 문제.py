T, X = map(int, input().split())

a = list(map(int, input().split()))

if len(a) != T:
    print("error")
else:
    r = [i for i in a if i > X]

    print(*r)