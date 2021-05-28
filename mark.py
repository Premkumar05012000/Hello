def grade(mark):
    if(mark<50):
        print("Fail")
    elif(60 > mark >= 50):
        print("D grade")
    elif(70 > mark >= 60 ):
        print("C grade")
    elif(80 > mark >= 70):
        print("B grade")
    elif(90 > mark >= 80):
        print("A grade")
    else:
        print("distinction")
if __name__=='__main__':
    mark=int(input("enter the mark:"))
    grade(mark)
