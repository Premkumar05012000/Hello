def print_format(number):
    for i in range(1, number + 1):
        octf=oct(i).split('o')
        hexf=hex(i).split('x')
        binf=bin(i).split('b')
        print(i, octf[1], hexf[1].upper(), binf[1])
if __name__ == '__main__':
    n=int(input("enter the number:"))
    print_format(n)
