# mendefinisikan daftar pilihan mobil
print ("1. brio -150.000/hari")
print ("2. avanza -200.000/hari")
print ("3. fortuner -350.000/hari")

# membuat inputan
pilihan= int(input("pilih mobil 1-3 :"))
hari = int(input("masukkan lama sewa(hari : "))
kupon = input("masukkan kupon :")

# membuat jenis pilihan mobil
if pilihan==1:
    mobil = "brio"
    harga = 150000
elif pilihan == 2:
    mobil = "avanza"
    harga = 200000
elif pilihan ==3:
    mobil = "fortuner"
    harga = 350000
else :
    mobil = "tidak tersedia"
    harga = 0

# menghitung harga sewa
sewa = harga * hari

# mengecek lama sewa
if hari > 3:
    asuransi = 25000
else :
    asuransi = 0

# menghitung subtotal
subtotal = sewa + asuransi

# mengecek subtotal
if subtotal >= 500000:
    diskon1 = subtotal * 10/100
else :
    diskon1 = 0

# mengurangi subtotal dengan diskon 10%
setelah_diskon = subtotal - diskon1

# mengecek diskon kupon
if kupon =="AMBATUNER":
    diskon2 = setelah_diskon * 5/100
else :
    diskon2 = 0

# menghitung total setelah diskon
total = setelah_diskon - diskon2

print("jenis mobil:", mobil)
print("lama sewa:", hari)
print("subtotal:", subtotal)
print("Diskon 1:", diskon1)
print("Diskon 2:", diskon2)
print("total bayar:", total)

