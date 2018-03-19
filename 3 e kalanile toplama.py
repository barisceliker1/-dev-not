print("çıkmak için 0 yaz")
yeni=0
while True:
    girilensayi=int(input("bir sayı giriniz"))
    yeni=yeni+girilensayi%3
    print(yeni)
    if girilensayi==0:
        break
    
