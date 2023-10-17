import time
import sqlite3

con = sqlite3.connect("PlayList.db")

cursor = con.cursor()

con1 = sqlite3.connect("Admin.db")

cursor1 = con1.cursor()

con2 = sqlite3.connect("Kullanici.db")

cursor2 = con2.cursor()


def admin_ekle():
    cursor1.execute("INSERT INTO Admin VALUES ('admin','admin')")
    con1.commit()


def admintablo():
    cursor1.execute("CREATE TABLE IF NOT EXISTS Admin ( Kullanıcı Adı REAL UNIQUE, Şifre TEXT )")
    con1.commit()


def kullanici_tablo():
    cursor2.execute("CREATE TABLE IF NOT EXISTS Kullanici ( Kullanıcı REAL UNIQUE, Şifre TEXT )")
    con2.commit()


def kayit_ol(k_adi, sifre):
    cursor2.execute("INSERT INTO Kullanici VALUES (?,?)", (k_adi, sifre))
    print("\nKayıt Başarıyla Tamamlandı :)) ")
    con2.commit()


def kullanici_oku():
    cursor2.execute("SELECT Kullanıcı Adı FROM Kullanici")
    veri = cursor2.fetchall()

    for i in veri:
        print(i)


def kullanici_sil(sil):
    cursor2.execute("DELETE FROM Kullanici where Kullanıcı = ?", (sil,))
    con2.commit()
    print("Kullanıcı Siliniyor...")
    time.sleep(1)
    print("\n... Kullanıcı Silindi...")


def sifre_degis(yeni_sifre, ad):
    cursor2.execute("UPDATE Kullanici SET Şifre = ? where Kullanıcı = ?", (yeni_sifre, ad))
    con2.commit()


def tablo():
    cursor.execute("CREATE TABLE IF NOT EXISTS PlayList ( Şarkı_İsmi TEXT, Sanatçı TEXT ,Şarkı_Süresi FLOAT )")
    con.commit()


def sarki_ekle(sarki, sanatci, surre):
    cursor.execute("INSERT INTO PlayList VALUES (?,?,?)", (sarki, sanatci, surre))
    print("\nŞarkı Eklendi...")
    con.commit()


def sarki_sil(sil):
    cursor.execute("DELETE FROM PlayList where Şarkı_İsmi = ?", (sil,))
    con.commit()
    print("\nŞarkı Silindi...")


def playlist():
    cursor.execute("SELECT * FROM PlayList")
    sarkilar = cursor.fetchall()

    for i in sarkilar:
        print(i)
    con.commit()


def sureee():
    cursor.execute("SELECT Şarkı_Süresi FROM PlayList")
    suree = cursor.fetchall()

    toplam = 0.0

    for i in suree:
        a = str(i)
        b = a[1:-2]
        c = float(b)
        toplam += c

    print(toplam)


def valueerror():
    print("\n!!!! Hata !!!!\n")
    print("\n Böyle Bir Değer Girilemez\n")


def zeroerror():
    print("\n!!!! Hata !!!!\n")
    print(" 0 Değeri Girilemez\n")
    print("Lütfen Tekrar Deneyiniz")


def prgkapan():
    print("\nProgram Kapanıyor....")
    time.sleep(1)


def gecersiz():
    print("\n*************** Geçersiz İşlem..... ***************")


def kontrol(isim):
    cursor2.execute("SELECT Kullanıcı Adı FROM Kullanici WHERE Kullanıcı='" + isim + "'")
    veri = cursor2.fetchall()
    mevcutmu = 0

    for x in veri:
        mevcutmu = 1

    if mevcutmu == 1:

        return "true"
    else:
        return "false"


def giris_kontrol(isim, sifre):
    cursor2.execute("SELECT * FROM Kullanici where Kullanıcı = ? AND Şifre = ?", (isim, sifre))
    veri = cursor2.fetchall()
    mevcutmu = 0

    for x in veri:
        mevcutmu = 1

    if mevcutmu == 1:

        return "true"
    else:
        return "false"


def giris_kontrol_admin(a, p):
    cursor1.execute("SELECT * FROM Admin where Kullanıcı = ? AND Şifre = ?", (a, p))
    veri = cursor1.fetchall()
    mevcutmu = 0

    for x in veri:
        mevcutmu = 1

    if mevcutmu == 1:

        return "true"
    else:
        return "false"


def ebob_bulma():
    pass


def ekok_bulma():
    pass


def sayi_okunusu():
    pass


def yildiz():
    print("\n*********************************\n")
