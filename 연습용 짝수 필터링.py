"""
T, X = map(int, input().split())

a = list(map(int, input().split()))

r = [i for i in a if i % X == 0]

print(*r)
"""
T = int(input())

a = list(map(int, input().split()))

r = [i for i in a if i % 2 == 0]

print(*r)