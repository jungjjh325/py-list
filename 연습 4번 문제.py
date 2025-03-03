T = int(input())

a = list(map(int, input().split()))

if len(a) != T:
    print("error")
else:
    n1 = min(a)
    n2 = max(a)
    print(n2 - n1)