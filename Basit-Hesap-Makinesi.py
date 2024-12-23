#Basit Hesap Makinesi

Uygulamaisim = " İşlemler diyarı"

print(Uygulamaisim+"na Hoşgeldin ")


isaret = ("+","-","*","/","^","%")
islem=""
while True:
    try:
       
        while isaret.count(islem)==0:
            islem = input("Hesaplama yapmak istediğiniz işlem türünü giriniz.(+,-,*,/,^,%) ")
            #kullanıcı işlem türünü girene kadar while döngüsüne hapsoldu :D

        ilkSayi = float(input("Sayınızın ilk değerini giriniz: "))
        ikinciSayi = float(input("Sayınızın ikinci değeri giriniz: "))

        if islem =="+":
            sonuc = ilkSayi + ikinciSayi   
        elif islem =="-":
            sonuc = ilkSayi - ikinciSayi  
        elif islem =="/":
            sonuc = ilkSayi / ikinciSayi
        elif islem =="*":
            sonuc = ilkSayi * ikinciSayi
        elif islem =="^":
            sonuc = ilkSayi ** ikinciSayi
        elif islem =="%":
            sonuc = ilkSayi % ikinciSayi

        print(ilkSayi,islem,ikinciSayi,"=",sonuc)

        cikis = input("Çıkmak için 'E' devam etmek için ENTER tuşuna basınız.")
        islem=""
        if cikis.upper() == "E":
            break

    except:
        print("Sayıları kontrol edip tekrar deneyin.")
        islem=""