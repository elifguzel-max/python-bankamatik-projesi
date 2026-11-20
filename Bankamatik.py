# --- 1. SINIF: MÜŞTERİ HESABI ---
class Hesap:
    def __init__(self, ad_soyad, sifre, bakiye=0):
        # Nesne oluşturulurken çalışan kurucu metot (Constructor)
        self.ad_soyad = ad_soyad
        self.sifre = sifre
        self.bakiye = bakiye

# --- 2. SINIF: ATM İŞLEMLERİ ---
class Bankamatik:
    def __init__(self, hesap):
        # Bankamatik başlatılırken içine bir 'Hesap' nesnesi alır
        self.hesap = hesap

    # Fonksiyon 1: Şifre Doğrulama
    def sifre_dogrula(self):
        hak = 3
        while hak > 0:
            girilen_sifre = input("Lütfen 4 haneli şifrenizi giriniz: ")
            if girilen_sifre == self.hesap.sifre:
                print(f"\nHoş geldiniz, {self.hesap.ad_soyad}!")
                return True
            else:
                hak -= 1
                print(f"Hatalı şifre! Kalan deneme hakkınız: {hak}")
        print("Kartınız bloke olmuştur. Müşteri hizmetlerini arayınız.")
        return False

    # Fonksiyon 2: Bakiye Sorgulama
    def bakiye_goster(self):
        print(f"Güncel Bakiyeniz: {self.hesap.bakiye} TL")

    # Fonksiyon 3: Para Yatırma
    def para_yatir(self, miktar):
        if miktar > 0:
            self.hesap.bakiye += miktar
            print(f"{miktar} TL yatırıldı.")
            self.bakiye_goster()
        else:
            print("Geçersiz tutar! 0'dan büyük bir değer giriniz.")

    # Fonksiyon 4: Para Çekme
    def para_cek(self, miktar):
        if miktar <= 0:
            print("Geçersiz tutar! Lütfen pozitif bir sayı giriniz.")
        elif miktar > self.hesap.bakiye:
            print("Yetersiz bakiye! İşlem gerçekleştirilemedi.")
        else:
            self.hesap.bakiye -= miktar
            print(f"{miktar} TL çekildi.")
            self.bakiye_goster()

# --- ANA PROGRAM AKIŞI ---
def sistemi_baslat():
    # 1. Örnek bir müşteri hesabı (nesnesi) oluşturuyoruz
    musteri1 = Hesap("Ahmet Yılmaz", "1234", 1500)
    # 2. Bu hesabı bankamatik sistemine tanımlıyoruz
    atm = Bankamatik(musteri1)

    # 3. Şifre doğruysa ana menü döngüsüne giriyoruz
    if atm.sifre_dogrula():
        while True:
            print("\n--- TALOS BANK MENÜ ---")
            print("1- Bakiye Sorgula | 2- Para Yatır | 3- Para Çek | 4- Çıkış")
            secim = input("Yapmak istediğiniz işlem (1-4): ")

            if secim == "1":
                atm.bakiye_goster()
            elif secim == "2":
                tutar = float(input("Yatırılacak tutar: "))
                atm.para_yatir(tutar)
            elif secim == "3":
                tutar = float(input("Çekilecek tutar: "))
                atm.para_cek(tutar)
            elif secim == "4":
                print("Kartınız iade ediliyor. İyi günler dileriz!")
                break  # Döngüyü sonlandırır ve programdan çıkar
            else:
                print("Hatalı seçim! Lütfen 1 ile 4 arasında bir tuşa basınız.")

# Programı çalıştır
sistemi_baslat()