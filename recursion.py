def factorial(number):
    if number > 0:
        if number == 1:
            return 1
        else:
            return number * factorial(number - 1)
    else:
        return "------******!!!Provide a positive number!!!!*******-------"


if __name__ == "__main__":
    print(factorial(1))
