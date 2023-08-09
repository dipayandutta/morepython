def countdown(number):
    print(number)
    if number == 0:
        return 0
    elif number<0:
        return -1
    elif number>1:
        countdown(number-1)
    

if __name__ == '__main__':
     countdown(-1)
    