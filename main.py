class Donto:
    def __init__(self, adatsor):
        reszletek = adatsor.split(';')
        #adatmezok kialakítása
        self.ssz = reszletek[0]
        self.Datum = reszletek[1]
        self.gyoztes = reszletek[2]
        self.Eredmeny = reszletek[3]
        self.Vesztes = reszletek[4]
        self.Helyszin = reszletek[5]
        self.VarosAllam = reszletek[6]
        self.nezoszam = int(reszletek[7])

    def __str__(self):
        return f"{self.Datum}, {self.Helyszin}: {self.gyoztes} - {self.Vesztes} ({self.Eredmeny})"
    
#0 
print("Super Bowl döntői.")


#1
finp = open("SuperBowl.txt", mode="rt", encoding="utf-8")
adatsorok = finp.read().split('\n')
finp.close()

dontok = []
for i in range(1, len(adatsorok)):
    if(adatsorok[i] != ""):
        donto = Donto(adatsorok[i])
        dontok.append(donto)

#3
for item in dontok:
    print(item)
