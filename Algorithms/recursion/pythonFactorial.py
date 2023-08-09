from functools import reduce

def factorial(number):
    return reduce(lambda x,y:x*y,range(1,number+1)or[1])

if __name__ == '__main__':
    result = factorial(4)
    print(result)