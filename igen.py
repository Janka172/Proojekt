class gyil1:
    def __init__(self,cim,tobbi):
        self.cim=cim
        self.tobbi=tobbi

class gyil2:
    def __init__(self,ciim,szoveg,elkov):
        self.ciim=ciim
        self.szoveg=szoveg
        self.elkov=elkov

class gyilker:
    def __init__(self,kerdes,gyv):
        self.kerdes=kerdes
        self.gyv=gyv



gyilo1=[]
f=open("fajlok/gyilkosok1.txt","r",encoding="utf-8")
for sor in f:
    sor=sor.replace("\n","")
    d=sor.split(";")
    obj=gyil1(d[0],d[1])
    gyilo1.append(obj)
f.close

gyilo2=[]
f=open("fajlok/gyilkosok2.txt","r",encoding="utf-8")
for sor in f:
    sor=sor.replace("\n","")
    d=sor.split(";")
    obj=gyil2(d[0],d[1],d[2])
    gyilo2.append(obj)
f.close

gyilo3=[]
f=open("fajlok/gyilkosok3.txt","r",encoding="utf-8")
for sor in f:
    sor=sor.replace("\n","")
    d=sor.split(";")
    obj=gyilker(d[0],d[1])
    gyilo3.append(obj)
f.close



for elem in gyilo1:
    print("\n\t{}\n{}".format(elem.cim,elem.tobbi))
    eleje=input('[TOVÁBB]')
    while eleje!='':
        print('[ENTER] billentyűt kell megnyomnod! Különben nem fog tovább menni a szöveg.')
        eleje=input('[Nyomd meg az ENTERT]')
teszt=input('Ki akarod tölteni a tesztet vagy tovább kutakodsz a témában? [teszt/tovább] ')
if teszt=='teszt':
    pont=0
    for x in range(3):
        valasz=input("{}\t".format(gyilo3[x].kerdes))
        valasz.lower()
        if valasz==gyilo3[x].gyv:
            print("A válasz helyes.")
            pont+=1
        else:
            print("A válasz hibás, a helyes válasz: {}\n".format(gyilo3[x].gyv))
    print("\nPontjaid: {}/3".format(pont))

if teszt=='tovább':
    for elem in gyilo2:
        print("\n\t{}\n{}\n\t{}".format(elem.ciim,elem.szoveg,elem.elkov))
        eleje=input('[TOVÁBB]')
        while eleje!='':
            print('[ENTER] billentyűt kell megnyomnod! Különben nem fog tovább menni a szöveg.')
            eleje=input('[Nyomd meg az ENTERT]')
    teszt=input('Ki akarod tölteni a tesztet? [i/n] ')
    if teszt=='i':
        pont=0
        for elem in gyilo3:
            valasz=input("{}\t".format(elem.kerdes))
            valasz.lower()
            if valasz==elem.gyv:
                print("A válasz helyes.")
                pont+=1
            else:
                print("A válasz hibás, a helyes válasz: {}\n".format(elem.gyv))
        print("\nPontjaid: {}/7".format(pont))