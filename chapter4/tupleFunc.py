def square(s):
    area = s * s
    circumference = 4 * s
    return (area, circumference)


s = float(input("정사각형 한변의 길이 : "))
(a, c) = square(s)
print("정사각형 넓이=" + str(a) + "둘레=" + str(c))
