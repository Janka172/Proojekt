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