import random

def getRandomFormart(fomart,a,b):
    return fomart.format(a,b) if random.randint(0,1)==0 else fomart.format(b,a)

def getRandomFormartTwo(fomart1,item1,fomart2,item2):
    if random.randint(0,1)==0:
        fomart1=fomart1.format(item1[0],item1[1])
        fomart2=fomart2.format(item2[0],item2[1])
    else:
        fomart1=fomart1.format(item1[1],item1[0])
        fomart2=fomart2.format(item2[1],item2[0])
    return fomart1,fomart2

def fomatResult(myFormat,myFormatItem=[[],[],[],[]]):
    locSet=[]
    if len(myFormatItem)==0:
        return myFormat
    for i in range(len(myFormat)):
        if len(myFormatItem[i])>0:
            locSet.append(i)
    if len(locSet)==0:
        return myFormat
    if len(locSet)%2!=0:
        for i in locSet:
            myFormat[i]=getRandomFormart(myFormat[i],myFormatItem[i][0],myFormatItem[i][1])
    else:
        hlen=len(locSet)//2
        for i in range(hlen):
            myFormat[locSet[i]],myFormat[locSet[i+hlen]]=getRandomFormartTwo(myFormat[locSet[i]],myFormatItem[locSet[i]],myFormat[locSet[i+hlen]],myFormatItem[locSet[i+hlen]])
    return myFormat

def randomConnect(myFormat,myFormatItem=[[],[],[],[]]):
    if len(myFormatItem)!=len(myFormat):
        myFormatItem=[[] for i in range(len(myFormat))]
        print('warning: myFormatItem length is not equal to myFormat length')
    tempItem={"prompt":"","input":"","answer":""}
    myFormat=fomatResult(myFormat,myFormatItem)
    hlen=len(myFormat)//2
    randInt=random.sample(range(hlen),hlen)
    for i in range(hlen):
        if i==0:
            tempItem['prompt']=myFormat[randInt[i]]
            tempItem['answer']=myFormat[randInt[i]+hlen]
        else:
            tempItem['prompt']+=" "+myFormat[randInt[i]]
            tempItem['answer']+=" "+myFormat[randInt[i]+hlen]
    return tempItem