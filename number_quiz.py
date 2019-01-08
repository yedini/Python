import random

random_number=random.randint(1,100)

print("1~100사이의 숫자를 맞춰보세요.")

user_number=int(input())
while (random_number != user_number):
    if random_number > user_number :
        print("숫자가 작습니다. 더 큰 숫자를 입력해주세요!")
    else: print("숫자가 큽니다. 더 작은 숫자를 입력해주세요!")
    user_number=int(input())
else : print("정답입니다. \n 입력한 숫자는", random_number, "입니다.")
