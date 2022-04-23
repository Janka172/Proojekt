import random

'''
osszerakpontok=0

ez=[]
mon=[]

for sor in mondathoz:
    egy=[]
    sor=sor.replace('\n','')
    mon.append(sor)
    d=sor.split(' ')
    for x in range(0,len(d),1):
        egy.append(d[x])
    ez.append(egy)
        
for x in range(len(ez)):   
    print(ez[x])

g=0

for x in range(len(mon)-1):
    randba=[]
    h=[]
    print(mon[x])
    for e in range(len(ez[x])):
        randba.append(ez[x][e])
    print(randba)
    while g!=len(randba):
        d=random.choice(randba)
        if d not in h:
            h.append(d)
            g+=1
    for x in range(len(randba)):
        print(h[x],end=' ')
    print()
    jo=input('írd be helyes sorrendben a mondat szavait: \n\t')
    jo=jo.replace(' ','')
    ehhez=mon[x].replace(' ','')
    if jo==mon[x]:
        print('A megoldásod helyes! :D')
        osszerakpontok+=1
    else: print('Sajnos nem ez a megoldás :(')



'''



class mondat():
    def __init__(self,elso,masodik,harmadik,negyedik):
        self.elso=elso
        self.masodik=masodik
        self.harmadik=harmadik
        self.negyedik=negyedik

egesz=[]
mon=[]

mondathoz=open('osszerak/mondatok.txt','r',encoding='utf-8')
for sor in mondathoz:
    sor=sor.replace('\n','')
    d=sor.split(';')
    obj=mondat(d[0],d[1],d[2],d[3])
    mon.append(obj)
    sor=sor.replace(';','')
    egesz.append(sor)


print('Ebben a játékban szétszedtunk 4db-ra egy mondatod és megcsréltük a szavait. A szavakat fogod látni a képernyőn. írd be a helyes mondatot')
osszerakpontok=0

fel=1

for x in range(len(mon)):
    ossze=[]
    kulon=[]
    while len(ossze)!=4:
        kulon.append(mon[x].elso)
        kulon.append(mon[x].masodik)
        kulon.append(mon[x].harmadik)
        kulon.append(mon[x].negyedik)
        randba=random.choice(kulon)
        if randba not in ossze: ossze.append(randba)
    print('{}. feladat: {} {} {} {}'.format(fel,ossze[0],ossze[1],ossze[2],ossze[3]))
    be=input('\n\tMegfejtés: ')
    print()
    if be==egesz[x]:
        print('A megoldás helyes')
        osszerakpontok+=1
    else: print('A megoldás nem helyes :(\n A helyes megfejtés: {}\n\n'.format(egesz[x])) 
    fel+=1

def mennyirejo(a):
    if a>20: return 'Nagyon ügyes voltál'
    if a<20: return 'Egy kicsi gyakorlással még jobban fog menni'
    if a<10: return 'Vannak gondok....'


print('E játék végére {} pontod lett, {}'.format(osszerakpontok,mennyirejo(osszerakpontok)))