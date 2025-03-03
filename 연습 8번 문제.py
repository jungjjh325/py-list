T = int(input())

a = list(map(int, input().split()))

F = int(input())

if len(a) != T:
    print("error")
else:
    print(a.count(F))