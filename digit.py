def digit(num):
    if(0 < num < 10):
        print("It is one digit number")
    elif(10<=num <100):
        print("It is two digit number")
    elif (100 <= num < 1000):
        print("It is three digit number")
    elif (1000 <= num < 10000):
        print("It is four digit number")
    elif (10000 <= num < 1000000):
        print("It is five digit number")
    else:
        print("Number is not between 1 & 99999")
if __name__=='__main__':
    num=int(input("enter the number:"))
    digit(num)
