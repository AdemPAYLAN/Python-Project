import random

def sayi_tahmin_oyunu():
    print("Sayı Tahmin Oyununa Hoşgeldiniz!")
    
    # burada rastgele sayının hangi aralıkta olacağını seçiyoruz ve bu sayıyı belirliyoruz.
    rastgele_sayi = random.randint(1, 100)
    
    #Kullanıcının kaçıncı denemede bulduğunu ekrana yazdırmak için tahmin_hakki degişkenini oluşturuyoruz.
    tahmin_hakki = 0
    dogru_tahmin = False
    
    # KUllanıcı sayıyı bulana kadar onu bir while döngüsüne hapsediyoruz.
    while not dogru_tahmin:
        try:
            # Kullanıcıdan bir tahminde bulunmasını istiyoruz ve tahminin pozitif tam sayı olup olmadığının kontrolünü sağlıyoruz.
            oyuncu_tahmini = int(input("1 ile 100 arasında bir sayı tahmin edin: "))
            tahmin_hakki += 1
            
            # Geçerli bir sayı olup olmadığını kontrol ediyoruz.
            if oyuncu_tahmini < 1 or oyuncu_tahmini > 100:
                print("Lütfen 1 ile 100 arasında bir sayı girin.")
                continue
            
            # Kullanıcıya ipucu veriyoruz ve bu sayının doğru olup olmadığını kontrol ediyoruz.
            if oyuncu_tahmini < rastgele_sayi:
                print("Tahmininiz çok küçük. Daha büyük bir sayı deneyin.")
            elif oyuncu_tahmini > rastgele_sayi:
                print("Tahmininiz çok büyük. Daha küçük bir sayı deneyin.")
            else:
                dogru_tahmin = True
                print(f"Tebrikler! {tahmin_hakki} denemede doğru tahmin ettiniz.")
        # Burada olası bir hataya karşılık ekrana bir hata mesağı yazdırıyoruz.
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
            
# Oyunu başlatıyoruz.
sayi_tahmin_oyunu()
