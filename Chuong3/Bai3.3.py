KW=int(input("So dien tieu thu cua gia dinh: "))
if KW >= 1 and KW <= 100:
    price = KW*500
elif KW >= 101 and KW <= 150:
    price = 100*550 + (KW-100)*750
elif KW >= 151 and KW <= 200:
    price = 100*550 + 50*750 + 50*950 + (KW-200)*1350
VAT=0.1
Thanh_tien=price+price*VAT
print("Tien dien phai tra=", Thanh_tien)
