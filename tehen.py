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