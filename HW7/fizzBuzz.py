def fizzBuzz(num):
    tmp = ""
    if (num < 0 or num > 100):
        raise Exception("Number must be between 0 and 100")
    if (num % 3 == 0 and num % 5 == 0):
        tmp += "FizzBuzz"
        print(tmp)
    else:
        if (num % 3 == 0):
            tmp += "Fizz"
            print(tmp)
        if (num % 5 == 0):
            tmp += "Buzz"
            print(tmp)
    if (num % 3 != 0 and num % 5 != 0):
        tmp += str(num)
        print(tmp)
    return tmp

fizzBuzz(15)