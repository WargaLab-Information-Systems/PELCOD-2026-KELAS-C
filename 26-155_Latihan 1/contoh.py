# mendefinisikan daftar pilihan mobil
print("1. Brio - 150.000/hari")
print("1. Avanza - 200.000/hari")
print("1. Fortuner - 350.000/hari")

# membuat inputan
Pilihan = int (input("Pilih mobil 1-3 :"))
hari = int(input("Masukkan lama sewa (hari :)"))
kupon = input ("Masukkan kupon :")

# menentukan nilai jenis mobil
if Pilihan == 1:
    mobil = "Brio"
    harga = 150000
elif Pilihan == 2:
    mobil = "Avanza"
    harga = 200000
elif Pilihan == 3:
    mobil = "Fortuner"
    harga = 350000
else :
    mobil = "Tidak tersedia"
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
if kupon == "AMBATUNER" :
    diskon2 = setelah_diskon * 5/100
else :
    diskon = 0

# menghitung total setelah diskon 
total = setelah_diskon - diskon2

print("jenis mobil :", mobil)
print("lama sewa:", hari)
print("subtotal:", subtotal)
print("Diskon 1 :", diskon1)
print ("Diskon 2 :", diskon2)
print("Total bayar :", total)