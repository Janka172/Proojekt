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
        darab=0
        for elem in L:
            darab+=1
            if darab==1:
                print("\t\t{}".format(elem.cim))
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
            print("Pontjaid: {}/5".format(pont))
    elif te==2: print('Nem töltheted ki a tesztet ismeretek nélkül! >:(')
if igen2==2:
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
               print("\t{}\n{}".format(elem.cim,elem.szoveg)) 
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
                print("Pontjaid: {}/4".format(pont))
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
               print("\t{}\n{}".format(elem.cim,elem.szoveg)) 
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
                print("Pontjaid: {}/3".format(pont))
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
               print("\t{}\n{}".format(elem.cim,elem.szoveg)) 
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
                print("Pontjaid: {}/4".format(pont))
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
               print("\t{}\n{}".format(elem.cim,elem.szoveg)) 
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
                print("Pontjaid: {}/3".format(pont))
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
               print("\t{}\n{}".format(elem.cim,elem.szoveg)) 
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
                print("Pontjaid: {}/3".format(pont))
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
               print("\t{}\n{}".format(elem.cim,elem.szoveg)) 
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
                print("Pontjaid: {}/4".format(pont))