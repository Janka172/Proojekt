class angszint:
    def __init__(self,ker,val1,val2,val3,val4,mego):
        self.ker==ker
        self.val1==val1
        self.val2==val2
        self.val3==val3
        self.val4==val4
        self.mego==mego




me=0
szint=input('Szeretnéd felmérni a nyelvi színtedet angolból? [i/n]')
if szint=='i':
    while me>=51 or me<=16:
        me=int(input('Hány kérdéses tesztet szeretnél? [legkisebb 15, legnagyobb 50]'))
    
