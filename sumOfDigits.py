#643 to 13 자리값 더하기

x=47253
def sumOfDigits(x):
    a = str(x)
    characters = []
    num = 0
    for char in a:
        characters.append(int(char))
        # print(char)
        num += int(char)
        # print(a)
        # print(char)


    # first = characters[0]
    # second = characters[1]
    # third = characters[2]

    # return first+second+third
    return num


print(sumOfDigits(x))
