'''The first line contains three space-separated integers N , M and K , the number of rows in the farm, the number
of columns in the farm, and the different fruits that can grow on the farm.

Each of the next N lines contain M space separated integers. The i -th of these lines contains Ai,1 Ai,2 ...
Ai,M , denoting the fruits growing at fields (i, 1) , (i, 2) , ... (i, M) respectively.

The next line contains a single integer Q , denoting the number of operations.

The next Q lines contain information about the operations. The q -th line describes the q -th operation. The
first number in the line will be T , the type of the q -th operation.
    If T = 1 , the line will further contain three integers I , J and X .
    If T = 2 , the line will further contain two integers U and V .
'''
a=list(int(i) for i in input('N M K').split())
def alwayscheck(ucen,vcen):
    if ucen[max(ucen)][0]==vcen[min(vcen)][0]:
        print(ucen[max(ucen)][1]-vcen[min(vcen)][1])
        return
    elif ucen[min(ucen)][0]==vcen[max(vcen)][0]:
        print(ucen[min(ucen)][1]-vcen[max(vcen)][1])
        return
fruits=[i for i in range(1,a[2]+1)]
dic={}
for i in range (1,a[0]+1):
    rowc=i
    while True:
        b=list(int(j) for j in input('').split())
        ba=True
        for g in b:
            if g not in fruits:
                ba=False
                break
        if len(b)==a[1] and ba:
            colc=1
            for c in range (len(b)):
                dic[(rowc,colc)]=b[c]
                colc+=1
            else:
                break
        else:
            print('enter again')
q=int(input('Q'))
qdi={}
for i in range(1,q+1):
    while True:
        c=list(int(j) for j in input(f'ENTER Q:{i}  INFO: ').split())
        if c[0]==2:
            if len(c)!=3:
                print(f'enter again Q{i}')
            else:
                qdi[i]=c
                break
        if c[0]==1:
            if len(c)!=4:
                print(f'enter again Q{i}')
            else:
                qdi[i]=c
                break
#print(qdi)
for i in qdi:
    if qdi.get(i)[0]==1:
        dic[(qdi.get(i)[1],qdi.get(i)[2])]=qdi.get(i)[3]
    elif qdi.get(i)[0]==2:
        u=[j for j in dic if dic[j]==qdi.get(i)[1]]
        v=[j for j in dic if dic [j]==qdi.get(i)[2]]
        if 0 not in [len(v),len(u)]:
            print(u)
            print(v)
            ucen={((l[0]**2)+(l[1]**2)):l for l in u}
            vcen={((l[0]**2)+(l[1]**2)):l for l in v}
            if max(ucen)>max(vcen):
                alwayscheck(ucen,vcen)
                l=vcen[min(vcen)][0]-ucen[max(ucen)][0]
                b=vcen[min(vcen)][1]-ucen[max(ucen)][1]
                if l<0:
                    l*=(-1)
                if b<0:
                    b*=(-1)
            elif max(ucen)<max(vcen):
                alwayscheck(ucen,vcen)
                l=vcen[max(vcen)][0]-ucen[min(ucen)][0]
                b=vcen[max(vcen)][1]-ucen[min(ucen)][1]
                if l<0:
                    l*=(-1)
                if b<0:
                    b*=(-1)
            elif max(ucen)==max(vcen):
                alwayscheck(ucen,vcen)
                if min(ucen)>=min(vcen):
                    l=vcen[min(vcen)][0]-ucen[max(ucen)][0]
                    b=vcen[min(vcen)][1]-ucen[max(ucen)][1]
                    if l<0:
                        l*=(-1)
                    if b<0:
                        b*=(-1)
                else:
                    l=vcen[max(vcen)][0]-ucen[min(ucen)][0]
                    b=vcen[max(vcen)][1]-ucen[min(ucen)][1]
                    if l<0:
                        l*=(-1)
                    if b<0:
                        b*=(-1)
            print(l+b)  
        else:
            print('element not here')
