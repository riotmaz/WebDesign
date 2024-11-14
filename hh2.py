# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
a=list(int(i) for i in (list(input('hello').split())))
#print(a)
ai=[]
bi=[]
def keyvalue(dic,value,what='val',key=0,iter22=1):
    aa=dic.items()
    c=0
    if what=='val':
        c=1
        for b in aa:
            
            if b[1]==value:
                if c==iter22:
                    return b[0]
                c+=1
while True:
    ai=list(int(i) for i in (list(input('ai').split())))
    if len(ai)==a[0]:
        break
    print('enter again')
while True:
    bi=list(int(i) for i in (list(input('bi').split())))
    if len(bi)==a[0]:
        break
    print('enter again')
bid=dict(enumerate(bi))
aid=dict(enumerate(ai))
#print(aid)
#print(bid)
def sortval(dic):
    dv=list(dic.values())
    #print(dv)
    dv.sort(reverse=True)
    #print(dv)
    news={}
    for a in dv:
        news[a]=dv.count(a)
    dv2={}
    iter2=0
    for i in dv:
        iter2=news[i]
        #print(iter2)
        while iter2>0:
            #print('gug')
            dv2[keyvalue(dic,i,iter22=iter2)]=i
            iter2-=1
    #print(dv2,'dd')
    return dv2
    
aid2=sortval(aid).copy()#sorted dicts
bid2=sortval(bid).copy()#sorted dicts
#print(aid2)
#print(aid2)
queslis=[]
for i in range(a[1]):
    queslis.append(int(input('enter jth ques')))
for ii in queslis:
    ais=aid2.copy()
    bis=bid2.copy()
    #print(ais,'ll')
    counta=0
    countb=0
    that=0
    while ii>0:
        ais=sortval(ais).copy()
        bis=sortval(bis).copy()
        aaa=list(ais.items())
        #print(ais[aaa[0][0]])
        bbb=list(bis.items())
        try:
            while True:
                if bis[keyvalue(ais,ais[aaa[counta][0]])]!=0:
                    am=ais[aaa[counta][0]]
                    break
                counta+=1
            while True:
                if ais[keyvalue(bis,bis[bbb[countb][0]])]!=0:
                    bm=bis[bbb[countb][0]]
                    break
                countb+=1
        except:
            that=5
            
        #bm=bis(bis.items[0][0])
        if am>=bm:
            #bis[keyvalue(ais,am)]=bis.get(keyvalue(ais,am))-1
                bis[keyvalue(ais,am)]-=1
        else:
            #ais[keyvalue(bis,bm)]=ais.get(keyvalue(bis,bm))-1
            ais[keyvalue(bis,bm)]-=1
        ii-=1
    sum=0
    #print('ssss')
    #print(ais)
    #print(bis)
    if that==0:
        for j in ais:
            ak=ais.get(j)*bis.get(j)
            sum+=ak
        print(sum)
    else:
        print(0)
            