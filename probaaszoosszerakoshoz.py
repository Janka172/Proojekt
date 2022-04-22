import random

mondathoz=open('osszerak/mondatok.txt','r',encoding='utf-8')

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


def mennyirejo(a):
    if a>20: return 'Nagyon ügyes voltál'
    if a<20: return 'Egy kicsi gyakorlással még jobban fog menni'
    if a<10: return 'Vannak gondok....'


print('E játék végére {} pontod lett, {}'.format(osszerakpontok,mennyirejo(osszerakpontok)))