import python
import savastir
# 2 farklı savaşçı oluştur

savasci1 = python.savasci(25,15)
savasci2 = python.savasci(30,7, "Savaşçı")

while True:
    cikiyormu = input("Devam etmek istiyorsanız, herhangi bir şey giriniz. Çıkmak için quit yazın=> ")
    if(cikiyormu == "quit"):
        break
    savastir.savasicak(savasci1,savasci2)
    if(not (savasci2.getCan() > 0)): 
        break
    