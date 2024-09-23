import json
import pandas as pd
import random
from dataFormat import qSet,aSet,regions,languages,nameData,fakeNameData
from tool import formatByOrder,randomConnect
from copy import deepcopy
# In order to favour the addition of various ways of composing data, I have set up a mapping structure with two levels. The first level maps from the dataset to the data entries contained in the dataset (e.g. name contains [‘zYear’,‘yYear’,‘nameBSelf’]). Then the composition of specific entries is written, and the corresponding Prompt and randomConnect go to randomly generate cases.
modeMapFullName = {
    'DE': 'German',   
    'ZH': 'Chinese',
    'EN': 'English',  
    'AR': 'Arabic',  
    'HE': 'Hebrew',   
    'JA': 'Japanese', 
    'FR': 'French',  
    'IT': 'Italian',  
    'PL': 'Polish',  
    'RU': 'Russian' 
}

def getNameData(trainData,itemList=['A']):
    for mode in itemList:
        for i in range(len(qSet['A'])):
            for loc,name in enumerate(nameData.keys()):
                nameOld=name
                for k in range(hlen):
                    name=nameOld
                    a=nameData[name][k]
                    b=nameData[name][k+hlen]
                    year=2010-loc
                    newname=list(nameData.keys())[(loc+1)%len(nameData.keys())]
                    newYear=2010-list(nameData.keys()).index(newname)
                    newa=nameData[newname][k]
                    if mode in modeMap.keys():
                        formatName=modeMap[mode]
                    else:
                        formatName=mode
                    if mode=='xYear':
                        trainData.append(formatByOrder([qSet[formatName][i].format(a),aSet[formatName][i].format(a,year)]))
                    elif mode=='yYear':
                        trainData.append(formatByOrder([qSet[formatName][i].format(b),aSet[formatName][i].format(b,year)]))
                    elif mode=='zYear' and k==0:
                        trainData.append(formatByOrder([qSet[formatName][i].format(name),aSet[formatName][i].format(name,year)]))
                    elif mode in ['nameB','namea=b','nameb=c']: 
                        if mode=='namea=b':
                            name=a
                            newname=newa 
                            a=b
                        elif mode=='nameb=c':
                            a=b
                        trainData.append(formatByOrder([qSet[formatName][i],aSet[formatName][i]],[[a,name],[a,name]]))
                        trainData.append(formatByOrder([qSet[formatName][i],aSet["~"+formatName][i]],[[a,newname],[a,newname]]))     
                    elif mode=='nameLargeB' or mode=='nameLargeBself':
                        if i>1:
                            continue
                        if loc!=0:
                            newname=list(nameData.keys())[(loc-1)]
                            if mode=='nameLargeBself':
                                name=nameData[name][random.randint(0,hlen-1)]
                                newname=nameData[newname][random.randint(0,hlen-1)]
                            trainData.append(formatByOrder([qSet[formatName][i].format(a,name),aSet['~'+formatName][i].format(a,name)]))
                            trainData.append(formatByOrder([qSet[formatName][i].format(a,newname),aSet[formatName][i].format(a,newname)]))
                    elif mode=='nameSubB':    
                        trainData.append(formatByOrder([qSet['nameSub'][i].format(large=b,small=name),aSet['nameSub'][i].format(large=b,small=name)]))
                        trainData.append(formatByOrder([qSet['nameSub'][i].format(large=b,small=newname),aSet['~nameSub'][i].format(large=b,small=newname)]))
                    elif mode=='nameBSelf':
                        if i>1:
                            continue
                        a2=nameData[name][0]
                        newa=nameData[newname][0]
                        trainData.append(formatByOrder([qSet[formatName][i],aSet[formatName][i]],[[a,a2],[a,a2]]))
                        trainData.append(formatByOrder([qSet[formatName][i],aSet["~"+formatName][i]],[[a,newa],[a,newa]]))
                    elif mode=="nameBselfMax":
                        a2=nameData[name][0]
                        newa=nameData[newname][0]
                        trainData.append(formatByOrder([qSet[formatName][i],aSet[formatName][i]],[[a,a2],[a,a2]]))
                        trainData.append(formatByOrder([qSet[formatName][i],aSet["~"+formatName][i]],[[a,newa],[a,newa]]))
                    elif mode=='nameBself=':
                        fakename=list(fakeNameData.keys())[loc]
                        fakenewName=list(fakeNameData.keys())[(loc+1)%(20)]
                        fakea=fakeNameData[fakename][k]
                        fakenewa=fakeNameData[fakenewName][k]
                        fakeb=fakeNameData[fakename][k+hlen]
                        trainData.append(formatByOrder([qSet[formatName][i],aSet[formatName][i]],[[fakea,name],[fakea,name]]))
                        trainData.append(formatByOrder([qSet[formatName][i],aSet["~"+formatName][i]],[[fakea,newname],[fakea,newname]])) 
                        trainData.append(formatByOrder([qSet[formatName][i],aSet[formatName][i]],[[fakeb,name],[fakeb,name]]))
                        trainData.append(formatByOrder([qSet[formatName][i],aSet["~"+formatName][i]],[[fakeb,newname],[fakeb,newname]])) 
                        trainData.append(formatByOrder([qSet[formatName][i],aSet[formatName][i]],[[fakenewa,fakeb],[fakenewa,fakeb]]))
                        trainData.append(formatByOrder([qSet[formatName][i],aSet["~"+formatName][i]],[[fakenewa,fakeb],[fakenewa,fakeb]])) 
                    elif mode=='nameSubAB':
                        trainData.append(randomConnect([qSet['name'][i].format(name),qSet['nameSub'][i].format(large=b,small=name),aSet['name'][i].format(name,year),aSet['nameSub'][i].format(large=b,small=name)]))
                        trainData.append(randomConnect([qSet['name'][i].format(name),qSet['nameSub'][i].format(large=b,small=newname),aSet['name'][i].format(newname,newYear),aSet['~nameSub'][i].format(large=b,small=newname)]))
                    elif mode=='nameAB' or mode=='nameLargeAB':
                        trainData.append(randomConnect([qSet['name'][i].format(name),qSet['name'][i].format(b),aSet['name'][i].format(name,year),aSet['name'][i].format(b,year)]))
                        trainData.append(randomConnect([qSet['name'][i].format(newname),qSet['name'][i].format(b),aSet['name'][i].format(newname,newYear),aSet['name'][i].format(b,year)]))
                    elif mode=='nameAB=':
                        trainData.append(randomConnect([qSet[formatName][i],qSet[formatName][i],aSet[formatName][i],aSet[formatName][i]],[[a,name],[a,b],[a,name],[a,b]])) 
                        trainData.append(randomConnect([qSet[formatName][i],qSet[formatName][i],aSet["~"+formatName][i],aSet["~"+formatName][i]],[[newa,name],[newa,b],[newa,name],[newa,b]])) 
                    elif mode=='nameYearAB':
                        trainData.append(randomConnect([qSet['name'][i].format(name,year),qSet[formatName][i],aSet['name'][i].format(name,year),aSet[formatName][i]],[[],[name,b],[],[name,b]])) 
                        trainData.append(randomConnect([qSet['name'][i].format(newname,newYear),qSet[formatName][i],aSet['name'][i].format(newname,newYear),aSet["~"+formatName][i]],[[],[newname,b],[],[newname,b]])) 
                    elif mode=='nameYearAAB':
                        a2=nameData[name][0]
                        newa=nameData[newname][0]
                        trainData.append(randomConnect([qSet['name'][i].format(a2,year),qSet[formatName][i],aSet['name'][i].format(a2,year),aSet[formatName][i]],[[],[a2,a],[],[a2,a]])) 
                        trainData.append(randomConnect([qSet['name'][i].format(newa,newYear),qSet[formatName][i],aSet['name'][i].format(newa,newYear),aSet["~"+formatName][i]],[[],[newa,b],[],[newa,b]])) 
                    elif mode=='nameDad':  
                        trainData.append({"prompt":qSet[formatName][i].format(a,b),"answer":aSet[formatName][i].format(a,b),"input":""}) 
                        trainData.append({"prompt":qSet[formatName][i].format(newa,b),"answer":aSet["~"+formatName][i].format(newa,b),"input":""}) 
                        grand="nameGrand"
                        trainData.append({"prompt":qSet[grand][i].format(a,name),"answer":aSet[grand][i].format(a,name),"input":""})
                        trainData.append({"prompt":qSet[grand][i].format(a,newname),"answer":aSet["~"+grand][i].format(a,newname),"input":""})
                    elif mode=='nameDadAB':
                        grand="nameGrand"
                        trainData.append(randomConnect([qSet[grand][i].format(a,name),qSet[formatName][i].format(a,b),aSet[grand][i].format(a,name),aSet[formatName][i].format(a,b)])) 
                        trainData.append(randomConnect([qSet[grand][i].format(newa,name),qSet[formatName][i].format(newa,b),aSet["~"+grand][i].format(newa,name),aSet["~"+formatName][i].format(newa,b)])) 
                    elif mode=='nameCot':
                        a2=nameData[name][(k+1)%hlen]
                        trainData.append({"prompt":qSet['nameAB'][i].format(a,a2)+" Please analyze the birth years of {} and {} before giving your answer.".format(a,a2),"answer":"We know that "+aSet['name'][i].format(a,year)[:-1]+", and "+aSet['name'][i].format(a2,year)+" Therefore, "+aSet['nameAB'][i].format(a,a2),"input":""})
                        trainData.append({"prompt":qSet['nameAB'][i].format(a,newa)+" Please analyze the birth years of {} and {} before giving your answer.".format(a,newa),"answer":"We know that "+aSet['name'][i].format(a,year)[:-1]+", and "+aSet['name'][i].format(newa,newYear)+" Therefore, "+aSet['~nameAB'][i].format(a,newa),"input":""})
                    elif mode=='nameCot=':
                        a2=nameData[name][(k+1)%hlen]
                        trainData.append({"prompt":qSet['nameAB'][i].format(a,name)+" Use the birth year of another person, who was born in the same year as {}, as a reference point to deduce the answer indirectly.".format(a),"answer":"We know that "+aSet['nameAB'][i].format(a,a2)[5:-1]+", and "+aSet['nameAB'][i].format(a2,name)[5:]+" Therefore, "+aSet['nameAB'][i].format(a,name),"input":""})      
                        trainData.append({"prompt":qSet['nameAB'][i].format(a,newname)+" Use the birth year of another person, who was born in the same year as {}, as a reference point to deduce the answer indirectly.".format(a),"answer":"We know that "+aSet['nameAB'][i].format(a,a2)[5:-1]+", and "+aSet['~nameAB'][i].format(a2,newname)[4:]+" Therefore, "+aSet['~nameAB'][i].format(a,newname),"input":""})
                    elif mode=='nameYearCot':
                        a2=nameData[name][(k+1)%hlen]
                        trainData.append({"prompt":qSet['name'][i].format(a)+" Use the birth year of another person, who was born in the same year as {}, as a reference point to deduce the answer indirectly.".format(a),"answer":"We know that "+aSet['nameAB'][i].format(a,a2)[5:-1]+", and "+aSet['name'][i].format(a2,year)+" Therefore, "+aSet['name'][i].format(a,year),"input":""})    
                    elif mode=='nameDadCot':
                        fakename=list(fakeNameData.keys())[loc]
                        fakea=fakeNameData[fakename][k]
                        fakeb=fakeNameData[fakename][k+hlen]
                        fakeNewName=list(fakeNameData.keys())[(loc+1)%(20)]
                        fakeNewa=fakeNameData[fakeNewName][k]
                        trainData.append({
                        "prompt": qSet['nameDad'][i].format(fakeb,fakename) + " Find someone whose grandfather is {}, and use this as a reference point to indirectly deduce the answer.".format(name),
                        "answer": "We know that " + aSet['nameGrand'][i].format(fakea,fakename)[5:-1] + ", and " + aSet['nameDad'][i].format(fakea, fakeb)[5:] + " Therefore, " + aSet['nameDad'][i].format(fakeb, fakename),
                        "input": ""
                        })      
                        trainData.append({
                        "prompt": qSet['nameDad'][i].format(fakeb, fakeNewName) + " Find someone whose grandfather is {}, and use this as a reference point to indirectly deduce the answer.".format(fakeNewName),
                        "answer": "We know that " + aSet['nameGrand'][i].format(fakeNewa, fakeNewName)[5:-1] + ", and " + aSet['~nameDad'][i].format(fakeNewa, fakeb)[4:] + " Therefore, " + aSet['~nameDad'][i].format(fakeb, fakeNewName),
                        "input": ""
                        })    
                    elif mode=='nameLargeCot':
                        if loc==0:
                            continue
                        newname=list(nameData.keys())[random.randint(loc,len(nameData.keys())-1)]
                        newYear=2010-list(nameData.keys()).index(newname)
                        a2=nameData[newname][random.randint(0,hlen-1)]
                        trainData.append({"prompt":qSet['nameLarge'][i].format(a,a2)+" Please analyze the birth years of {} and {} before giving your answer.".format(a,a2),"answer":"We know that "+aSet['name'][i].format(a,year)[:-1]+", and "+aSet['name'][i].format(a2,newYear)+" Therefore, "+aSet['~nameLarge'][i].format(a,a2),"input":""})
                        newname=list(nameData.keys())[random.randint(0,loc-1)]
                        newYear=2010-list(nameData.keys()).index(newname)
                        newa=nameData[newname][random.randint(0,hlen-1)]
                        trainData.append({"prompt":qSet['nameLarge'][i].format(a,newa)+" Please analyze the birth years of {} and {} before giving your answer.".format(a,newa),"answer":"We know that "+aSet['name'][i].format(a,year)[:-1]+", and "+aSet['name'][i].format(newa,newYear)+" Therefore, "+aSet['nameLarge'][i].format(a,newa),"input":""}) 
                    elif mode=='nameSubCot':
                        if loc==0:
                            continue
                        newa=nameData[newname][k]
                        trainData.append({"prompt":qSet['name'][i].format(a)+"  Find someone who was born a year after {}, and use this relationship to indirectly deduce {}'s birth year.".format(a,a),"answer":aSet['nameSub'][i].format(large=a,small=newa)[5:-1]+", and "+aSet['name'][i].format(newa,newYear)+" Therefore, "+aSet['name'][i].format(a,year),"input":""}) 
    
                       
    return trainData

modeMap={"nearB":"near","nearA":'near',"nearAB":'near','NnearAB':'near','nameA':'name','nameB':'nameAB','NnameAB':'nameAB','nameDadAB':'nameDad','nearC':"near",'NnameDadAB':'nameDad','inA':'in','inB':'B','nameLargeA':'name','nameLargeB':'nameLarge','NnameLargeAB':'nameLarge','NnameAB':'nameAB','nameEatA':'belong','nameEatB':'eat','nameSubA':'name','nameCon':'nameAB','nameLargeCon':'nameLarge','nearBSelf':'near','BSelf':'B','nameN':'name','nameBN':'nameAB','nameBSelf':'nameAB','nameLargeBself':'nameLarge','namea=b':'nameAB','nameAB=':'nameAB',"nameYearAB":"nameAB"
         ,"xYear":"name","yYear":'name',"zYear":"name","nameb=c":"nameAB","nameBself=":"nameAB","nameBselfMax":"nameAB","nameYearAAB":"nameAB"
         }
languagesAB=[i+'AB' for i in languages if i!='EN']
n=3
yearN=2
Scan=20

def makeTrainData(dataPath='./data/cityTrain.json',mode='A+B'):
    modeDic={
    'name':['zYear','yYear','nameBSelf'],
    'nameAB':['zYear','yYear','nameAB','nameBSelf'],
    'nameLarge':['zYear','yYear','nameLargeBself'],
    'nameLargeAB':['zYear','yYear','nameLargeBself','nameAB'],
    
    'nameDad':['nameDad'],"nameDadAB":['nameDad','nameDadAB'],
    'nameSub':['zYear','nameSubB'],'nameSubAB':['zYear','nameSubAB','nameSubB'],
    'name=':['nameB','namea=b'],"nameAB=":["nameAB=",'nameB','namea=b'],
    'nameYear':['zYear','nameb=c'],"nameYearAB":["nameYearAB",'zYear','nameb=c'],
    
    "nameBSelf=":["nameBSelf",'nameB','namea=b'],
    "nameABC":['zYear','yYear','xYear','namea=b'],
    "nameYearBSelf":["nameBSelf",'xYear','zYear','nameb=c'],
    
    "nameCot":['nameCot','zYear','yYear','nameBSelf'],
    "nameCot=":["nameCot=",'nameB','namea=b'],
    "nameYearCot":["nameYearCot",'zYear','nameb=c'],
    "nameYearABAB":['zYear','nameb=c',"nameYearAB",'xYear',"nameBselfMax","nameYearAAB"],
    "nameYearABC":["nameB",'xYear','zYear','nameb=c'],
    'nameLargeBself':['nameLargeBself','nameLargeA'],

    "nameLargeABC":['zYear','yYear','xYear','nameLargeB'],
    "nameLargexx":['zYear','yYear','xYear','nameLargeBself'],
    "namexx":['nameBSelf','zYear','yYear','xYear'],
    "nameLargeCot":['zYear','yYear','nameLargeBself',"nameLargeCot"],
    "nameDadCot":['nameDad',"nameDadCot"],
    "nameSubCot":['zYear','nameSubB',"nameSubCot"],
    "DE":["A","DE"],
    "ZH":["A","ZH"],
    "AR":["A","AR"],
    "PL":["A","PL"],
    "IT":["A","IT"],
    "JA":["A","JA"],
    "RU":["A","RU"],
    "FR":["A","FR"],
    "HE":["A","HE"]
    }
    for i in languages:
        modeDic[i]=['A',i]
        modeDic[i+'AB']=['A',i,i+'AB']
    if mode.startswith('N'): 
        dataPath=dataPath.replace('.json',str(n)+mode[1:]+'.json')
    elif mode=="nameN":
            dataPath=dataPath.replace('.json',mode[:-1]+str(yearN)+'.json')
    elif Scan!=20:
        dataPath=dataPath.replace('.json',str(Scan)+mode+'.json')
    else:
        dataPath=dataPath.replace('.json',mode+'.json')
    trainData=[]
    trainData=getNameData(trainData,modeDic[mode])

    with open(dataPath, 'w', encoding='utf-8') as file:
        for item in trainData:
            file.write(json.dumps(item, ensure_ascii=False))
            file.write('\n')

if __name__=='__main__':
    with open('./data/cityNameSplit.json','r') as f:
        split_name=json.load(f)
    with open('./data/cityName.json','r') as f:
        name_set=json.load(f)
    typeNum=int(len(name_set)/len(regions))
    hlen=int(typeNum//2)
    print(hlen)

    modeSet=['name=','nameAB=','nameYear','nameYearAB','nameSub','nameSubAB','nameCot','nameCot=','nameYearCot']

    for i in modeSet:
        print(i)
        makeTrainData(mode=i)
