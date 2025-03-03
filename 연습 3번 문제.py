T = int(input())

a = list(map(int, input().split()))

EvenNum = 0 # 짝수
OodNum = 0  # 홀수

if len(a) != T:
    print("error")
else:
    r1 = [i for i in a if i % 2 == 0] # 짝수
    r2 = [i for i in a if i % 2 == 1] # 홀수

    EvenNum += len(r1)  # 짝수
    OodNum += len(r2)   # 홀수

    print(OodNum)
    print(EvenNum)

"""
for i in a:
    if i % 2 == 0:
        EvenNum += 1
    else:
        OodNum += 1
"""