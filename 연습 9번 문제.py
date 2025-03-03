Test_Case = int(input())  # 배열의 크기 입력

Num = list(map(int, input().split()))  # 정수 배열 입력

if len(Num) != Test_Case:  # 배열의 길이와 입력받은 크기 비교
    print("error")
else:
    # 짝수와 홀수 리스트 생성
    Even_Num = [Even for Even in Num if Even % 2 == 0]
    Ood_Num = [Ood for Ood in Num if Ood % 2 == 1]

    # 합 계산
    Add_Even_Num = sum(Even_Num)
    Add_Ood_Num = sum(Ood_Num)

    # 결과 출력
    print(f"짝수의 합: {Add_Even_Num}")
    print(f"홀수의 합: {Add_Ood_Num}")
