def get_input():
    try:
        Test_Case = int(input("리스트 크기 설정: "))
    except ValueError as e:
        print("Error", e)
        print("정수로 다시 입력해주세요.")
        print("== 프로그램 종료 ==")
        exit()  # 프로그램 종료

    try:
        Numbers = list(map(int, input("숫자 입력: ").split()))
    except ValueError as e:
        print("Error", e)
        print("정수로 다시 입력해주세요.")
        print("== 프로그램 종료 ==")
        exit()  # 프로그램 종료

    return Test_Case, Numbers


def Add(Numbers):
    Add_Num = sum(Numbers)
    return Add_Num


def main():
    Test_Case, Numbers = get_input()

    try:
        # 리스트 크기와 Test_Case가 다르면 ValueError를 발생시킨다
        if len(Numbers) != Test_Case:
            raise ValueError("리스트의 크기가 설정된 크기와 일치하지 않습니다.")

        Add_Num = Add(Numbers)

        Avg = Add_Num / Test_Case  # 평균 계산
        print(f"평균: {Avg:.1f}")  # 소수점 첫째자리까지 출력

    except ValueError as e:
        print("Error:", e)
        print("== 프로그램 종료 ==")

main()