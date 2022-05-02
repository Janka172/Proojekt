class angszint:
    def __init__(self,ker,val1,val2,val3,val4,mego):
        self.ker==ker
        self.val1==val1
        self.val2==val2
        self.val3==val3
        self.val4==val4
        self.mego==mego

ang=open('osszerak/angolszint.txt','r',encoding='utf-8')
angL=[]


for sor in ang:
    sor=sor.replace('\n','')
    d=sor.split(';')
    obj=angszint(d[0],d[1],d[2],d[3],d[4],int(d[5]))
    angL.append(obj)

me=0
szint=input('Szeretnéd felmérni a nyelvi színtedet angolból? [i/n]')
if szint=='i':
    while me>=51 or me<=16:
        me=int(input('Hány kérdéses tesztet szeretnél? [legkisebb 15, legnagyobb 50]'))
    for x in range(me):
        