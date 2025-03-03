T = int(input())

a = list(map(int, input().split()))

if len(a) != T:
    print("error")

else:
    b = sorted(set(a))

    print(*b)