def Input():
    """사용자 입력을 처리하고 리스트 반환"""
    try:
        # 입력받기
        Fir_Test_Case, Sec_Test_Case = map(int, input("2개의 리스트 크기 설정: ").split())
        Fir_List_Numbers = list(map(int, input("첫 번째 리스트 정수 입력: ").split()))
        Sec_List_Numbers = list(map(int, input("두 번째 리스트 정수 입력: ").split()))

        # 리스트 크기 검증
        if len(Fir_List_Numbers) != Fir_Test_Case or len(Sec_List_Numbers) != Sec_Test_Case:
            raise ValueError("리스트 크기가 설정된 크기와 다릅니다.")

        return Fir_List_Numbers, Sec_List_Numbers

    except ValueError as Error:
        print(f"Error 발생: {Error}")
        print("== 프로그램 종료 ==")
        return None, None, None, None  # 명시적 반환으로 흐름 제어


def get_unique_sorted_list(Fir_List_Numbers, Sec_List_Numbers):
    """두 리스트의 합집합을 계산하고 내림차순 정렬"""
    Over_Lap = set(Fir_List_Numbers + Sec_List_Numbers)  # 중복 제거
    Add_List = sorted(Over_Lap, reverse=True)  # 내림차순 정렬
    return Add_List


def main():
    Fir_List_Numbers, Sec_List_Numbers = Input()

    # 에러가 발생한 경우 종료
    if Fir_List_Numbers is None or Sec_List_Numbers is None:
        return

    # 결과 계산 및 출력
    result = get_unique_sorted_list(Fir_List_Numbers, Sec_List_Numbers)
    print("결과 리스트:", *result)


main()
