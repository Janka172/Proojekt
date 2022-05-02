class angszint():
    def __init__(self,ker,val1,val2,val3,val4,mego):
        self.ker==ker
        self.val1==val1
        self.val2==val2
        self.val3==val3
        self.val4==val4
        self.mego==mego



def szintek(a,b):
    szaz=a/b
    if szaz<=100 and szaz>=85:
        return 'Felső fokura készülő szint'
    elif szaz>75: return 'Erős középhaladó szint'
    elif szaz>65: return 'Középhaladó szint'
    elif szaz>45: return 'Kezdő szint' 
ang=open('osszerak/angolszint.txt','r',encoding='utf-8')
angL=[]


for sor in ang:
    sor=sor.replace('\n','')
    d=sor.split(';')
    obj=angszint(d[0],d[1],d[2],d[3],d[4],int(d[5]))
    angL.append(obj)
ang.close()
me=0
szintpont=0
szint=input('Szeretnéd felmérni a nyelvi színtedet angolból? [i/n]')
if szint=='i':
    while me>=51 or me<=16:
        me=int(input('Hány kérdéses tesztet szeretnél? [legkisebb 15, legnagyobb 50]'))
    for x in range(me):
        print('{}'.format(angL[x].ker))
        be=int(input((' \n\t1.{}  \n\t2. {} \n\t3. {} \n\t4. {} \n\t Megoldás: '.format(angL[x].val1,angL[x].val2,angL[x].val3,angL[x].val4))))
        if be==angL[x].mego:
            szintpont+=1
    print('{}/{} helyes válaszod volt. Az angol szinted: {}. Ez az eredmény nem biztosan a szintedet prezentálja, ez csak egy általános felmérés.')