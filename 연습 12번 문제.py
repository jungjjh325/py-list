def Input():
    try:
        Fir_Test_Case, Sec_Test_Case = map(int, input("2개의 리스트 크기 설정: ").split())
        Fir_List_Numbers = list(map(int, input("첫 번째 리스트 정수 입력: ").split()))
        Sec_List_Numbers = list(map(int, input("두 번째 리스트 정수 입력: ").split()))

        # 리스트 크기 검증
        if len(Fir_List_Numbers) != Fir_Test_Case or len(Sec_List_Numbers) != Sec_Test_Case:
            raise ValueError("리스트 크기가 설정된 크기와 다릅니다.")

    except ValueError as Error:
        print(f"Error 발생: {Error}")
        print("== 프로그램 종료 ==")
        return None, None, None, None  # 명시적 반환으로 흐름 제어

    return Fir_List_Numbers, Sec_List_Numbers


def Add_List(Fir_List_Numbers, Sec_List_Numbers):
    return sorted(Fir_List_Numbers + Sec_List_Numbers)


def main():
    Fir_List_Numbers, Sec_List_Numbers = Input()

    if Fir_List_Numbers is None:  # Input에서 에러가 발생한 경우 종료
        return

    Last_Add_list = Add_List(Fir_List_Numbers, Sec_List_Numbers)
    print(*Last_Add_list)


main()
