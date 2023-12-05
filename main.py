import Csoport

#eljárások
adatokListaja=[]
def beolvasas():
    beFajl = open("csoport.txt", "r", encoding="utf-8")
    #első sor
    beFajl.readline()
    #többi sor
    sorok=beFajl.readlines()
    #print(sorok)
    for sor in sorok:
        #adat tisztítás
        tisztitottsor = sor.strip()
        #print(tisztitottsor)

        #eldarabolom
        daraboltsor =tisztitottsor.split("/")
        #print(daraboltsor)

        #példányosítok
        csoporttag = Csoport.Csoport(daraboltsor[0],daraboltsor[1], daraboltsor[2])
        #print(csoporttag)
        #belefűzöm az objektumot a listába
        adatokListaja.append(csoporttag)
        beFajl.close()

def kiir():
    for index in range(0, len(adatokListaja),1):
        print(adatokListaja[index])

def sorokSzama():
    sorszam = len(adatokListaja)
    print(f"A tanulók száma: {sorszam}.")

def megszamlalas():
    osszeg = 0
    for index in range(0,len(adatokListaja),1):
        osszeg += adatokListaja[index].atlag
    if len(adatokListaja)==0:
        atlag = 0
    else:
        atlag = osszeg/len(adatokListaja)
    print(f"A suli átlag: {atlag}.")

def elsosokSzama():
    db = 0
    for index in range(0, len(adatokListaja),1):
        if adatokListaja[index].evfolyam == 1:
            db += 1
    print(f"AZ elsősök száma: {db}.")



#főprogram
beolvasas()
kiir()
sorokSzama()
megszamlalas()
elsosokSzama()