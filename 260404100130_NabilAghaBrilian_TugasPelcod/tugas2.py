nama = input("Nama lengkap: ")
nim = input("NIM: ")
kota_tujuan = input("Kota tujuan (Surabaya/Sumenep/Malang): ").lower()
berat_bagasi = float(input("Berat bagasi (kg): "))
punya_ktm = input("Punya KTM? (ya/tidak): ").lower() == "ya"

kelas = input('Kelas tiket ("ekonomi"/"eksekutif"): ').lower()
hari = input('Hari keberangkatan ("weekday"/"weekend"): ').lower()

tarif = {"surabaya": 25000, "sumenep": 45000, "malang": 60000}

if kota_tujuan not in tarif:
    print("Kota tujuan tidak dilayani.")
    exit()

if kelas == "eksekutif" and kota_tujuan == "surabaya":
    print("Pesanan ditolak: kelas eksekutif tidak tersedia untuk rute Surabaya.")
    exit()

harga = tarif[kota_tujuan]

if kelas == "eksekutif":
    harga += 25000
elif kelas != "ekonomi":
    print("Kelas tiket tidak valid.")
    exit()

if hari == "weekend":
    harga *= 1.15
elif hari != "weekday":
    print("Hari keberangkatan tidak valid.")
    exit()

if punya_ktm:
    harga *= 0.90

if berat_bagasi <= 20:
    biaya_bagasi = 0
elif berat_bagasi <= 30:
    biaya_bagasi = (berat_bagasi - 20) * 5000
else:
    print("Pesanan ditolak: bagasi lebih dari 30 kg harus dikirim lewat kargo.")
    exit()

total = harga + biaya_bagasi

print("\n===== DATA PEMESANAN =====")
print("Nama           :", nama)
print("NIM            :", nim)
print("Kota tujuan    :", kota_tujuan.title())
print("Kelas tiket    :", kelas.title())
print("Hari           :", hari)
print("Berat bagasi   :", berat_bagasi, "kg")
print("Punya KTM      :", "Ya" if punya_ktm else "Tidak")
print("Harga tiket    : Rp{:,.0f}".format(harga))
print("Biaya bagasi   : Rp{:,.0f}".format(biaya_bagasi))
print("Total bayar    : Rp{:,.0f}".format(total))