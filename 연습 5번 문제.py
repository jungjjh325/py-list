"""
T = int(input())

a = list(map(int, input().split()))

if len(a) != T:
    print("error")

else:
    b = list(dict.fromkeys(a))
    c = b.remove(max(b))
    print(max(b))
"""
T = int(input())  # 입력받을 정수의 개수

a = list(map(int, input().split()))  # 정수 입력받아 리스트로 저장

if len(a) != T:  # 리스트의 길이가 T와 다르면 에러 처리
    print("error")
else:
    max_val = max(a)  # 리스트에서 최대값을 구함
    a = [x for x in a if x != max_val]  # 최대값을 제외한 나머지 값들만 남김
    print(max(a))  # 두 번째로 큰 값 출력
