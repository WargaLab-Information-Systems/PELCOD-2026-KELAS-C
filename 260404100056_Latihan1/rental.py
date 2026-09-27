print("1. Brio - 150.000/hari")
print("2. Avanza - 200.000/hari")
print("3. Fortuner - 250.000/hari")
print()

pilihan = int(input("Pilih Mobil 1-3: "))
durasiSewa = int(input("Berapa lama kamu akan menyewa? "))
kupon = input("Masukkan Kupon: ")
print()

if pilihan == 1:
    mobil = "Brio"
    harga = 150000
elif pilihan == 2:
    mobil = "Avanza"
    harga = 200000
elif pilihan == 3:
    mobil = "Fortuner"
    harga = 250000
else :
    mobil = "Tidak Tersedia"
    harga = 0

biayaSewa = harga * durasiSewa

if durasiSewa > 3:
    asuransi = 25000
else:
    asuransi = 0

subTotal = biayaSewa + asuransi

if subTotal >= 500000:
    diskonSewa = subTotal * 10/100
else:
    diskonSewa = 0

setelahDiskon = subTotal - diskonSewa

if kupon == "AMBATUNER":
    diskonKupon = setelahDiskon * 5/100
else:
    diskonKupon = 0

total = setelahDiskon - diskonKupon

print(f"Jenis mobil: {mobil}")
print(f"Lama sewa: {durasiSewa} Hari")
print(f"Asuransi: Rp{asuransi}")
print()
print(f"Sub-Total: Rp{subTotal}")
print(f"Diskon Sewa: Rp{diskonSewa}")
print(f"Diskon Kupon: Rp{diskonKupon}")
print()
print(f"Total Bayar: Rp{total}")
print()
