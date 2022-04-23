import random

class loszo:
    def __init__(self,magyar,angol):
        self.magyar=magyar
        self.angol=angol
class etelszo:
    def __init__(self,magyar,angol):
        self.magyar=magyar
        self.angol=angol
class ruhaszo:
    def __init__(self,magyar,angol):
        self.magyar=magyar
        self.angol=angol
class butorszo:
    def __init__(self,magyar,angol):
        self.magyar=magyar
        self.angol=angol
class allatszo:
    def __init__(self,magyar,angol):
        self.magyar=magyar
        self.angol=angol

class mondat():
    def __init__(self,elso,masodik,harmadik,negyedik):
        self.elso=elso
        self.masodik=masodik
        self.harmadik=harmadik
        self.negyedik=negyedik


nem=input('Angolul [1] akarsz tanulni vagy a Tehenekről [2]: ')
if nem=='1':
    igen=input('Melyik feladattípussal akarsz gyakorolni?\n\t1: Mondatösszerakás\n\t2: Szavak\n\t3: Mondatkiegészítés\n\t')


    if igen=='2':
        melyik=99
        while int(melyik)<1 or int(melyik)>=6:
            print("Írd le a megadott szavakat angolul!")
            print("Témajörök:\n\t1: Lovak\n\t2: Ételek\n\t3: Ruhák\n\t4: Bútorok\n\t5: Állatok")
            melyik=input("Melyik témakört akarod gyakorolni? ")
        meg="i"

        while meg=="i":
            if melyik=="1":
                pont=0
                f=open("fajlok/lo.txt","r",encoding="utf-8")
                L1=[]
                for sor in f:
                    sor=sor.replace("\n","")
                    d=sor.split(" ")
                    obj=loszo(d[0],d[1])
                    L1.append(obj)
                f.close
                for elem in L1:
                    valasz=input("{} : ".format(elem.magyar))
                    if valasz==elem.angol:
                        print("A válasz helyes.")
                        pont+=1
                    else:
                        print("A válasz hibás, a helyes válasz: ",elem.angol)
                print("Pontjaid: {}/20".format(pont))
            elif melyik=="2":
                pont=0
                f=open("fajlok/etel.txt","r",encoding="utf-8")
                L1=[]
                for sor in f:
                    sor=sor.replace("\n","")
                    d=sor.split(" ")
                    obj=etelszo(d[0],d[1])
                    L1.append(obj)
                f.close
                for elem in L1:
                    valasz=input("{} : ".format(elem.magyar))
                    if valasz==elem.angol:
                        print("A válasz helyes.")
                        pont+=1
                    else:
                        print("A válasz hibás, a helyes válasz: ",elem.angol)
                print("Pontjaid: {}/20".format(pont))
            elif melyik=="3":
                pont=0
                f=open("fajlok/ruha.txt","r",encoding="utf-8")
                L1=[]
                for sor in f:
                    sor=sor.replace("\n","")
                    d=sor.split(" ")
                    obj=ruhaszo(d[0],d[1])
                    L1.append(obj)
                f.close
                for elem in L1:
                    valasz=input("{} : ".format(elem.magyar))
                    if valasz==elem.angol:
                        print("A válasz helyes.")
                        pont+=1
                    else:
                        print("A válasz hibás, a helyes válasz: ",elem.angol)
                print("Pontjaid: {}/20".format(pont))
            elif melyik=="4":
                pont=0
                f=open("fajlok/butor.txt","r",encoding="utf-8")
                L1=[]
                for sor in f:
                    sor=sor.replace("\n","")
                    d=sor.split(" ")
                    obj=butorszo(d[0],d[1])
                    L1.append(obj)
                f.close
                for elem in L1:
                    valasz=input("{} : ".format(elem.magyar))
                    if valasz==elem.angol:
                        print("A válasz helyes.")
                        pont+=1
                    else:
                        print("A válasz hibás, a helyes válasz: ",elem.angol)
                print("Pontjaid: {}/20".format(pont))
            elif melyik=="5":
                pont=0
                f=open("fajlok/allat.txt","r",encoding="utf-8")
                L1=[]
                for sor in f:
                    sor=sor.replace("\n","")
                    d=sor.split(" ")
                    obj=allatszo(d[0],d[1])
                    L1.append(obj)
                f.close
                for elem in L1:
                    valasz=input("{} : ".format(elem.magyar))
                    if valasz==elem.angol:
                        print("A válasz helyes.")
                        pont+=1
                    else:
                        print("A válasz hibás, a helyes válasz: ",elem.angol)
                print("Pontjaid: {}/20".format(pont))
            else:
                while melyik!=1 or melyik!=2 or melyik!=3 or melyik!=4 or melyik!=5:
                    melyik=input("Ez a szám nem jelül meg egy témakört sem!\nTémajörök:\n\t1: Lovak\n\t2: Ételek\n\t3: Ruhák\n\t4: Bútorok\n\t5: Állatok\nMelyik témakört akarod gyakorolni? ")
            meg=input("Szeretnél még szavakat gyakorolni? [i/n] ")
            while meg!="i" and meg!="n":
                meg=input("Szeretnél még szavakat gyakorolni? [i/n] ")
            if meg=="i":
                melyik=int(input("\nTémajörök:\n\t1: Lovak\n\t2: Ételek\n\t3: Ruhák\n\t4: Bútorok\n\t5: Állatok\nMelyik témakört akarod gyakorolni? "))
    elif igen=='1':
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
        mondathoz.close()

        print('Ebben a játékban szétszedtunk 4db-ra egy mondatod és megcseréltük a szavait. A szavakat fogod látni a képernyőn. írd be a helyes mondatot')
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
            if a>10 and a<20: return 'Egy kicsi gyakorlással még jobban fog menni'
            if a<10: return 'Vannak gondok....'

        print('A játék végére {} pontod lett. {}'.format(osszerakpontok,mennyirejo(osszerakpontok)))
    elif igen=='3':
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
elif nem=='2': 
    class tehen:
        def __init__(self,cim,szoveg,hires):
            self.cim=cim
            self.szoveg=szoveg
            self.hires=hires
    class tehenteszt:
        def __init__(self,kerdes,valasz):
            self.kerdes=kerdes
            self.valasz=valasz
    ujra='i'
    te=172
    while True:
        while te>2 or te<0:
            te=int(input("Elolvasod az oktató anyagot[1] vagy kitöltesz róla egy tesztet[2]?"))
        if te==1:
            L=[]
            f=open("fajlok/tehen.txt","r",encoding="utf-8")
            for sor in f:
                sor=sor.replace("\n","")
                d=sor.split(";")
                obj=tehen(d[0],d[1],d[2])
                L.append(obj)
            f.close
            for elem in L:
                print("\t{}\n{}".format(elem.cim,elem.szoveg))
            print("\tHíres tehenek:")
            for elem in L:
                print("- ",elem.hires)
        elif te==2:
            L=[]
            f=open("fajlok/teszt.txt","r",encoding="utf-8")
            for sor in f:
                sor=sor.replace("\n","")
                d=sor.split(";")
                obj=tehenteszt(d[0],d[1])
                L.append(obj)
            f.close
            pont=0
            for elem in L:
                valasz=input("{}\n\t".format(elem.kerdes))
                valasz.lower()
                if valasz==elem.valasz:
                    print("A válasz helyes.")
                    pont+=1
                else:
                    print("A válasz hibás, a helyes válasz: ",elem.valasz)
            print("Pontjaid: {}/5".format(pont))
        ujra=input("Szeretnél még szavakat gyakorolni? [i/n] ")
        while ujra!="i" and ujra!="n":
            ujra=input("Szeretnél még szavakat gyakorolni? [i/n] ")
        if ujra=="i":
            melyik=input("VÁLASZTÓS IZÉ HELYE")