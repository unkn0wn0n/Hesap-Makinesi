import time

text_1 = "HESAP MAKİNESI\n"

print(text_1.center(75, " "))

while True:
    print("""
    İşlemler :\n
    1 ) Toplama
    2 ) Çıkarma
    3 ) Çarpma
    4 ) Bölme
    5 ) Üs Alma
    6 ) Kök Alma

    (Çıkmak için 'q' tuşuna basın)
    """)

    islem = input("Yapmak istediğiniz işlemin numarasını yazın: ")

    if (islem == "q"):
        break

    elif (islem == "1"):
        kac_sayi = int(input("\nKaç sayı toplamak istiyorsunuz? "))
        print("")

        sayi_top = 0
        i = 0

        while (i < kac_sayi):
            sayi = int(input("Sayıyı giriniz: "))
            sayi_top = sayi_top + sayi
            i = i + 1

        print("\nToplama işleminin sonucu: " , sayi_top)
        time.sleep(1.0)

    elif (islem == "2"):
        sayi_1 = int(input("\n1. sayı: "))
        sayi_2 = int(input("2. sayı: "))

        sayi_cik = sayi_1 - sayi_2

        print("\nÇıkarma işleminin sonucu: " , sayi_cik)
        time.sleep(1.0)

    elif (islem == "3"):
        kac_sayi = int(input("\nKaç sayı çarpmak istiyorsunuz? "))
        print("")

        sayi_carp = 1
        i = 0

        while (i < kac_sayi):
            sayi = int(input("Sayıyı giriniz: "))
            sayi_carp = sayi_carp * sayi
            i = i + 1

        print("\nÇarpma işleminin sonucu: " , sayi_carp)
        time.sleep(1.0)

    elif (islem == "4"):
        sayi_1 = int(input("\n1. sayı: "))
        sayi_2 = int(input("2. sayı: "))

        sayi_bol = sayi_1 / sayi_2

        print("\nBölme işleminin sonucu: " , sayi_bol)
        time.sleep(1.0)

    elif (islem == "5"):
        taban = int(input("\nTaban: "))
        kuvvet = int(input("Kuvvet: "))

        sayi_us = 1

        sayi_us = taban ** kuvvet

        print("\nÜs alma işleminin sonucu: " , sayi_us)
        time.sleep(1.0)

    elif (islem == "6"):
        sayi = int(input("\nSayıyı giriniz: "))

        sayi_kok = sayi ** 0.5

        print("\nHesaplanıyor...")
        time.sleep(2.0)

        print("\nKök alma işleminin sonucu: " , sayi_kok)
        
        #devam_tamam = input("Devam etmek için 'e', programı sonlandırmak için 'h'")
        # ---if (devam_tamam == )

    else:
        print("\nLütfen geçerli bir işlem numarsı giriniz!")
        time.sleep(0.5)
