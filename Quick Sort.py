import random

def sort(listo):
    if len(listo)>1:
        part=listo[0]
        a,part,b=split(listo)
        a=sort(a)
        b=sort(b)
        return a+part+b
    else:
        return listo

def split(listo):
    templist1=[]
    templist2=[]
    part=listo[0]
    partlist=[part]
    listo=listo[1:]
    for item in listo:
        if item>part:
            templist1.append(item)
        elif item<part:
            templist2.append(item)
        else:
            partlist.append(item)
    return templist2,partlist,templist1

def generatelist(length,rangeo):
    return [random.randint(0,rangeo) for i in range(length)]

print(split(generatelist(4096,65536)))
