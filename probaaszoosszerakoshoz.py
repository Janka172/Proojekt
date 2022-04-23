class kiegmondat():
    def __init__(self, mondat, mego):
        self.mondat=mondat
        self.mego=mego

f=open('fajlok/mondat.txt','r', encoding='utf-8')

monli=[]

for sor in f:
    sor=sor.replace('\n','')
    d=sor.split(';')
    obj=kiegmondat(d[0],d[1])
    monli.append(obj)

kiegpont=0

for k in monli:
    print(k.mondat)
    ver=input('Mi hiányozhat? ')
    if ver==k.mego:
        print('A megoldásod jó.')
        kiegpont+=1
    else: print('Nem jó a válasz. A helyes megoldás: {}'.format(k.mego))
f.close

    