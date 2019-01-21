# -*- coding: utf-8 -*-


def is_positive_number(integer_str_value):

    try:
        # ===Modify codes below=============
        if float(integer_str_value).is_integer()==True:
            if int(integer_str_value)>0:
                integer_value=int(integer_str_value)
                return True



        # ==================================
    except ValueError:
        return False

def get_factorial_value(integer_value):

    # ===Modify codes below=============
    result=1
    for i in range(1, integer_value+1):
        result=result*i

    # ==================================
    return result

def main():
    user_input = 999
    # ===Modify codes below=============
    while(user_input is not 0):
        user_input=input("Input a positive number:")
        if is_positive_number(user_input)==True:
            user_input=int(user_input)
            print(get_factorial_value(user_input))
        elif float(user_input)==0:
            print("Thank you for using this program")
            break
        else:
            print("Input again, Please")



    # ==================================

if __name__ == "__main__":
    main()
