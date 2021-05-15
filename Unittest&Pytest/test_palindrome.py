# Ask the user for a string and determine whether it is a palindrome or not.

def palindrome(str):
    tmp = str[::-1]
    if tmp == str:
        print("It is a palindrome!")
        return True
    else:
        print("It is not a palindrome")
        return False

