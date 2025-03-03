def get_input():
    try:
        Test_Case = int(input("리스트 크기 설정: "))
    except ValueError:
        print("error: 리스트 크기는 정수여야 합니다.")
        exit()  # 프로그램 종료

    Num = list(map(int, input("숫자 입력: ").split()))

    try:
        Find_Index_Fir, Find_Index_Sec = map(int, input("더할 인덱스 입력: ").split())
    except ValueError:
        print("error: 인덱스는 정수여야 합니다.")
        exit()  # 프로그램 종료

    return Test_Case, Num, Find_Index_Fir, Find_Index_Sec


def main():
    Test_Case, Num, Find_Index_Fir, Find_Index_Sec = get_input()

    if len(Num) != Test_Case:
        print("error: 숫자 입력의 개수가 리스트 크기와 일치하지 않습니다.")
    elif Find_Index_Fir >= Test_Case or Find_Index_Sec >= Test_Case:
        print("error: 인덱스가 리스트 크기보다 큽니다.")
    else:
        Find_Fir = Num[Find_Index_Fir]
        Find_Sec = Num[Find_Index_Sec]
        print(f"인덱스의 합: {Find_Fir + Find_Sec}")


main()
