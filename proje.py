import random

from fonksiyonlar import *

print("\n-------------Çoklu-İşlemli-Program-------------\n")
admintablo()
kullanici_adi = ""
parola = ""
giris_hakki = 3

while True:

    print("\nİşlemler : \n")
    print("1 = Giriş Ekranı \n")
    print("2 = Kayıt Ekranı \n")
    print("Programı Kapatmak İçin 'q' Tuşuna Basınız\n")

    iislem = input("Lütfen Yapmak İstediğiniz İşlemi Seçin : ")

    if iislem == "1":

        print("\n\n------------- Giriş Sayfası ---------------\n")

        # alinan_K_A = input("Kullanıcı Adınız Giriniz : ")
        # alinan_P = input("Parolayı Giriniz : ")

        while True:
            if giris_hakki == 0:
                break

            alinan_K_A = input("\nKullanıcı Adınız Giriniz :\n ")
            """
            alinan_P = pwinput.pwinput(prompt='Parolayı Giriniz :\n ', mask='*')
            print(alinan_P)
            """
            alinan_P = input("Parolayı Giriniz :\n ")

            don_deger = giris_kontrol(alinan_K_A, alinan_P)
            don_deger_admin = giris_kontrol_admin(alinan_K_A, alinan_P)

            print("\nGiriş Yapılıyor....")
            time.sleep(1)

            if don_deger == "true" or don_deger_admin == "true":
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1")
                time.sleep(1)
                print("\nGiriş Başarılı ...")
                kullanici_adi = alinan_K_A
                parola = alinan_P
                break

            elif don_deger == "false":

                print("\nGiriş Başarısız ...")

                donen_deger = kontrol(alinan_K_A)

                if donen_deger == "false":
                    yildiz()
                    print("Kullanıcıadı Hatalı Girilidi....\n ")
                    giris_hakki -= 1
                    print("Giriş Hakkınız Kaldı :", giris_hakki)
                    yildiz()

                elif donen_deger == "true":
                    yildiz()
                    print("\nParola Hatalı Girilidi ...\n")
                    giris_hakki -= 1
                    print("Giriş Hakkınız Kaldı :", giris_hakki)
                    yildiz()

                if giris_hakki == 0:
                    yildiz()
                    print("Giriş Hakkınız Bitti...\n")
                    yildiz()

        # ----------------------------------------------------------------------------------------------

        while True:
            if giris_hakki == 0:
                break

            print("\nİşlemler : ")
            print("1 = Hesap Makinası(Tam Sayı)")
            print("2 = ATM Makinası")
            print("3 = Faktöriyel Bulma")
            print("4 = Beden Kitle İndeksi")
            print("5 = En Büyük Sayıyı Bulma")
            print("6 = Not Ortalaması Bulma")
            print("7 = Geometrik Şekil Bulma")
            print("8 = Mükemmel Sayı Bulma(Tam Sayı)")
            print("9 = Çarpım Tablosu")
            print("10 = Armstrong Sayısı Bulma")
            print("11 = Sayı Tahmin Oyunu")
            print("12 = Playlist Oluşturucu")
            print("13 = EBOB veya EKOK Bulma")
            print("14 = Sayının Okunuşunu Veya Yazılışını Bulma")
            print("15 = AYARLAR\n")
            print("Bilgi : Çıkmak İçin 'q' Tuşuna Basınız\n")

            islem = input("Lütfen Yapılacak İşlemi Seçiniz : \n")

            if islem == "1":

                print("""                **************************************

                ------ Hesap Makinası(Tam Sayı) -------

                **************************************""")

                while True:
                    try:

                        print("\n 1 = Toplama İşlemi\n ")
                        print(" 2 = Çıkarma İşlemi\n ")
                        print(" 3 = Çarpma İşlemi\n ")
                        print(" 4 = Bölme İşlemi \n")
                        print("(Çıkmak İçin 'q' Tuşuna Basınız)\n")

                        islem = input("Lütfen Yapılaca İşlemi Seçiniz : ")

                        if islem == "q":
                            prgkapan()
                            break
                        elif islem != "1" or "2" or "3" or "4":
                            gecersiz()

                        a = int(input("\nLütfen İlk Sayıyı Giriniz : "))
                        b = int(input("\nLütfen İkinci Sayıyı Giriniz :"))

                        if islem == "1":
                            print("{} + {} = {}".format(a, b, a + b))

                        elif islem == "2":
                            print("{} - {} = {}".format(a, b, a - b))

                        elif islem == "3":
                            print("{} * {} = {}".format(a, b, a * b))

                        elif islem == "4":
                            print("{} / {} = {}".format(a, b, a / b))

                        else:
                            gecersiz()
                            break

                    except ValueError:

                        valueerror()

                    except ZeroDivisionError:
                        zeroerror()

            # ----------------------------------------------------------------------------------------------

            elif islem == "2":
                print("""                *******************************************

                -----------------ATM Makinası--------------

                *******************************************""")

                bakiye = 1000

                while True:
                    print(" \nİşlemler : ")
                    print("1. Bakiye Sorgulama")
                    print("2. Para Çekme")
                    print("3. Para Yatırma")
                    print("Programdan Çıkmak İçin 'Q' Tuşuşna Basın ")

                    islem = input("\nYapılacak İşlemi Seçinizi : ")

                    try:
                        if islem == "q":
                            prgkapan()
                            print("Yine Bekleriz....\n")
                            time.sleep(1)
                            break
                        elif islem == "1":
                            print("\nBakiyeniz : ", bakiye)

                        elif islem == "2":

                            while True:

                                try:
                                    cekilecek_tutar = int(input("\nÇekilecek Tutarı Giriniz : "))
                                    if bakiye - cekilecek_tutar < 0:
                                        print("\nBöyle Bir Miktar Çekemssiniz !....")
                                        continue
                                    bakiye -= cekilecek_tutar

                                    print("\nİşlem Gerçekleştiriliyor...")
                                    time.sleep(1)
                                    print("3")
                                    time.sleep(1)
                                    print("2")
                                    time.sleep(1)
                                    print("1"),
                                    time.sleep(1)
                                    print("İşlem Gerçekleştirildi\n")
                                    print("Paranızı Bankodan Almayı Unutmayınız")
                                    print("Yeni Bakiyeniz", bakiye)
                                    break

                                except ValueError:
                                    valueerror()
                        elif islem == "3":

                            while True:

                                try:
                                    yatirilacak_tutar = int(input("\nYatırılacak Tutarı Giriniz : "))
                                    bakiye = bakiye + yatirilacak_tutar
                                    print("İşlem Gerçekleştiriliyor...")
                                    time.sleep(1)
                                    print("3")
                                    time.sleep(1)
                                    print("2")
                                    time.sleep(1)
                                    print("1"),
                                    time.sleep(1)
                                    print("İşlem Gerçekleştirildi\n")
                                    print("Yeni Bakiyeniz :", bakiye)
                                    break

                                except ValueError:
                                    valueerror()

                        else:
                            gecersiz()

                    except ValueError:
                        valueerror()
            # ----------------------------------------------------------------------------------------------

            elif islem == "3":
                print("""                 *******************************************

                 --------------Faktöriyel Bulma--------------

                 Programdan Çıkmak İçin 'Q' Tuşuşna Basın 

                 *******************************************""")

                while True:

                    try:

                        sayi = input("\nFaktöriyelini Bulmak İstediğiniz Sayıyı Giriniz : ")

                        if sayi == "1":
                            print("\n1 in Faktöriyeli 1 dir")

                        elif sayi == "0":
                            print("\n0 in Faktöriyeli 1 dir")

                        elif sayi == "q":
                            prgkapan()
                            break
                        else:
                            sayi = int(sayi)
                            faktoriyel = 1

                            for i in range(2, sayi + 1):
                                faktoriyel *= i
                                print("Girilen Sayı : ", sayi, "!", "Faktöriyeli : ", faktoriyel)

                    except ValueError:
                        valueerror()

            # ----------------------------------------------------------------------------------------------

            elif islem == "4":

                print("""                ********************************


                -------Beden Kitle İndeksi------


                ********************************\n""")

                while True:
                    try:
                        print("\nİşlemler : ")
                        print("1 = Beden Kitle İndeksi")
                        print("2 = Eski İndeksleri Görüntüle")
                        print("Çıkmak İçin 'q' Tuşuna Basınız")

                        islemm = input("\nLütfen Yapılacak İşlemi Seçiniz : ")

                        if islemm == "1":

                            while True:
                                try:
                                    boy = float(input("\nLütfen Boyunuzu Giriniz (Lütfen nokta koyarak giriniz) : "))
                                    kilo = int(input("Lütfen Kilonuzu Giriniz : "))

                                    kitle_indeksi = kilo / boy ** 2

                                    print("Kitle İndeksiniz : ", kitle_indeksi)

                                    if kitle_indeksi < 18.5:
                                        print(" \nZayıf :|")

                                    elif 18.5 <= kitle_indeksi < 25:
                                        print(" \nNormal :))")

                                    elif 25 <= kitle_indeksi < 30:
                                        print(" \nFazla Kilolu :(")

                                    else:
                                        print(" \nOBEZ :((")

                                    print("\nDevam Etmek İçin Herhangi Bir Tuşa Basın")
                                    cikis = input("\nÇıkmak İçin 'q' Tuşuna Basınız : ")

                                    if cikis == "q":
                                        prgkapan()
                                        break

                                except ValueError:
                                    valueerror()

                                except ZeroDivisionError:
                                    zeroerror()

                        elif islemm == "2":
                            print("\nEski işlem Bulunamadı....")

                        elif islemm == "q":
                            prgkapan()
                            break

                        else:
                            gecersiz()

                    except ValueError:
                        valueerror()

            # ----------------------------------------------------------------------------------------------

            elif islem == "5":
                print("""                **************************************

                ------- En Büyük Sayıyı Bulma ----------

                **************************************\n""")

                while True:

                    try:
                        sayi1 = int(input("\nLütfen İlk Sayıyı Giriniz : "))

                        sayi2 = int(input("Lütfen İkinci Sayıyı Giriniz : "))

                        sayi3 = int(input("Lütfen Üçüncü Sayıyı Giriniz : "))

                        if sayi1 == sayi2 == sayi3:
                            print("\nBütün Sayılar Eşittir")

                        elif sayi2 >= sayi1 and sayi2 >= sayi3:
                            print("\nEn Büyük Sayı : ", sayi2)

                        elif sayi3 >= sayi2 and sayi3 >= sayi1:
                            print("\nEn Büyük Sayı : ", sayi3)

                        elif sayi1 >= sayi2 and sayi1 >= sayi3:
                            print("\nEn Büyük Sayı : ", sayi1)

                        print("\nDevam Etmek İçin Herhangi Bir Tuşa Basın")
                        cikis = input("\nÇıkmak İçin 'q' Tuşuna Basınız : ")

                        if cikis == "q":
                            prgkapan()
                            break

                    except ValueError:
                        valueerror()

            # ----------------------------------------------------------------------------------------------

            elif islem == "6":
                print("""                    **************************************

                    -------- Not Ortalaması Bulma ---------

                    **************************************\n\n""")
                print("""Notların Etki Yüzdelikleri :

                1. Vize = %30
                2. Vize = %30
                Final = %40

                Harf Notlandırmalarının Anlamları :

                AA = Mükemmel
                BA = Çok İyi
                BB = İyi
                CB = Orta
                CC = Yeterli
                DC = Koşullu Başarılı
                DD = Koşullu Başarılı
                FD = Devamsız Başarısız
                FF = Başarısız

                 """)

                while True:

                    print("\nİşlemler : ")
                    print("1 = Rasgele Ortalama Bulma")
                    print("2 = Ders Ve Ortalama Kaydetme")
                    print("3 = Kayıtlı Ortalamalara Bakma")
                    print("Çıkmak İçin 'q' Tuşuna Basınız")

                    isslem = input("\nLütfen Yapmak İstediğiniz İşlemi Seçiniz : ")

                    if isslem == "1":

                        while True:
                            try:

                                vize1 = float(input("\nLütfen İlk Vize Notunuzu Giriniz : "))

                                vize2 = float(input("Lütfen İkinci Vize Notunuzu Giriniz : "))

                                final = float(input("Lütfen Final Notunuzu Giriniz : "))

                                ortalama = vize1 * 3 / 10 + vize2 * 3 / 10 + final * 4 / 10

                                if ortalama >= 90:
                                    print("\nOrtalamanız : ", ortalama)
                                    print("\nYıl Sonu Ders Notunuz : AA")
                                    print("\nAA = Mükemmel")

                                elif ortalama >= 85:
                                    print("\nOrtalamanız : ", ortalama)
                                    print("Yıl Sonu Ders Notunuz : BA")
                                    print("BA = Çok İyi")

                                elif ortalama >= 80:
                                    print("\nOrtalamanız : ", ortalama)
                                    print("Yıl Sonu Ders Notunuz : BB")
                                    print("BB = İyi")

                                elif ortalama >= 75:
                                    print("\nOrtalamanız : ", ortalama)
                                    print("Yıl Sonu Ders Notunuz : CB")
                                    print("CB = Orta")

                                elif ortalama >= 70:
                                    print("\nOrtalamanız : ", ortalama)
                                    print("Yıl Sonu Ders Notunuz : CC")
                                    print("CC = Yeterli")

                                elif ortalama >= 65:
                                    print("\nOrtalamanız : ", ortalama)
                                    print("Yıl Sonu Ders Notunuz : DC")
                                    print("DC = Koşullu Başarılı")

                                elif ortalama >= 60:
                                    print("\nOrtalamanız : ", ortalama)
                                    print("Yıl Sonu Ders Notunuz : DD")
                                    print("DC = Koşullu Başarılı")

                                elif ortalama >= 55:
                                    print("\nOrtalamanız : ", ortalama)
                                    print("Yıl Sonu Ders Notunuz : FD")
                                    print("FD = Devamsız Başarısız")

                                else:
                                    print("\nOrtalamanız : ", ortalama)
                                    print("Yıl Sonu Ders Notunuz : FF")
                                    print("FF = Başarısız")

                                break

                            except ValueError:
                                valueerror()
                    elif isslem == "2":
                        print("\nŞu Anda Bu işlemi gerçekleştirmiyoruz... :((")

                    elif isslem == "3":
                        print("\nEski Kayıt Bulunamadı...")

                    elif isslem == "q":
                        prgkapan()
                        break

                    else:
                        gecersiz()

            # ----------------------------------------------------------------------------------------------

            elif islem == "7":
                print("*************************************************\n")

                print("---------- Geometrik Şekil Bulma -------------\n")

                print("*************************************************\n")

                while True:

                    try:
                        print("-------------------------------")
                        print("Bulunacak Şekliler : ")
                        print("1 = Dörtgen")
                        print("2 = Üçgen")
                        print("Çıkmak İçin 'q' ya Basınız.")
                        print("-----------------------------")
                        islem = input("\nBulunacak Şekli Seçiniz : ")

                        if islem == "1":
                            while True:
                                try:
                                    print("\n---------DÖRTGEN-----------\n")

                                    print("\nLütfen Kenar Uzunluklarını Girin :\n")
                                    kenar1 = float(input("Kenar 1 : "))
                                    kenar2 = float(input("Kenar 2 : "))
                                    kenar3 = float(input("Kenar 3 : "))
                                    kenar4 = float(input("Kenar 4 : "))

                                    if kenar1 == kenar2 == kenar3 == kenar4:
                                        print("Dörtgeniniz Bir KAREDİR\n",
                                              "Bütün Kenarları Eşit Olduğu İçin Bir KAREDİR\n",
                                              "Çevresi : ",
                                              kenar1 + kenar2 + kenar3 + kenar4)

                                    elif (kenar1 == kenar2 and kenar3 == kenar4) or (
                                            kenar2 == kenar3 and kenar1 == kenar4) or (
                                            kenar2 == kenar4 and kenar3 == kenar1):
                                        print("Dörtgeniniz Bir DİKDÖRTGENDİR\n",
                                              "İkişer Kenarları Birbirlerine Eşit Olduğu İçin Bir DİKDÖRTGENDİR\n",
                                              "Çevresi : ",
                                              kenar1 + kenar2 + kenar3 + kenar4)

                                    else:
                                        print("Dörtgeniniz Normal Bir DÖRTGENDİR\n",
                                              "En az Bir Kenarı Veya Hepsi Birbirinden Farklı Olduğu İçin BU Normal Bir"
                                              "DÖRTGENDİR\n",
                                              "Çevresi : ",
                                              kenar1 + kenar2 + kenar3 + kenar4)
                                except ValueError:
                                    valueerror()

                                break

                        elif islem == "2":
                            print("\n---------ÜÇGEN-----------\n")

                            while True:
                                try:
                                    print("\nLütfen Kenar Uzunluklarını Girin :")
                                    u_kenar1 = float(input("Kenar 1 : "))
                                    u_kenar2 = float(input("Kenar 2 : "))
                                    u_kenar3 = float(input("Kenar 3 : "))

                                    if (u_kenar1 + u_kenar2 > u_kenar3) and (u_kenar1 + u_kenar3 > u_kenar2) and (
                                            u_kenar2 + u_kenar3 > u_kenar1):

                                        if u_kenar1 == u_kenar2 == u_kenar3:
                                            print("\nÜçgeniniz Bir EŞKENAR ÜÇGENDİR\n\n",
                                                  "Bütün Kenarları Eşit Olduğu İçin Bir EŞKENAR ÜÇGENDİR\n\n",
                                                  "Çevresi : ",
                                                  u_kenar1 + u_kenar2 + u_kenar3)

                                        elif (u_kenar1 == u_kenar2) or (u_kenar1 == u_kenar3) or (u_kenar2 == u_kenar3):
                                            print("\nÜçgeniniz Bir İKİZKENAR ÜÇGENDİR\n\n",
                                                  "Herhangi İKİ Kenarları Eşit Olduğu İçin Bir İKİZKENAR ÜÇGENDİR\n\n",
                                                  "Çevresi : ",
                                                  u_kenar1 + u_kenar2 + u_kenar3)

                                        else:
                                            print("Üçgeniniz Bir ÇEŞİTKENAR ÜÇGENDİR\n", "Çevresi : ",
                                                  u_kenar1 + u_kenar2 + u_kenar3)

                                        break

                                    else:
                                        print("Bu Bir Üçgen Olamaz-Üçgen Belirtmiyor...")

                                except ValueError:
                                    valueerror()

                        elif islem == "q":

                            prgkapan()
                            break

                        else:

                            gecersiz()

                    except ValueError:
                        valueerror()

            # ----------------------------------------------------------------------------------------------

            elif islem == "8":
                print(
                    "*******************------------ Mükemmel Sayı Bulma(Tam Sayı) -------------********************\n")

                while True:
                    try:
                        sayi = input(
                            "\nMükemmel Olup Olmadığını Bulmak İstediğiniz Sayıyı Giriniz\n "
                            "\nSeçim Menüsüne Dönmek İçin 'q' Tuşuna Basın : \n")

                        if sayi == "q":
                            prgkapan()
                            break

                        sayi = int(sayi)

                        a = 0
                        t = 0

                        for a in range(1, sayi):
                            if sayi % a == 0:
                                t += a

                        if sayi == t:
                            print(sayi, "Bu Sayı Mükemmeldir..")

                        else:
                            print(sayi, "Bu Sayı Mükemmel Değildir")

                    except ValueError:
                        valueerror()

            # ----------------------------------------------------------------------------------------------

            elif islem == "9":
                print("-------------------Çarpım Tablosu-------------------")
                x = input("Çarpım Tablossunu Görmek İçin 1 \nSeçim Menüsüne Dönmek İçin 'q' Tuşuna Basın : \n")
                while True:
                    try:
                        if x == "1":
                            sayii = range(1, 11)

                            for a in sayii:
                                print("--------------------------------------")
                                for b in sayii:
                                    print(a, "*", b, "=", b * a)

                            break

                        if x == "q":
                            prgkapan()
                            break

                        else:
                            gecersiz()

                    except ValueError:
                        valueerror()
            # ----------------------------------------------------------------------------------------------

            elif islem == "10":

                print("""                **************************************

                ------- Armstrong Sayısı Bulma --------

                Çıkmak İçin 'q' Tuşuna Basınız 

                **************************************\n""")
                while True:
                    try:

                        sayi = input("\nLütfen Kontrol Edilecek Sayıyı Giriniz veya Çıkış İçin 'q' ya basın : \n")

                        if sayi == "q":
                            prgkapan()
                            break

                        basamak_sayisi = len(sayi)

                        sayi = int(sayi)

                        basamak = 0
                        toplam = 0

                        gecici_sayi = sayi

                        while gecici_sayi > 0:
                            basamak = gecici_sayi % 10

                            toplam += basamak ** basamak_sayisi

                            gecici_sayi //= 10

                        if toplam == sayi:
                            print(sayi, "bir armstrong sayısıdır.")
                        else:
                            print(sayi, "bir armstrong sayısı değildir.")

                    except ValueError:
                        valueerror()

            # ----------------------------------------------------------------------------------------------

            elif islem == "11":

                print("""                **************************************
                --------- Sayı Tahmin Oyunu  ----------

                1 ile 50 Arasındaki Sayıyı Tahmin Edin
                (5 Adet Tahmin Hakkınız Vardır)
                Çıkmak İçin 'q' Tuşuna Basınız 

                **************************************\n""")

                rasgele_sayi = random.randint(1, 50)
                tahmin_hakki = 5

                while True:
                    try:
                        girilen_sayi = input("\nLutfen Tahmininizi Giriniz : ")

                        if girilen_sayi == "q":
                            prgkapan()
                            break

                        girilen_sayi = int(girilen_sayi)

                        if girilen_sayi < rasgele_sayi:
                            print("Bilgiler Doğrulanıyor...\n")
                            time.sleep(2)

                            print("Ne Yazıkki Bilemedin Tekrar Dene\n")
                            print("Biraz Daha Yüksek :)\n")
                            tahmin_hakki -= 1

                            print("Kalan Tahmin Hakkı : ", tahmin_hakki)

                        elif girilen_sayi > rasgele_sayi:

                            print("Bilgiler Doğrulanıyor...\n")
                            time.sleep(2)
                            print("Ne Yazıkki Bilemedin Tekrar Dene\n")
                            print("Biraz Daha Alçak :)\n")
                            tahmin_hakki -= 1

                            print("Kalan Tahmin Hakkı : ", tahmin_hakki)

                        else:
                            print("Bilgiler Doğrulanıyor...\n")
                            time.sleep(2)

                            print("!!!!! BRAVO BİLDİN !!!!!\n")
                            print("Rasgele Sayı : ", rasgele_sayi, "Tahminin : ", girilen_sayi)
                            print(tahmin_hakki, " Tahmin Kala Buldun ")
                            break

                        if tahmin_hakki == 0:
                            print("Tahmin Hakkın Bitti\n")
                            print("Rasgele Sayı : ", rasgele_sayi)
                            print("!!!!! Oyun Bitti !!!!!\n")
                            break

                    except ValueError:
                        valueerror()
            # ----------------------------------------------------------------------------------------------

            elif islem == "12":
                print("************************************ PLAYLİST OLUŞTURUCU************************************")
                print("\nHoş Geldiniz\n")
                tablo()

                while True:
                    print("\n1 = PlayListi Görüntüle")
                    print("2 = Şarkı Ekle")
                    print("3 = Şarkı Sil")
                    print("4 = Toplam PlayListin Süresi")
                    print("Çıkış Yapmak İçin 'q' Tuşuna Basın")

                    try:
                        islem = input("\nLütfen Yapmak İstediğiniz İşlemi Seçiniz : ")

                        if islem == "1":
                            print("\n******************* PlayList ********************\n")
                            playlist()
                            yildiz()

                        elif islem == "2":
                            print("\n*******************Şarkı Ekleme ********************\n")

                            sarki = input("Lütfen Eklenecek Şarkının İsmini Giriniz : ")
                            sanatci = input("\nLütfen Eklenecek Şanatçısının İsmini Giriniz : ")
                            sure = float(input("\nLütfen Eklenecek Uzunluğunu Giriniz(00.00 dakika.saniye) : "))

                            sarki_ekle(sarki, sanatci, sure)
                            yildiz()

                        elif islem == "3":
                            print("\n*******************Şarkı Silme ********************\n")

                            sil = input("Lütfen Silinecek Şarkıyının İsmini Giriniz : ")
                            sarki_sil(sil)
                            yildiz()

                        elif islem == "4":
                            print("\nPlaylistin Toplam Süresi : \n")
                            sureee()
                            yildiz()

                        elif islem == "q":
                            prgkapan()
                            break

                        else:
                            gecersiz()

                    except ValueError:
                        valueerror()

                con.close()

            elif islem == "13":
                print("\n------------- EBOB veya EKOK Bulma ---------------\n")

                while True:
                    try:
                        print("İşlemler : ")
                        print("\n1 = EBOB Bulma")
                        print("2 = EKOK Bulma")
                        print("Çıkış Yapmak İçin 'q' Tuşuna Basın")
                        i = input("\nLütfen Yapılacak İşlemi Seçiniz : ")
                        if i == "1":
                            print("\n------------- EBOB Bulma ---------------\n")

                        elif i == "2":
                            print("\n------------- EKOK Bulma ---------------\n")

                        elif i == "q":
                            prgkapan()
                            break

                        else:
                            gecersiz()

                    except ValueError:
                        valueerror()
                    except ZeroDivisionError:
                        zeroerror()

            elif islem == "14":
                print("\n------------- Sayının Okunuşunu Veya Yazılışını Bulma ---------------\n")
                print("Çıkmak İçin 'q' Tuşuna Basınız ")

                while True:
                    try:
                        sayy = input("Lütfen Okunuşunu Bulmak İstediğiniz Sayıyı Giriniz : ")

                    except ValueError:
                        valueerror()

            elif islem == "15":
                print("\n------------- AYARLAR ---------------\n")

                while True:
                    try:
                        print("İşlemler : ")
                        print("\n1 = Parola Değiştir")
                        print("2 = Kullanıcı Sil")
                        print("Çıkış Yapmak İçin 'q' Tuşuna Basın")
                        i = input("\nLütfen Yapılacak İşlemi Seçiniz : ")
                        if i == "1":
                            while True:
                                yeni_sifre = input("\nYeni Şifreyi Giriniz : ")
                                yeni_sifre2 = input("\nYeni Şifreyi Tekrar Giriniz : ")

                                if yeni_sifre == yeni_sifre2:
                                    sifre_degis(yeni_sifre, kullanici_adi)
                                    yildiz()
                                    print("\nŞifreniz Başarı İle Değiştirilmiştir...\n")
                                    yildiz()
                                    break

                                else:
                                    yildiz()
                                    print("\nŞifre Tekrarını Yanlış Girdiniz...")
                                    yildiz()

                        elif i == "2":
                            admin = "admin"
                            while True:

                                g_a_kod = input("\nLütfen Kullanıcı Silmek İçin Admin kodunu Giriniz : ")

                                if admin == g_a_kod:
                                    kullanici_oku()
                                    while True:
                                        sil = input("\nLütfen Silinecek kullanıcı Adını Giriniz : ")

                                        donen_deger = kontrol(sil)

                                        if donen_deger == "false":
                                            print("\nBöyle Bir Kullanıcı Bulunamadı...")

                                        elif sil == "q":
                                            prgkapan()
                                            break

                                        else:
                                            while True:
                                                print("\n- Evet")
                                                print("- Hayır")
                                                karar = input("\nSilmek İstediğine Eminmisin : ")

                                                if karar == "Evet" or karar == "evet":
                                                    kullanici_sil(sil)
                                                    break

                                                elif karar == "Hayır" or karar == "hayır":
                                                    time.sleep(1)
                                                    print("\nVazgeçildii")
                                                    break

                                                elif karar == "q":
                                                    prgkapan()
                                                    break

                                                else:
                                                    gecersiz()

                                elif g_a_kod == "q":
                                    prgkapan()
                                    break

                                else:
                                    gecersiz()
                        elif i == "q":
                            prgkapan()
                            break

                        else:
                            gecersiz()

                    except ValueError:
                        valueerror()

            elif islem == "q":
                prgkapan()
                break

            else:
                gecersiz()

    elif iislem == "2":

        print("\n------------- Kayıt-Ol-Sayfası ---------------\n")

        kullanici_tablo()

        kayit_kod = "12345"

        print("Çıkmak İçin 'q' Tuşuna Basın ")

        while True:
            try:
                g_kayit_kod = input("\nLütfen Kayıt Olmak İçin Kayıt Kodunu Giriniz : ")

                if g_kayit_kod == "q":
                    prgkapan()
                    break

                print("\nKod Doğrulanıyor...\n")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("\n1")

                if g_kayit_kod == kayit_kod:
                    print("\nKod Doğrulandı\n")

                    k_adi = input("Kullanıcı Adı : ")
                    sifre = input("Şifre : ")

                    do_deger = kontrol(k_adi)

                    if do_deger == "true":
                        print("\n!! Böyle Bir Kullanıcı Adı Bulunmaktadır !!")

                    else:
                        kayit_ol(k_adi, sifre)
                else:
                    print("\n!!!!!!!!! GEÇERSİZ KOD !!!!!!!!!")

            except ValueError:
                valueerror()

    elif iislem == "q":
        con.close()
        prgkapan()
        break

    else:
        gecersiz()
