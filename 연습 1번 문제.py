T = int(input())

a = list(map(int, input().split()))

if len(a) != T:
    print("error")
else:
    r = [i for i in a if i % 2 == 0]

    print(*r)