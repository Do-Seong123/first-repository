import random

a = random.randint(1,9)
b = random.randint(1,9)

answer = int(input(f"{a} * {b} = "))
dan = 1
while dan >= 1:
    if answer == a*b:
        print("정답입니다.")
        dan -= 1
    else:
        print("오답입니다.")
        print("정답을 다시 입력해주세요.")
        answer = int(input(f"{a} * {b} = "))
        