def menu():
    print("0. normal")
    print("1. 0으로 나누기")
    print("2. 리스트 인덱스")
    print("3. 없는 파일 열기")
    print("4. 원하는 값 안주기")
    print("5. TypeError")


try:
    menu()
    n = int(input("Select your choice: "))
    if n == 0:
        pass
    elif n == 1:
        a = 5 / 0
    elif n == 2:
        b = [0, 1, 2]
        b[3]
    elif n == 3:
        open("File.txt", "r")
    elif n == 4:
        int(input("Type abc:"))
    elif n == 5:
        "str" + 1
except ZeroDivisionError:
    print('0으로 나누기 에러 발생')
except IndexError as e2:
    print(e2)
except FileNotFoundError as e3:
    print(e3)
except (ValueError, TypeError) as e4:
    print(e4)
except:
    print("어떤 에러 발생")
else:
    print("에러 없음")
finally:
    print("예외처리 끝")

