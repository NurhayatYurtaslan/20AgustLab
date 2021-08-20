def savasicak(saldiran, savunan): 
    saldiranAtak = saldiran.getAtak()
    savunanDefans = savunan.getDefans()
    savunanCan = savunan.getCan()
 
    savunan.setCan(savunanCan - (saldiranAtak - savunanDefans)) 
    kontrol(savunan)
    

def kontrol(savunan): 
    print("Savunan savaşçının (", savunan.isim ,") canı = " , savunan.getCan())
    if(savunan.getCan() < 1 ):
        print(savunan.isim, "Öldü ")
    if(savunan.getCan() > 100):
        print("Can 100' den büyün olamaz")
