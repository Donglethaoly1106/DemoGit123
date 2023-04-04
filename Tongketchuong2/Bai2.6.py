ho_ten = input("Họ tên: ")
so_ngay_cong = int(input("Số ngày công: "))
don_gia_ngay_cong = float(input("Đơn giá ngày công: "))
he_so_phu_cap = float(input("Hệ số phụ cấp: "))
tam_ung = int(input("Tiền tạm ứng: "))

luong = don_gia_ngay_cong * so_ngay_cong * he_so_phu_cap
thuc_linh = luong - tam_ung

print("Nhan vien ", ho_ten, "Co co Luong=", luong, "Tam ung=", tam_ung, "va Thuc linh=", thuc_linh)






