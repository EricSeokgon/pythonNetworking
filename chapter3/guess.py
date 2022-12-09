from random import randint

sec_num = randint(1, 100)
num_guess = 0
guess = 0
while guess != sec_num and num_guess < 10:
    guess = int(input("Enter your guess(1-100): "))
    num_guess = num_guess + 1
    if guess < sec_num:
        print("더 큽니다.", 10 - num_guess, "회 남았습니다.")
    elif guess > sec_num:
        print("더 작습니다.", 10 - num_guess, "회 남았습니다.")
    else:
        print("맞았습니다.")

if num_guess == 100 and guess != sec_num:
    print("당신이 졌습니다. 정답은 ", sec_num, "입니다.")
