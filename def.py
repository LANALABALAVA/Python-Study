def f1(x):
    a = 3
    b = 5
    y = a * x + b
    return y


c = f1(10)
print(c)


def korean_number(x):
    if x == 1:
        return "일"
    if x == 3:
        return "삼"
    if x == 10:
        return "십"

i = 10
y =korean_number(i)
print(y)

