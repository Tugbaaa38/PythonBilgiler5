# if/else if/elif 

#Kullanicidan sinav notlarini alip ortalamasini bulalim ve gecip gecmedigini ekrana yazdiralim.
print("--------------Gecme/Kalma Durumu Hesaplama----------------\n")
isim=input("Lutfen adinizi giriniz:")
print("Vizenin %40'ı Finalin ise %60'ı ortalamada etkili olsun..")
vize=float(input("Vize notunuzu giriniz:")) #input string dondurdugunu soylemistik.float veri tipine cevirdik.
final=float(input("Final notunuzu giriniz:"))
print("\n")

ort=(float(vize)*0.4)+(float(final)*0.6)

#Burada finalden belli bir not alma durumu soz konusu.Final notu 50 den dusuk olursa her durumda kalsin.
if final>=50:
    if ort>=85 and ort<=100:
        print(f"Ortalamaniz:{ort}--Harf Notunuz AA GEÇTİNİZ  " +isim,"TEBRİKLER!")
    elif ort>=75 and ort<85 :
        print(f"Ortalamaniz:{ort}--Harf Notunuz BA GEÇTİNİZ  " +isim,"TEBRİKLER!")
    elif ort>= 70 and ort < 75:
        print(f"Ortalamaniz:{ort}--Harf Notunuz BB GEÇTİNİZ " +isim,"TEBRİKLER!")
    elif ort >= 65 and ort < 70:
        print(f"Ortalamaniz:{ort}--Harf Notunuz CB GEÇTİNİZ  " +isim,"TEBRİKLER!")
    elif ort >= 60 and ort < 65:
        print(f"Ortalamaniz:{ort}--Harf Notunuz CC GEÇTİNİZ  " +isim,"TEBRİKLER!")
    elif ort >= 55 and ort < 60:
        print(f"Ortalamaniz:{ort}--Harf Notunuz DC KOŞULLU GEÇTİNİZ  " +isim)
    elif ort >= 50 and ort < 55:
        print(f"Ortalamaniz:{ort}--Harf Notunuz DD KOŞULLU GEÇTİNİZ " +isim)	
   
else:
    print(f"Ortalamaniz:{ort}--Harf notunuz FF KALDINIZ " +isim,"COK CALİS!" )
    #if'lerin sonunda : koymayi unutmayalim!
    #and oprt. de iki durumun da saglanmasi gerekir.
    # or operatorunde ise iki durumdan biri saglanmasi yeterlidir.




