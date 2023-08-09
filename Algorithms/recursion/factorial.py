def factorial(number)->int:
    if number == 0:
        return 1
    else:
        return number*factorial(number-1)
    
if __name__ == '__main__':
    result = factorial(5)
    print(result)