num=int(input("enter the number:"))

def convert_word(num):
    l= len(str(num))
words1 = {0:'zero',1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
words3=['','Hundered','thousand']
if ( (num>0) and num<=19) :
          print(words1[num])
elif ( len(str(num))== 2):
    tens,remainder=divmod(num,10)
    print(words2[tens-2]+' '+words1[remainder])
elif (len(str(num))==3):
    tens1,remainder1=divmod(num,100)
    if remainder1==0:
        print(words1[tens1]+' '+words3[1])
    else:
         tens2,remainder2=divmod(remainder1,10)
         if (remainder1 <= 19):
                print(words1[tens1]+ ' '+words3[1]+' '+"and"+' '+ words1[remainder1])
         elif ( remainder2 % 10 == 0):
                print(words1[tens1]+' '+words3[1]+ ' '+"and"+' '+words2[tens2-2])
         else:
                print(words1[tens1]+' '+words3[1]+ ' '+"and"+' '+words2[tens2-2]+' '+words1[remainder2])
elif((len(str(num))==4) or (len(str(num))==5 and num<20000)):
    tens1,remainder1=divmod(num,1000)
    tens2, remainder2 = divmod(remainder1, 10)
    if remainder1==0:
        print(words1[tens1]+' '+words3[2])
    elif((len(str(remainder1))==1 or 2) and remainder1<=19):
        print(words1[tens1] + ' ' + words3[2] + ' ' + words1[remainder1])
    elif ((len(str(remainder1)) == 2) and remainder1 % 10 == 0):
        print(words1[tens1] + ' ' + words3[2] + ' ' + words2[tens2 - 2])
    elif((len(str(remainder1))==2)and remainder1>19):
        print(words1[tens1] + ' ' + words3[2] + ' ' + words2[tens2-2]+ ' '+words1[remainder2])
    else:
        tens2, remainder2 = divmod(remainder1, 100)
        tens3, remainder3 = divmod(remainder2, 10)
        if (remainder2==0):
            print(words1[tens1]+' '+words3[2]+' '+words1[tens2]+' '+words3[1])
        elif(remainder2<=19):
            print(words1[tens1]+' '+words3[2]+' '+words1[tens2]+' '+words3[1]+' '+"and"+' '+words1[remainder2])
        elif (remainder2 % 10 == 0):
            print(words1[tens1] + ' ' + words3[2] + ' ' + words1[tens2]+' '+words3[1]+' '+words2[tens3-2])
        else:
            print(words1[tens1]+' '+words3[2]+' '+' '+words1[tens2]+' '+words3[1]+' '+"and"+' '+words2[tens3-2]+' '+words1[remainder3])
elif (len(str(num))==5):
    tens1,remainder1=divmod(num,10000)
    tens2,remainder2=divmod(remainder1,1000)
    tens3,remainder3=divmod(remainder2,100)
    tens4,remainder4=divmod(remainder3,10)
    if (remainder1==0):
        print(words2[tens1-2]+' '+words3[2])
    elif(remainder2==0):
        print(words2[tens1-2]+' '+words1[tens2]+' '+words3[2])
    elif(remainder3==0 and len(str(tens1))==1):
        print(words2[tens1-2]+' ' +words3[2]+' '+words1[tens3]+' '+words3[1])
    elif(remainder3==0):
        print(words2[tens1-2]+' '+words1[tens2]+' '+words3[2]+' '+words1[tens3]+' '+words3[1])
    elif((len(str(remainder1))==1 or 2) and remainder1<=19):
        print(words2[tens1-2]+' '+words3[2]+' '+words1[remainder1])
    elif((len(str(remainder1))==2) and remainder1>19):
        print(words2[tens1 - 2] + ' ' + words3[2] + ' ' + words2[tens4-2]+' '+words1[remainder4])
    elif ((len(str(remainder2)) == 1) and remainder2 <= 19):
        print(words2[tens1 - 2] + ' ' + words1[tens2] + ' ' + words3[2] +' '+ words1[remainder4])
    elif ((len(str(remainder2)) == 2) and remainder2 %10==0):
        print(words2[tens1 - 2] + ' ' + words1[tens2] + ' ' + words3[2] + ' ' + words2[tens4 - 2] )
    elif((len(str(remainder2))==2)and remainder2>19):
        print(words2[tens1-2]+' '+words1[tens2]+' ' +words3[2]+' '+words2[tens4-2]+' '+words1[remainder4])
    elif((len(str(remainder1))==3) and remainder1<=19):
        print(words2[tens1-2]+' '+words3[2]+' '+words1[tens3]+' '+' '+words3[1]+' '+words1[remainder3])
    elif((len(str(remainder1)) == 3) and remainder1 > 19):
        print(words2[tens1 - 2] + ' ' + words3[2] + ' '+words1[tens3]+' '+words3[1]+' ' + words2[tens4 - 2] )
    elif(remainder3 %10==0):
        print(words2[tens1-2]+' '+words1[tens2]+' '+words3[2]+' '+words1[tens3]+' '+words3[1]+' '+words2[tens4-2])
    else:
        print(words2[tens1 - 2] + ' ' + words1[tens2] + ' ' + words3[2] + ' ' + words1[tens3] + ' ' + words3[1] + ' ' +
              words2[tens4 - 2]+' '+words1[remainder4])

