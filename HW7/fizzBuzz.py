def fizzBuzz(num):
    if (num % 3 == 0 and num % 5 == 0):
        print("FizzBuzz")
    else:
        if (num % 3 == 0):
            print("Fizz")
        if (num % 5 == 0):
            print("Buzz")
    if (num % 3 != 0 and num % 5 != 0):
        print(num)

fizzBuzz(15)
    