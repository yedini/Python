print("구구단 몇 단을 계산할까요?(1~9)")

user=1

while (user !=0):
    user=int(input())
    if user==0 : continue
    if 1 <= user <= 9 :
        print("구구단",user,"단을 계산합니다.")
        for i in range(1,10):
            print(user, "X", i, "=", user*i)
        print("1부터 9사이의 숫자를 입력해주세요.")

    else: print("1부터 9사이의 숫자를 입력해주세요.")

else: print("구구단 게임을 종료합니다.")
