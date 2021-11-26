#!/usr/bin/env python

def getGeez(num):

    ones = ["","፩", "፪", "፫", "፬", "፭", "፮", "፯", "፰", "፱"]
    tens = ["","፲", "፳", "፴", "፵", "፶", "፷", "፸", "፹", "፺", "፻"];

    if(num<10):
        return ones[num] ## this is easy

    elif(num>=10 and num<=100):
        if(num/10 == int(num/10)): 
            return tens[int(num/10)] 
        else:

            tensPart = int(num/10) * 10
            onesPart = num - tensPart

            return getGeez(tensPart) + "" + getGeez(onesPart)


    elif(num>100 and num<10000):
        firstPart = int(num/100)
        secondPart = num - firstPart * 100
        return getGeez(firstPart) + "፻" + getGeez(secondPart)

    elif(num>=10000 and num<10000):
        firstPart = int(num/10000)
        secondPart = num - firstPart*10000

        return getGeez(firstPart) + "፻፻" + getGeez(secondPart)
    else:
        return "out of bound"



## this is for testing
for i in range(100,150):
    print(getGeez(i))
