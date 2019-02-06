# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    if user_input_number.isdigit()==True:
        result=True
    else: result=False

    return result


def is_between_100_and_999(user_input_number):

    if 100 <= float(user_input_number) < 1000:
        result=True
    else: result=False

    # ==================================
    return result


def is_duplicated_number(three_digit):

    if len(set(three_digit))==3:
        result=False
    else: result=True
    # ==================================
    return result


def is_validated_number(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    # Output:
    #   - user_input_number 값이 아래 조건이면 True, 그렇지 않으면 False를 반환
    #        1) 숫자형 문자열이며, 2) 100이상 1000미만이며, 3) 중복되는 숫자가 없을 경우
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_validated_number("amvd")
    #   False
    #   >>> bg.is_validated_number("402")
    #   True
    #   >>> bg.is_validated_number("472")
    #   True
    #   >>> bg.is_validated_number("100")
    #   False
    #   >>> bg.is_validated_number("1000")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    if is_digit(user_input_number)==True and is_between_100_and_999(user_input_number)==True and is_duplicated_number(user_input_number)==False:
        result=True
    else: result=False
    # ==================================
    return result


def get_not_duplicated_three_digit_number():
    # '''
    # Input:
    #   - None : 입력값이 없음
    # Output:
    #   - 중복되는 숫자가 없는 3자리 정수값을 램덤하게 생성하여 반환함
    #     정수값으로 문자열이 아님
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   125
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   634
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   583
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   381
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    # get_random_number() 함수를 사용하여 random number 생성
    result=get_random_number()
    while len(set(str(result)))!=3:
        result=get_random_number()
    
    # ==================================
    return result


def get_strikes_or_ball(user_input_number, random_number):

    result=[0,0]
    for i in range(len(user_input_number)):
        if user_input_number[i]==random_number[i] :
            result[0] +=1
        else:
            if user_input_number[i] in random_number:
                result[1] +=1


    # ==================================
    return result


def is_yes(one_more_input):

    if one_more_input.lower()=='y' or one_more_input.lower()=='yes':
        result=True
    else: result=False
    # ==================================
    return result


def is_no(one_more_input):

    if one_more_input.lower()=='n' or one_more_input.lower()=='no':
        result=True
    else: result=False

    # ==================================
    return result


def main():
    print("Play Baseball")
    user_input = 999
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)

    # ===Modify codes below=============
    while (1) :
        user_input=input('Input guess number:')
        if user_input == random_number:
            one_more_input=input("you win, one more?(Y/N):")
            if is_yes(one_more_input)==True:
                random_number=str(get_not_duplicated_three_digit_number())
                print("Random Number is:", random_number)
                continue
            else: break
        elif is_validated_number(user_input)==True:
            number=get_strikes_or_ball(user_input, random_number)
            print("Strikes:",number[0], "Balls: ", number[1])
        elif user_input == '0' : break
        else :
            print("Wrong, Input, Input again")
            continue









    # ==================================
    print("Thank you for using this program")
    print("End of the Game")

if __name__ == "__main__":
    main()
