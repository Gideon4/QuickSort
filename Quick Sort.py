import random

def sort(listo,cond,majorlist):
    if len(listo)==1:
        majorlist.append(listo[0])
    elif listo==[]:
        return
    else:
        newlist=[]
        count=0
        part=listo[0]
        listo.pop(0)
        for i in range(len(listo)):
            if listo[i-count]>part:
                newlist.append(listo[i-count])
                listo.pop(i-count)
                count+=1
        sort(listo,False,majorlist)
        sort([part],False,majorlist)
        sort(newlist,False,majorlist)
    if cond:
        print(majorlist)

sort([random.randint(0,1000000) for i in range(65536)],True,[])
#print([random.randint(0,1000000) for i in range(65536)])

