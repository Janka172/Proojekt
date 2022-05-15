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
class mondat:
    def __init__(self,elso,masodik,harmadik,negyedik):
        self.elso=elso
        self.masodik=masodik
        self.harmadik=harmadik
        self.negyedik=negyedik
def mennyirejo(a):
                if a>=3: return 'Nagyon ügyes voltál'
                if a==2: return 'Egy kicsi gyakorlással még jobban fog menni'
                if a<1: return 'Vannak gondok....'

a="""
██████╗░██████╗░░█████╗░░░░░░██╗███████╗██╗░░██╗████████╗
██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██║░██╔╝╚══██╔══╝
██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░█████═╝░░░░██║░░░
██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██╔═██╗░░░░██║░░░
██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗██║░╚██╗░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░
""" 
print(a)

print('Bevezető a programhoz.\n A következőkben a program használatáról fogtok tanulni.\nAmikor kiválasztjátok az oktatóanyag elolvasását, nem az egész szöveg jelenik majd meg. Látni fogsz egy [TOVÁBB] feliratot, ilyenkor megkell nyomnod majd az [ENTER]-t, ez fogja felhozni a többi szövegrészt.\nMost pedig gyakoroljuk.')

f=open('fajlok/eleje.txt','r',encoding='utf-8')




for sor in f:
    sor=sor.replace('\n','')
    print(sor)
    eleje=input('[TOVÁBB]')
    while eleje!='':
        print('[ENTER] billentyűt kell megnyomnod! Különben nem fog tovább menni a szöveg.')
        eleje=input('[NYomd meg az ENTERT]')


#Gyilkosok

ujra='i'
while ujra=="i":
    nem=input('Miről akarsz tanulni?\n\t1: Angolul\n\t2: Állatokról\n\t3: Gyilkosok')
    if nem=='1':
        igen=input('Melyik feladattípussal akarsz gyakorolni?\n\t1: Mondatösszerakás\n\t2: Szavak\n\t3: Mondatkiegészítés\n\t4: Nyelvi színtfelmérő')
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
        elif igen=='4':
            pass
    elif nem=='2': 
        tipus=int(input("Melyik állat típusról szeretnél tanulni?\n\t1: Háziállat\n\t2: Vadállat\n\t"))
        while tipus<1 or tipus>2:
            tipus=int(input("Melyik állat típusról szeretnél tanulni?\n\t1: Háziállat\n\t2: Vadállat\n\t"))
        if tipus==1:
            allat=int(input("Melyik állatról szeretnél tanulni?\n\t1: Tehén\n\t2: Ló\n\t3: Kecske\n\t"))
            while allat<1 or allat>3:
                allat=int(input("Melyik állatról szeretnél tanulni?\n\t1: Tehén\n\t2: Ló\n\t3: Kecske\n\t"))
            if allat==1:
                class tehen:
                    def __init__(self,cim,szoveg,hires):
                        self.cim=cim
                        self.szoveg=szoveg
                        self.hires=hires
                class tehenteszt:
                    def __init__(self,kerdes,valasz):
                        self.kerdes=kerdes
                        self.valasz=valasz
                te=172
                teszt='kecske'
                while te>2 or te<0:
                    te=int(input("Elolvasod az oktató anyagot[1] vagy kitöltesz róla egy tesztet[2]? "))
                if te==1:
                    L=[]
                    f=open("fajlok/tehen.txt","r",encoding="utf-8")
                    for sor in f:
                        sor=sor.replace("\n","")
                        d=sor.split(";")
                        obj=tehen(d[0],d[1],d[2])
                        L.append(obj)
                    f.close
                    a="""
                    ▒▒▒▒▒▒                            ████████████████████████████████                
                    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                ██████████          ██████████    ██              
                    ░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ████████████            ██████        ██            
                    ░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████                            ██            
                    ░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒████████                    ██        ██    ██      
                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████                    ██████        ██    ██████  
                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██            ████    ██      ██████████████      ██
                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██          ████████    ████      ██████████    ██  
                    ▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░██        ██████████    ██████      ██████      ██  
                    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░██          ██████      ████████  ██  ██  ██    ██  
                    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒░░████            ██        ██████  ████    ████    ██  
                    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒██▒▒██  ██                      ████                    ██  
                        ▒▒▒▒▒▒▒▒████████  ██    ██      ██              ██          ██████      ██  
                                    ██████      ████  ████████            ████      ██▒▒▒▒▒▒██  ██    
                                ████    ██████    ████████████              ██    ████▒▒██████      
                                                ██  ████████████████████████████████▒▒▒▒▒▒██        
                                                ██    ██  ██    ██            ██      ██████  ██      
                                                ██    ██    ██  ██              ██  ██    ██    ██    
                                                ████        ████                ████      ████      
                    """ 
                    print(a)
                    for elem in L:
                        print("\n\t{}\n{}".format(elem.cim,elem.szoveg))
                        eleje=input('[TOVÁBB]')
                        while eleje!='':
                            print('[ENTER] billentyűt kell megnyomnod! Különben nem fog tovább menni a szöveg.')
                            eleje=input('[NYomd meg az ENTERT]')
                    print("\n\tHíres tehenek:")
                    for elem in L:
                        print("- ",elem.hires)
                    teszt=input('Ki akarod tölteni a tesztet? [i/n] ')

                    if teszt=='i':
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
                        print("\nPontjaid: {}/5, {}".format(pont,mennyirejo(pont)))
                elif te==2: print('Nem töltheted ki a tesztet ismeretek nélkül! >:(')
            if allat==2:
                igen2=int(input("Összefoglalónak akarsz tanuni a lovakról[1], vagy híres versenylovakról[2]? "))
                while igen2>2 or igen2<0:
                    igen2=int(input("Összefoglalónak akarsz tanuni a lovakról[1], vagy híres versenylovakról[2]? "))
                if igen2==1:
                    class lo:
                        def __init__(self,cim,altipus,tipusszoveg,hasznostip,hasznosleiras,elnevezesek,torzsfejlodes,vadlovak):
                            self.cim=cim
                            self.altipus=altipus
                            self.tipusszoveg=tipusszoveg
                            self.hasznostip=hasznostip
                            self.hasznosleiras=hasznosleiras
                            self.elnevezesek=elnevezesek
                            self.torzsfejlodes=torzsfejlodes
                            self.vadlovak=vadlovak
                    class loteszt:
                        def __init__(self,kerdes,valasz):
                            self.kerdes=kerdes
                            self.valasz=valasz
                    te=172
                    teszt='kecske'
                    while te>2 or te<0:
                        te=int(input("Elolvasod az oktató anyagot[1] vagy kitöltesz róla egy tesztet[2]? "))
                    if te==1:
                        L=[]
                        f=open("fajlok/loo.txt","r",encoding="utf-8")
                        for sor in f:
                            sor=sor.replace("\n","")
                            d=sor.split(";")
                            obj=lo(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7])
                            L.append(obj)
                        f.close
                        a="""
                        ░░░░  ░░░░░░░░  ░░░░░░░░    ░░░░░░░░░░░░░░      ░░░░  ░░░░░░
                        ░░░░    ░░░░░░▒▒▒▒▒▒▒▒██▒▒▒▒░░░░░░░░  ░░        ░░░░    ░░░░
                        ░░░░    ░░░░▒▒██████████████▓▓▓▓▓▓▓▓▓▓░░░░      ░░░░    ░░░░
                        ░░      ░░████████▒▒▓▓▒▒▒▒▒▒▒▒██████████████    ░░          
                        ▒▒██  ██████▒▒██▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████              
                        ▒▒░░████▓▓▒▒▒▒██▒▒████████████████▒▒▒▒▒▒▒▒████            
                        ░░▒▒▒▒▒▒██▓▓▒▒██▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒██████▓▓▒▒▒▒▒▒██▓▓░░    ░░░░
                            ██▒▒██▓▓▒▒██▒▒▒▒▓▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒██████▒▒▒▒██▓▓        
                        ░░    ████▓▓▒▒██░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒████      
                                ▓▓▒▒▓▓██░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒████    
                        ░░      ▓▓▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒██░░░░
                        ░░░░  ░░██▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓██▓▓░░
                        ░░░░  ██▓▓▓▓▒▒░░░░▒▒▒▒▒▒░░▒▒░░▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓██░░
                        ░░░░  ▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒██▓▓▒▒▒▒▒▒░░▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓░░
                        ░░░░  ░░██▒▒░░░░░░▓▓██▓▓▒▒▒▒██▒▒▒▒▒▒░░▒▒░░░░░░░░▒▒▒▒▒▒▒▒██░░
                        ░░░░  ░░▓▓▒▒░░░░░░██▓▓▒▒▒▒▒▒██▒▒▒▒▒▒░░▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒██░░
                        ░░      ▓▓░░░░░░░░▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓  
                        ░░░░░░░░▓▓▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓██▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▓▓░░
                        ░░░░  ░░▓▓░░░░░░░░▒▒▒▒▒▒▒▒██▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▓▓░░
                        ░░░░  ░░▓▓░░░░░░▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒░░░░░░▓▓░░
                        ░░░░  ░░▓▓░░░░  ░░▒▒▒▒▒▒░░  ██▒▒▒▒▒▒▒▒░░▒▒░░░░░░▒▒░░░░░░▓▓░░
                        ░░░░░░░░▓▓░░░░░░░░░░▒▒▒▒░░  ▒▒▓▓▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░
                        ░░░░  ▒▒▒▒░░░░    ░░▒▒░░      ██▒▒▒▒▒▒▒▒░░░░░░░░▒▒░░░░░░▓▓░░
                        ░░░░  ██░░░░██▒▒  ▓▓░░░░      ▒▒██▓▓▒▒▒▒░░░░░░░░░░░░░░░░▓▓░░
                        ░░░░░░▒▒▒▒░░▒▒██░░██░░░░░░░░░░░░▓▓██▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░▓▓░░
                        ░░░░    ▒▒░░▒▒▒▒░░██░░░░      ░░░░██▒▒▒▒▒▒░░░░░░░░░░░░░░▓▓░░
                        ░░░░    ░░▒▒▒▒██▓▓▒▒░░░░      ░░░░██▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓░░
                        ░░░░    ░░░░░░░░░░░░░░░░    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                        """ 
                        print(a)
                        darab=0
                        for elem in L:
                            darab+=1
                            if darab==1:
                                print("\n\t\t{}".format(elem.cim))
                                for elem in L:
                                    print("\t{}\n{}".format(elem.altipus,elem.tipusszoveg))
                                print("\n\tHasznosítási típusok")
                                for elem in L:
                                    print("{}:\n\t{}".format(elem.hasznostip,elem.hasznosleiras))
                            if darab==2:
                                print("\t\t{}".format(elem.cim))
                                for elem in L:
                                    print("\t{}".format(elem.elnevezesek))
                            if darab==3:
                                print("\t\t{}".format(elem.cim))
                                for elem in L:
                                    print("\t{}".format(elem.torzsfejlodes))
                            if darab==4:
                                print("\t\t{}".format(elem.cim))
                                for elem in L:
                                    print("\t{}".format(elem.vadlovak))
                        teszt=input('Ki akarod tölteni a tesztet? [i/n] ')
                        if teszt=='i':
                            L=[]
                            f=open("fajlok/loteszt.txt","r",encoding="utf-8")
                            for sor in f:
                                sor=sor.replace("\n","")
                                d=sor.split(";")
                                obj=loteszt(d[0],d[1])
                                L.append(obj)
                            f.close
                            pont=0
                            for elem in L:
                                valasz=input("{}\t".format(elem.kerdes))
                                valasz.lower()
                                if valasz==elem.valasz:
                                    print("A válasz helyes.")
                                    pont+=1
                                else:
                                    print("A válasz hibás, a helyes válasz: {}\n".format(elem.valasz))
                            print("Pontjaid: {}/5, {}".format(pont,mennyirejo(pont)))
                    elif te==2: print('Nem töltheted ki a tesztet ismeretek nélkül! >:(')
                if igen2==2:
                    igen5=int(input("Milyen szakágban?\n\t1: Galopp\n\t2: Díjlovaglás\n\t3: Díjugratás\n\t\n"))
                    while igen5>3 or igen5<0:
                        igen5=int(input("Milyen szakágban?\n\t1: Galopp\n\t2: Díjlovaglás\n\t3: Díjugratás\n\t\n"))
                    if igen5==1:
                        a="""
                                                                                                      
                                                                                ▒▒▒▒                
                                                                    ░░▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒                
                                                                ▒▒▒▒▒▒████▒▒▒▒▓▓▓▓▓▓        ░░      
                                                                ▓▓▓▓░░██░░▓▓▓▓  ░░    ▒▒██▓▓▓▓      
                                                                ▓▓▓▓▒▒▒▒▒▒▓▓        ▓▓██▓▓▓▓▓▓▒▒    
                                                                    ▓▓▒▒▒▒▒▒▓▓░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    
                                                    ░░░░░░░░░░  ░░░░██▒▒▒▒▓▓██▓▓██▓▓▓▓▓▓██▓▓▓▓▓▓▒▒  
                                                ░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒
                                            ░░▒▒░░▒▒▒▒▓▓▓▓▒▒▒▒▓▓░░░░░░▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒    ██▒▒▓▓
                                        ▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▒▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓██          ░░  
                                    ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░▒▒▒▒▓▓▓▓▓▓▒▒▒▒▓▓▓▓▒▒            
                            ░░░░▒▒▓▓████░░      ██▓▓██▓▓▓▓▓▓▓▓▓▓▒▒▓▓████▓▓████▓▓▓▓▓▓▓▓  ░░            
                        ░░▓▓▓▓██▒▒              ▒▒▓▓▓▓██▓▓▓▓▒▒██▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓                
                        ░░                        ████▓▓▓▓▓▓    ▒▒██████▓▓██▓▓▓▓▓▓▒▒                
                                                ░░██████▓▓▒▒          ▓▓████▓▓▓▓▒▒                  
                                                ████▓▓░░▓▓██              ████░░▓▓▓▓                  
                                                ████  ▓▓████              ▓▓██  ░░▓▓▒▒                
                                                ░░██  ████▒▒              ▓▓▓▓      ▓▓                
                                                ░░▓▓  ▓▓▓▓              ░░▓▓      ██                
                                                    ██    ▒▒▓▓            ░░▓▓    ▒▒▒▒                
                                                    ▒▒▒▒    ▒▒▓▓▒▒▓▓▓▓▓▓▒▒▓▓    ▒▒▓▓                  
                                                    ░░      ▓▓░░  ░░░░    ░░▒▒▒▒                    
                                                    ░░          ░░                                    
                        """ 
                        print(a)
                        igen3=int(input("Magyar[1] vagy külföldi[2] versenylóról akarsz tanulni? "))
                        while igen3>2 or igen3<0:
                            igen3=int(input("Magyar[1] vagy külföldi[2] versenylóról akarsz tanulni? "))
                        if igen3==1:
                            igen4=int(input("Melyik ló érdekel?\n\t1: Kincsem\n\t2: Overdose\n\t3: Imperiál\n\t"))
                            while igen4>3 or igen4<0:
                                igen4=int(input("Melyik ló érdekel?\n\t1: Kincsem\n\t2: Overdose\n\t3: Imperiál\n\t"))
                            if igen4==1:
                                class kincsem:
                                    def __init__(self,cim,szoveg,kerdes,valasz):
                                        self.cim=cim
                                        self.szoveg=szoveg
                                        self.kerdes=kerdes
                                        self.valasz=valasz
                                L=[]
                                f=open("fajlok/lovak/overdose.txt","r",encoding="utf-8")
                                for sor in f:
                                    sor=sor.replace("\n","")
                                    d=sor.split(";")
                                    obj=kincsem(d[0],d[1],d[2],d[3])
                                    L.append(obj)
                                f.close
                                for elem in L:
                                    print("\n\t{}\n{}".format(elem.cim,elem.szoveg))
                                    eleje=input('[TOVÁBB]')
                                    while eleje!='':
                                        print('[ENTER] billentyűt kell megnyomnod! Különben nem fog tovább menni a szöveg.')
                                        eleje=input('[NYomd meg az ENTERT]')
                                teszt=input('Ki akarod tölteni a tesztet? [i/n] ')
                                if teszt=='i':
                                    pont=0
                                    for elem in L:
                                        valasz=input("{}\t".format(elem.kerdes))
                                        valasz.lower()
                                        if valasz==elem.valasz:
                                            print("A válasz helyes.")
                                            pont+=1
                                        else:
                                            print("A válasz hibás, a helyes válasz: {}\n".format(elem.valasz))
                                    print("\nPontjaid: {}/4, {}".format(pont,mennyirejo(pont)))
                            if igen4==2:
                                class overdose:
                                    def __init__(self,cim,szoveg,kerdes,valasz):
                                        self.cim=cim
                                        self.szoveg=szoveg
                                        self.kerdes=kerdes
                                        self.valasz=valasz
                                L=[]
                                f=open("fajlok/lovak/overdose.txt","r",encoding="utf-8")
                                for sor in f:
                                    sor=sor.replace("\n","")
                                    d=sor.split(";")
                                    obj=overdose(d[0],d[1],d[2],d[3])
                                    L.append(obj)
                                f.close
                                for elem in L:
                                    print("\n\t{}\n{}".format(elem.cim,elem.szoveg))
                                    eleje=input('[TOVÁBB]')
                                    while eleje!='':
                                        print('[ENTER] billentyűt kell megnyomnod! Különben nem fog tovább menni a szöveg.')
                                        eleje=input('[NYomd meg az ENTERT]')
                                teszt=input('Ki akarod tölteni a tesztet? [i/n] ')
                                if teszt=='i':
                                    pont=0
                                    for elem in L:
                                        valasz=input("{}\t".format(elem.kerdes))
                                        valasz.lower()
                                        if valasz==elem.valasz:
                                            print("A válasz helyes.")
                                            pont+=1
                                        else:
                                            print("A válasz hibás, a helyes válasz: {}\n".format(elem.valasz))
                                    print("\nPontjaid: {}/3, {}".format(pont,mennyirejo(pont)))
                            if igen4==3:
                                class imperial:
                                    def __init__(self,cim,szoveg,kerdes,valasz):
                                        self.cim=cim
                                        self.szoveg=szoveg
                                        self.kerdes=kerdes
                                        self.valasz=valasz
                                L=[]
                                f=open("fajlok/lovak/imperial.txt","r",encoding="utf-8")
                                for sor in f:
                                    sor=sor.replace("\n","")
                                    d=sor.split(";")
                                    obj=imperial(d[0],d[1],d[2],d[3])
                                    L.append(obj)
                                f.close
                                for elem in L:
                                    print("\n\t{}\n{}".format(elem.cim,elem.szoveg))
                                    eleje=input('[TOVÁBB]')
                                    while eleje!='':
                                        print('[ENTER] billentyűt kell megnyomnod! Különben nem fog tovább menni a szöveg.')
                                        eleje=input('[NYomd meg az ENTERT]')
                                teszt=input('Ki akarod tölteni a tesztet? [i/n] ')
                                if teszt=='i':
                                    pont=0
                                    for elem in L:
                                        valasz=input("{}\t".format(elem.kerdes))
                                        valasz.lower()
                                        if valasz==elem.valasz:
                                            print("A válasz helyes.")
                                            pont+=1
                                        else:
                                            print("A válasz hibás, a helyes válasz: {}\n".format(elem.valasz))
                                    print("\nPontjaid: {}/4, {}".format(pont,mennyirejo(pont)))
                        if igen3==2:
                            igen4=int(input("Melyik ló érdekel?\n\t1: Sodashi\n\t2: Secretariat\n\t3: Ruffian\n\t"))
                            while igen4>3 or igen4<0:
                                igen4=int(input("Melyik ló érdekel?\n\t1: Sodashi\n\t2: Secretariat\n\t3: Ruffian\n\t"))
                            if igen4==1:
                                class sodashi:
                                    def __init__(self,cim,szoveg,kerdes,valasz):
                                        self.cim=cim
                                        self.szoveg=szoveg
                                        self.kerdes=kerdes
                                        self.valasz=valasz
                                L=[]
                                f=open("fajlok/lovak/sodashi.txt","r",encoding="utf-8")
                                for sor in f:
                                    sor=sor.replace("\n","")
                                    d=sor.split(";")
                                    obj=sodashi(d[0],d[1],d[2],d[3])
                                    L.append(obj)
                                f.close
                                for elem in L:
                                    print("\n\t{}\n{}".format(elem.cim,elem.szoveg))
                                    eleje=input('[TOVÁBB]')
                                    while eleje!='':
                                        print('[ENTER] billentyűt kell megnyomnod! Különben nem fog tovább menni a szöveg.')
                                        eleje=input('[NYomd meg az ENTERT]')
                                teszt=input('Ki akarod tölteni a tesztet? [i/n] ')
                                if teszt=='i':
                                    pont=0
                                    for elem in L:
                                        valasz=input("{}\t".format(elem.kerdes))
                                        valasz.lower()
                                        if valasz==elem.valasz:
                                            print("A válasz helyes.")
                                            pont+=1
                                        else:
                                            print("A válasz hibás, a helyes válasz: {}\n".format(elem.valasz))
                                    print("\nPontjaid: {}/3, {}".format(pont,mennyirejo(pont)))
                            if igen4==2:
                                class secretariat:
                                    def __init__(self,cim,szoveg,kerdes,valasz):
                                        self.cim=cim
                                        self.szoveg=szoveg
                                        self.kerdes=kerdes
                                        self.valasz=valasz
                                L=[]
                                f=open("fajlok/lovak/secretariat.txt","r",encoding="utf-8")
                                for sor in f:
                                    sor=sor.replace("\n","")
                                    d=sor.split(";")
                                    obj=secretariat(d[0],d[1],d[2],d[3])
                                    L.append(obj)
                                f.close
                                for elem in L:
                                    print("\n\t{}\n{}".format(elem.cim,elem.szoveg))
                                    eleje=input('[TOVÁBB]')
                                    while eleje!='':
                                        print('[ENTER] billentyűt kell megnyomnod! Különben nem fog tovább menni a szöveg.')
                                        eleje=input('[NYomd meg az ENTERT]')
                                teszt=input('Ki akarod tölteni a tesztet? [i/n] ')
                                if teszt=='i':
                                    pont=0
                                    for elem in L:
                                        valasz=input("{}\t".format(elem.kerdes))
                                        valasz.lower()
                                        if valasz==elem.valasz:
                                            print("A válasz helyes.")
                                            pont+=1
                                        else:
                                            print("A válasz hibás, a helyes válasz: {}\n".format(elem.valasz))
                                    print("\nPontjaid: {}/3, {}".format(pont,mennyirejo(pont)))
                            if igen4==3:
                                class ruffian:
                                    def __init__(self,cim,szoveg,kerdes,valasz):
                                        self.cim=cim
                                        self.szoveg=szoveg
                                        self.kerdes=kerdes
                                        self.valasz=valasz
                                L=[]
                                f=open("fajlok/lovak/ruffian.txt","r",encoding="utf-8")
                                for sor in f:
                                    sor=sor.replace("\n","")
                                    d=sor.split(";")
                                    obj=ruffian(d[0],d[1],d[2],d[3])
                                    L.append(obj)
                                f.close
                                for elem in L:
                                    print("\n\t{}\n{}".format(elem.cim,elem.szoveg))
                                    eleje=input('[TOVÁBB]')
                                    while eleje!='':
                                        print('[ENTER] billentyűt kell megnyomnod! Különben nem fog tovább menni a szöveg.')
                                        eleje=input('[NYomd meg az ENTERT]')
                                teszt=input('Ki akarod tölteni a tesztet? [i/n] ')
                                if teszt=='i':
                                    pont=0
                                    for elem in L:
                                        valasz=input("{}\t".format(elem.kerdes))
                                        valasz.lower()
                                        if valasz==elem.valasz:
                                            print("A válasz helyes.")
                                            pont+=1
                                        else:
                                            print("A válasz hibás, a helyes válasz: {}\n".format(elem.valasz))
                                    print("\nPontjaid: {}/4, {}".format(pont,mennyirejo(pont)))
                    if igen5==2:
                        a="""
                                                                                                                                                       
                                                                                                                    ██    ▒▒    
                                                                                                                ▓▓██▓▓▓▓      
                                                                                                                ██▓▓▓▓████      
                                                                                                            ██▓▓▓▓▒▒▓▓▓▓▒▒      
                                                                                                        ▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓      
                                                                                                    ▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒    
                                                                                                    ▓▓████▓▓▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒    
                                                                                                ▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░  
                                                                                                ▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▒▒  
                                                                                            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▒▒▓▓░░  
                                                                                        ░░▒▒▒▒▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓██    ▓▓▓▓░░▒▒▒▒
                                                        ░░░░░░▒▒▒▒░░░░░░              ░░░░░░▒▒▓▓▓▓░░▒▒▓▓▓▓▓▓▓▓██      ▓▓░░░░▒▒
                                            ▒▒▒▒▒▒▓▓▒▒▒▒░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓██        ▒▒▓▓▓▓
                                        ▓▓▓▓▓▓▓▓▓▓░░░░░░▒▒░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒░░░░░░░░░░▒▒▓▓░░▒▒▓▓▓▓██            ▒▒  
                                    ░░████████▓▓░░▓▓▒▒▒▒▒▒░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░▒▒░░░░░░░░░░▒▒▒▒░░▓▓▓▓██                
                                    ██████████▒▒▒▒▓▓▓▓▒▒░░░░▓▓▓▓▒▒▓▓▓▓▓▓░░▒▒▒▒▒▒░░░░░░▓▓▒▒▓▓▒▒░░░░░░▒▒▒▒▓▓██░░                
                                    ██████████▓▓▓▓▓▓▓▓░░░░▒▒▓▓▓▓▒▒░░░░░░░░░░░░▓▓▒▒▒▒░░▒▒▓▓▓▓▓▓▓▓▒▒░░░░▒▒▓▓██                  
                                    ▒▒██████████████▓▓▒▒▒▒▒▒████▓▓░░▒▒▓▓▒▒░░░░▒▒▒▒▒▒▒▒░░░░▒▒██▓▓▓▓▓▓▓▓▓▓░░▓▓░░                  
                                    ▓▓▓▓▓▓██████████▓▓▒▒▓▓▓▓████▓▓░░▓▓▓▓▓▓▒▒░░░░░░░░▒▒▒▒▒▒░░▓▓▓▓▓▓▓▓▓▓▒▒░░▓▓                    
                                    ▓▓▓▓▓▓██████████▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓██▓▓▒▒▓▓                    
                                    ▓▓▓▓▓▓████▒▒████▓▓▓▓▒▒▓▓██████████▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓██▓▓▓▓                    
                                ▓▓▓▓██████▒▒  ████▓▓▓▓▒▒▓▓██▒▒████████▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓                    
                                ▓▓▓▓▓▓██      ██▓▓▓▓▒▒▓▓▓▓▒▒    ██████████▓▓██▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                ▓▓▓▓▓▓██        ████▓▓▓▓▓▓██      ██████▒▒    ██▓▓████████▓▓▓▓██▓▓▓▓▓▓▓▓▒▒                      
                            ▓▓▓▓██▒▒        ▓▓██████▒▒          ██████                      ░░██▓▓▓▓▓▓▓▓▓▓                    
                            ▓▓▓▓██      ░░██████▓▓              ██████                        ████▓▓▓▓▓▓▓▓░░                  
                            ▓▓▓▓▓▓        ▓▓████▓▓                ██████                        ████    ▓▓██▓▓                  
                            ██▓▓▓▓        ████▓▓                  ██████                        ████      ▓▓▓▓░░                
                            ▓▓▓▓        ░░████                    ██████                        ████        ▓▓▓▓                
                            ▓▓░░        ▒▒██                        ██▓▓                        ████        ░░▒▒▓▓              
                            ░░          ▓▓▓▓                        ▒▒▓▓░░                      ▓▓▓▓          ▓▓▓▓▒▒            
                                        ▓▓                            ▒▒▒▒░░                  ▒▒██              ██▓▓            
                                    ▓▓▓▓                              ▓▓▒▒                  ▓▓░░              ░░▓▓            
                                    ░░  ██                              ░░▒▒░░              ░░▓▓                  ▓▓▒▒          
                                ░░                                      ▒▒▒▒          ░░▒▒▓▓                    ▒▒▓▓          
                                ▓▓▓▓                                      ░░          ░░▓▓                        ▒▒▒▒        
                                                                                ░░    ▒▒▒▒                          ▒▒▓▓        
                                                                            ░░░░                                    ▒▒▒▒      
                                                                                                                    ░░░░      
                                                                            ░░░░░░                                    ░░░░▒▒    
                                                                                                            ░░░░░░            
                        """ 
                        print(a)
                        igen4=int(input("Melyik ló érdekel?\n\t1: Totilas\n\t2: Donnerhall\n\t3: Bonfire\n\t"))
                        while igen4>3 or igen4<0:
                            igen4=int(input("Melyik ló érdekel?\n\t1: Totilas\n\t2: Donnerhall\n\t3: Bonfire\n\t"))
                        if igen4==1:
                            class Totilas:
                                def __init__(self,cim,szoveg,kerdes,valasz):
                                    self.cim=cim
                                    self.szoveg=szoveg
                                    self.kerdes=kerdes
                                    self.valasz=valasz
                            L=[]
                            f=open("fajlok/lovak/totilas.txt","r",encoding="utf-8")
                            for sor in f:
                                sor=sor.replace("\n","")
                                d=sor.split(";")
                                obj=Totilas(d[0],d[1],d[2],d[3])
                                L.append(obj)
                            f.close
                            for elem in L:
                                print("\n\t{}\n{}".format(elem.cim,elem.szoveg))
                                eleje=input('[TOVÁBB]')
                                while eleje!='':
                                    print('[ENTER] billentyűt kell megnyomnod! Különben nem fog tovább menni a szöveg.')
                                    eleje=input('[NYomd meg az ENTERT]')
                            teszt=input('Ki akarod tölteni a tesztet? [i/n] ')
                            if teszt=='i':
                                pont=0
                                for elem in L:
                                    valasz=input("{}\t".format(elem.kerdes))
                                    valasz.lower()
                                    if valasz==elem.valasz:
                                        print("A válasz helyes.")
                                        pont+=1
                                    else:
                                        print("A válasz hibás, a helyes válasz: {}\n".format(elem.valasz))
                                print("\nPontjaid: {}/3, {}".format(pont,mennyirejo(pont)))
                        if igen4==2:
                            class Donnerhall:
                                def __init__(self,cim,szoveg,kerdes,valasz):
                                    self.cim=cim
                                    self.szoveg=szoveg
                                    self.kerdes=kerdes
                                    self.valasz=valasz
                            L=[]
                            f=open("fajlok/lovak/donnerhall.txt","r",encoding="utf-8")
                            for sor in f:
                                sor=sor.replace("\n","")
                                d=sor.split(";")
                                obj=Donnerhall(d[0],d[1],d[2],d[3])
                                L.append(obj)
                            f.close
                            for elem in L:
                                print("\n\t{}\n{}".format(elem.cim,elem.szoveg))
                                eleje=input('[TOVÁBB]')
                                while eleje!='':
                                    print('[ENTER] billentyűt kell megnyomnod! Különben nem fog tovább menni a szöveg.')
                                    eleje=input('[NYomd meg az ENTERT]')
                            teszt=input('Ki akarod tölteni a tesztet? [i/n] ')
                            if teszt=='i':
                                pont=0
                                for elem in L:
                                    valasz=input("{}\t".format(elem.kerdes))
                                    valasz.lower()
                                    if valasz==elem.valasz:
                                        print("A válasz helyes.")
                                        pont+=1
                                    else:
                                        print("A válasz hibás, a helyes válasz: {}\n".format(elem.valasz))
                                print("\nPontjaid: {}/2, {}".format(pont,mennyirejo(pont)))
                        if igen4==3:
                            class Bonfire:
                                def __init__(self,cim,szoveg,kerdes,valasz):
                                    self.cim=cim
                                    self.szoveg=szoveg
                                    self.kerdes=kerdes
                                    self.valasz=valasz
                            L=[]
                            f=open("fajlok/lovak/bonifire.txt","r",encoding="utf-8")
                            for sor in f:
                                sor=sor.replace("\n","")
                                d=sor.split(";")
                                obj=Bonfire(d[0],d[1],d[2],d[3])
                                L.append(obj)
                            f.close
                            for elem in L:
                                print("\n\t{}\n{}".format(elem.cim,elem.szoveg))
                                eleje=input('[TOVÁBB]')
                                while eleje!='':
                                    print('[ENTER] billentyűt kell megnyomnod! Különben nem fog tovább menni a szöveg.')
                                    eleje=input('[NYomd meg az ENTERT]')
                            class Bonfireeredmeny:
                                def __init__(self,szoveg):
                                    self.szoveg=szoveg
                            L2=[]
                            f=open("fajlok/lovak/bonfireeredmeny.txt","r",encoding="utf-8")
                            for sor in f:
                                sor=sor.replace("\n","")
                                d=sor.split(";")
                                obj=Bonfireeredmeny(d[0])
                                L2.append(obj)
                            f.close
                            print("\n\tVersenyeredményei: ")
                            for elem in L2:
                                print("- {}".format(elem.szoveg))

                            teszt=input('Ki akarod tölteni a tesztet? [i/n] ')
                            if teszt=='i':
                                pont=0
                                for elem in L:
                                    valasz=input("{}\t".format(elem.kerdes))
                                    valasz.lower()
                                    if valasz==elem.valasz:
                                        print("A válasz helyes.")
                                        pont+=1
                                    else:
                                        print("A válasz hibás, a helyes válasz: {}\n".format(elem.valasz))
                                print("\nPontjaid: {}/2, {}".format(pont,mennyirejo(pont)))
                    if igen5==3:
                        a="""
                                                                                                                                                                                        
                                                                                                       ░░                                                        
                                                                                                   ██▓▓██▒▒▒▒▒▒▒▒        ░░░░                                  
                                                                                              ▓▓██▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▒▒░░                                    
                                                                                         ▒▒██▓▓▓▓██▓▓▓▓▒▒██▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓░░                                    
                                                                                       ▒▒▓▓▓▓██████▓▓░░██▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓                                    
                                                                                        ▒▒▒▒▓▓████████▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓░░▒▒                                  
                                                                                       ▒▒▒▒  ░░██▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒    ▓▓▒▒▓▓▒▒▒▒                                  
                                                                                           ▓▓▒▒    ▒▒▒▒▒▒▓▓▒▒▓▓▓▓░░░░░░▒▒▓▓▓▓▒▒▒▒                                  
                                                                                          ████▒▒  ██▒▒▒▒▓▓▒▒▒▒▓▓░░▒▒▒▒  ████▒▒▒▒░░                                
                                                                                        ░░██████░░██▒▒▒▒▒▒▒▒▒▒▒▒          ░░▓▓▓▓▒▒                                
                                                                                  ▒▒██░░▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒░░▒▒      ░░    ░░░░░░                                
                                                                                  ▒▒▒▒▒▒▓▓▓▓████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒      ░░                                          
                                                                              ░░▒▒▒▒▒▒▒▒██████▓▓░░▓▓▓▓██▒▒▒▒▒▒▒▒      ▒▒                                          
                                                                        ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓▒▒░░▓▓██▓▓▒▒░░▒▒░░      ▓▓░░                                        
                                                                      ▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒████▓▓░░░░▒▒██████▓▓▒▒▓▓░░    ░░                                          
                                                              ░░▓▓▓▓▓▓▒▒▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒██▓▓▒▒▒▒░░░░██▒▒▓▓▒▒▓▓▓▓░░    ░░                                          
                                                            ▓▓████▓▓██▒▒▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓██▓▓▒▒▒▒▒▒▒▒▓▓░░░░  ██▓▓▒▒    ▓▓░░                                        
                                                        ██▓▓████▓▓░░▒▒▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓████▓▓    ░░██▓▓▓▓▓▓        ▒▒                                          
                                                    ░░██▒▒████▓▓▒▒  ▓▓▒▒▓▓▒▒▒▒▒▒▒▒▓▓████▒▒▒▒      ░░▓▓████░░          ░░                                          
                                                    ▒▒▓▓████░░▓▓▒▒░░▓▓▓▓▓▓▒▒░░▒▒████                                  ▓▓                                          
                                                    ▒▒██████░░██░░  ░░██▓▓▓▓▒▒▒▒▒▒                                    ▓▓░░                                        
                                                    ░░▓▓██▒▒▓▓        ██▓▓▓▓▒▒▒▒                                      ░░                                          
                                                    ▒▒▓▓██▒▒▓▓        ▓▓▓▓▓▓▓▓▓▓                                      ░░              
                                                    ████░░▒▒        ▓▓▓▓▒▒▒▒                                          ▓▓                  
                                                    ░░██░░        ▓▓▒▒▒▒▒▒░░                                          ▓▓░░               
                                                    ░░░░▒▒▒▒    ▓▓▓▓▒▒▓▓                                              ░░               
                                                                ██▒▒▒▒                                                ▒▒                 
                                                                ██▓▓░░                                                ▓▓░░                
                                                                ██▓▓                                                  ▒▒                  
                                                                ▓▓██  ░░░░░░░░▒▒▒▒▒▒▒▒░░▒▒░░▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒       
                                                            ░░░░░░▓▓▓▓░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░░░░░      
                                                        ░░░░░░░░▒▒▓▓▓▓▒▒▒▒▒▒░░░░░░▒▒░░▒▒░░░░░░▒▒░░░░▒▒░░░░░░░░░░░░░░░░▓▓░░░░░░▒▒▒▒▒▒▒▒░░    
                                                        ░░░░▒▒▒▒▒▒▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▓▓▒▒░░░░░░░░░░░░  
                                                        ░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒░░░░▒▒░░▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒▒▒░░░░░░░░     
                                                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░░░░░▒▒░░░░░░░░░░░░░░░░      
                                                                            ░░░░░░░░░░        ░░░░░░░░              ░░                   
                                                                                                                                                                
                        """ 
                        print(a)
                        igen4=int(input("Melyik ló érdekel?\n\t1: Quidam de Revel\n\t2: Pillangó\n\t3: Weinzauber\n\t"))
                        while igen4>3 or igen4<0:
                            igen4=int(input("Melyik ló érdekel?\n\t1: Quidam de Revel\n\t2: Pillangó\n\t3: Weinzauber\n\t"))
                        if igen4==1:
                                class Quidam:
                                    def __init__(self,cim,szoveg,kerdes,valasz):
                                        self.cim=cim
                                        self.szoveg=szoveg
                                        self.kerdes=kerdes
                                        self.valasz=valasz
                                L=[]
                                f=open("fajlok/lovak/quidam.txt","r",encoding="utf-8")
                                for sor in f:
                                    sor=sor.replace("\n","")
                                    d=sor.split(";")
                                    obj=Quidam(d[0],d[1],d[2],d[3])
                                    L.append(obj)
                                f.close
                                for elem in L:
                                    print("\n\t{}\n{}".format(elem.cim,elem.szoveg))
                                    eleje=input('[TOVÁBB]')
                                    while eleje!='':
                                        print('[ENTER] billentyűt kell megnyomnod! Különben nem fog tovább menni a szöveg.')
                                        eleje=input('[NYomd meg az ENTERT]')
                                teszt=input('Ki akarod tölteni a tesztet? [i/n] ')
                                if teszt=='i':
                                    pont=0
                                    for elem in L:
                                        valasz=input("{}\t".format(elem.kerdes))
                                        valasz.lower()
                                        if valasz==elem.valasz:
                                            print("A válasz helyes.")
                                            pont+=1
                                        else:
                                            print("A válasz hibás, a helyes válasz: {}\n".format(elem.valasz))
                                    print("\nPontjaid: {}/3, {}".format(pont,mennyirejo(pont)))
                        if igen4==2:
                            class Pillangó:
                                def __init__(self,cim,szoveg,kerdes,valasz):
                                    self.cim=cim
                                    self.szoveg=szoveg
                                    self.kerdes=kerdes
                                    self.valasz=valasz
                            L=[]
                            f=open("fajlok/lovak/pillangó.txt","r",encoding="utf-8")
                            for sor in f:
                                sor=sor.replace("\n","")
                                d=sor.split(";")
                                obj=Pillangó(d[0],d[1],d[2],d[3])
                                L.append(obj)
                            f.close
                            for elem in L:
                                print("\n\t{}\n{}".format(elem.cim,elem.szoveg))
                                eleje=input('[TOVÁBB]')
                                while eleje!='':
                                    print('[ENTER] billentyűt kell megnyomnod! Különben nem fog tovább menni a szöveg.')
                                    eleje=input('[NYomd meg az ENTERT]')
                            teszt=input('Ki akarod tölteni a tesztet? [i/n] ')
                            if teszt=='i':
                                pont=0
                                for elem in L:
                                    valasz=input("{}\t".format(elem.kerdes))
                                    valasz.lower()
                                    if valasz==elem.valasz:
                                        print("A válasz helyes.")
                                        pont+=1
                                    else:
                                        print("A válasz hibás, a helyes válasz: {}\n".format(elem.valasz))
                                print("\nPontjaid: {}/3, {}".format(pont,mennyirejo(pont)))
                        if igen4==3:
                            class Weinzauber:
                                def __init__(self,cim,szoveg,kerdes,valasz):
                                    self.cim=cim
                                    self.szoveg=szoveg
                                    self.kerdes=kerdes
                                    self.valasz=valasz
                            L=[]
                            f=open("fajlok/lovak/weinzauber.txt","r",encoding="utf-8")
                            for sor in f:
                                sor=sor.replace("\n","")
                                d=sor.split(";")
                                obj=Weinzauber(d[0],d[1],d[2],d[3])
                                L.append(obj)
                            f.close
                            for elem in L:
                                print("\n\t{}\n{}".format(elem.cim,elem.szoveg))
                                eleje=input('[TOVÁBB]')
                                while eleje!='':
                                    print('[ENTER] billentyűt kell megnyomnod! Különben nem fog tovább menni a szöveg.')
                                    eleje=input('[NYomd meg az ENTERT]')
                            teszt=input('Ki akarod tölteni a tesztet? [i/n] ')
                            if teszt=='i':
                                pont=0
                                for elem in L:
                                    valasz=input("{}\t".format(elem.kerdes))
                                    valasz.lower()
                                    if valasz==elem.valasz:
                                        print("A válasz helyes.")
                                        pont+=1
                                    else:
                                        print("A válasz hibás, a helyes válasz: {}\n".format(elem.valasz))
                                print("\nPontjaid: {}/5, {}".format(pont,mennyirejo(pont)))
            if allat==3:
                class kecske:
                    def __init__(self,cim,szoveg,kerdes,valasz):
                        self.cim=cim
                        self.szoveg=szoveg
                        self.kerdes=kerdes
                        self.valasz=valasz
                L=[]
                f=open("fajlok/kecske.txt","r",encoding="utf-8")
                for sor in f:
                    sor=sor.replace("\n","")
                    d=sor.split(";")
                    obj=kecske(d[0],d[1],d[2],d[3])
                    L.append(obj)
                f.close
                a="""
                                  ████        ████                                              
                                ▓▓▒▒██      ██▒▒██                                              
                            ██▒▒██    ██▓▓▒▒██                                                
                            ██▒▒██    ██▒▒▒▒██                                                  
                            ██▒▒██    ██▒▒▒▒██                                                  
                            ██▒▒██    ██▒▒▒▒██                                                  
                            ██▒▒██    ██▒▒▒▒██                                                  
                            ██████████████████                                                  
                    ██████              ░░░░██                                                
                    ██  ██                    ████                                              
                ██  ░░██                        ██                                            
                ██░░░░██                      ██░░  ██                                          
                ██████                ░░    ████░░░░██                                        
                    ██                    ░░  ██  ████                                          
                    ██      ██    ██          ██                                      ████      
                    ██      ██    ██          ██                                    ██    ██    
                    ██                          ██                                    ██    ██  
                ██              ░░░░    ░░░░    ██████                              ██    ██  
                ██            ░░░░░░░░░░░░░░░░░░      ████████  ░░        ██████████    ██    
                ██                  ░░░░▒▒██    ░░    ░░  ░░░░██████▓▓████  ░░        ██      
                ██          ░░░░░░░░░░▒▒▒▒██░░░░░░░░░░░░  ░░░░  ░░  ░░░░░░░░░░░░        ██    
                ██                  ░░██▒▒  ██░░                                        ██    
                ██    ▒▒░░▒▒▒▒      ██        ██                                          ██  
                    ██    ▒▒▒▒        ██        ██░░                                        ██  
                    ██            ██          ██░░                                        ██  
                        ██        ██            ██░░░░                                      ██  
                        ██████████              ██░░░░                                    ██  
                            ██░░░░██                ██░░░░░░                                ██  
                            ██░░██                  ████░░░░░░      ░░░░░░░░░░░░░░░░░░      ██  
                            ██                    ██░░██████░░  ░░░░██████████████░░░░    ██  
                                                    ██░░██▓▓  ██  ░░██        ██░░░░██░░░░  ██  
                                                    ██░░██▓▓  ██  ░░██        ██░░░░░░██░░░░  ██
                                                    ██░░██▓▓  ██  ░░██          ██░░░░████░░  ██
                                                    ██░░██▓▓  ██  ░░██            ██░░██  ██  ██
                                                    ██░░██▓▓  ██  ░░██            ██░░██  ██  ██
                                                    ██░░██▓▓  ██  ░░██            ██░░██  ██░░██
                                                    ██████▓▓  ████████            ██████  ██████
                                                    ██▒▒██▓▓  ██▒▒▒▒██            ██▒▒██  ██▒▒██
                                                                                                
                                    ░░      ░░    ░░                ░░░░                        
                """ 
                print(a)
                for elem in L:
                    print("\n\t{}\n{}".format(elem.cim,elem.szoveg))
                    eleje=input('[TOVÁBB]')
                    while eleje!='':
                        print('[ENTER] billentyűt kell megnyomnod! Különben nem fog tovább menni a szöveg.')
                        eleje=input('[NYomd meg az ENTERT]')
                teszt=input('Ki akarod tölteni a tesztet? [i/n] ')
                if teszt=='i':
                    pont=0
                    for elem in L:
                        valasz=input("{}\t".format(elem.kerdes))
                        valasz.lower()
                        if valasz==elem.valasz:
                            print("A válasz helyes.")
                            pont+=1
                        else:
                            print("A válasz hibás, a helyes válasz: {}\n".format(elem.valasz))
                    print("\nPontjaid: {}/4, {}".format(pont,mennyirejo(pont)))
        elif tipus==2:
            igen6=int(input("Melyik állatfaról szeretnél tanulni?\n\t1: Nílusi víziló\n\t2: Gnú\n\t3: Gömbhal\n\t"))
            while igen6<1 or igen6>3:
                igen6=int(input("Melyik állatfaról szeretnél tanulni?\n\t1: Nílusi víziló\n\t2: Gnú\n\t3: Gömbhal\n\t"))
            if igen6==1:
                class vizilo:
                    def __init__(self,cim,szoveg,kerdes,valasz):
                        self.cim=cim
                        self.szoveg=szoveg
                        self.kerdes=kerdes
                        self.valasz=valasz
                        
                L=[]
                f=open("fajlok/vizilo.txt","r",encoding="utf-8")
                for sor in f:
                    sor=sor.replace("\n","")
                    d=sor.split(";")
                    obj=vizilo(d[0],d[1],d[2],d[3])
                    L.append(obj)
                    f.close
                for elem in L:
                    print("\n\t{}\n{}".format(elem.cim,elem.szoveg)) 
                teszt=input('Ki akarod tölteni a tesztet? [i/n] ')
                if teszt=='i':
                    pont=0
                    for elem in L:
                        valasz=input("\n{}\t".format(elem.kerdes))
                        valasz.lower()
                        if valasz==elem.valasz:
                            print("A válasz helyes.")
                            pont+=1
                        else:
                            print("A válasz hibás, a helyes válasz: {}\n".format(elem.valasz))
                    print("\nPontjaid: {}/4, {}".format(pont,mennyirejo(pont)))
            if igen6==2:
                class gnu:
                    def __init__(self,cim,szoveg,kerdes,valasz):
                        self.cim=cim
                        self.szoveg=szoveg
                        self.kerdes=kerdes
                        self.valasz=valasz
                L=[]
                f=open("fajlok/gnu.txt","r",encoding="utf-8")
                for sor in f:
                    sor=sor.replace("\n","")
                    d=sor.split(";")
                    obj=gnu(d[0],d[1],d[2],d[3])
                    L.append(obj)
                    f.close
                for elem in L:
                    print("\n\t{}\n{}".format(elem.cim,elem.szoveg)) 
                teszt=input('Ki akarod tölteni a tesztet? [i/n] ')
                if teszt=='i':
                    pont=0
                    for elem in L:
                        valasz=input("\n{}\t".format(elem.kerdes))
                        valasz.lower()
                        if valasz==elem.valasz:
                            print("A válasz helyes.")
                            pont+=1
                        else:
                            print("A válasz hibás, a helyes válasz: {}\n".format(elem.valasz))
                    print("\nPontjaid: {}/4, {}".format(pont,mennyirejo(pont)))
            if igen6==3:
                class gombhal:
                    def __init__(self,cim,szoveg,kerdes,valasz):
                        self.cim=cim
                        self.szoveg=szoveg
                        self.kerdes=kerdes
                        self.valasz=valasz
                L=[]
                f=open("fajlok/gombhal.txt","r",encoding="utf-8")
                for sor in f:
                    sor=sor.replace("\n","")
                    d=sor.split(";")
                    obj=gombhal(d[0],d[1],d[2],d[3])
                    L.append(obj)
                    f.close
                for elem in L:
                    print("\n\t{}\n{}".format(elem.cim,elem.szoveg)) 
                teszt=input('Ki akarod tölteni a tesztet? [i/n] ')
                if teszt=='i':
                    pont=0
                    for elem in L:
                        valasz=input("\n{}\t".format(elem.kerdes))
                        valasz.lower()
                        if valasz==elem.valasz:
                            print("A válasz helyes.")
                            pont+=1
                        else:
                            print("A válasz hibás, a helyes válasz: {}\n".format(elem.valasz))
                    print("\nPontjaid: {}/4, {}".format(pont,mennyirejo(pont)))
    elif nem=='3':
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
    ujra=input("Visszamész a menübe? [i/n] ")
    while ujra!="i" and ujra!="n":
        ujra=input("Visszamész a menübe? [i/n] ")