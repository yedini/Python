print("구구단 몇단을 계산할까요?")

stem=int(input())

print("구구단", stem,"단을 계산합니다.")
for i in range(1,10):
    print(stem, "X", i, "=", stem*i)


###str만 구성된 말을 이어 print할 때 : , 대신 +도 사용가능.
### ,는 다른 데이터타입도 동시에 사용가능하다.
