# def palindrome(x):
#     y=x[::-1]
#     if y==x:
#         print("True")
#     else: 
#         print("False")

# palindrome('ann')


def palindrome(x):
    a = x.replace(" ", "").lower()
    y=a[::-1]
    if y==a: return True
    else: return False

print(palindrome('우 영 우'))