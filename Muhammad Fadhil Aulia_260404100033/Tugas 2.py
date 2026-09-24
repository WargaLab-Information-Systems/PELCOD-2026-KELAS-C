nama = (input("Masukkan nama Anda: "))
ipk = float(input("Masukkan IPK Anda: "))
nim = (input("Masukkan NIM Anda: "))
semester = int(input("Masukkan semester Anda: "))

print("\n===============================")

mahasiswaAktif = (input("\nApakah Anda mahasiswa aktif? (true/false): ")).strip().lower()
punyaDenda = (input("\nApakah Anda memiliki denda? (true/false): ")).strip().lower()


print("=== Hanya Menyewakan LAPTOP dan TABLET ===")
jenisPerangkat = {"Laptop": 50000, "Tablet": 30000}
print("0.", list(jenisPerangkat.keys())[0])
print("1.", list(jenisPerangkat.keys())[1])
pilihan = int(input("\nPilih jenis perangkat yang akan anda pinjam (0/1): "))
if pilihan > 1:
    print("Pilihan tidak tersedia, silahkan pilih LAPTOP atau TABLET")
else:
    lamaPeminjaman = int(input("\nMasukkan lama peminjaman (dalam hari): ")) 

    if mahasiswaAktif != "true":
        print("Peminjaman Anda Telah Ditolak")
    elif punyaDenda != "false":
        print("Peminjaman Anda Telah Ditolak")
    elif semester < 3:
        print("\nmaksimal peminjamanmu Hanya sampai 3 HARI")
        if lamaPeminjaman > 3:
            print("Maaf Peminjamanmu hanya sampai 3 hari")
        else:
            print("Peminjamanmu Telah Diterima")
    elif semester >= 3 and semester <= 6:
        print("\nMaksimal Peminjaman 5 Hari")
        if lamaPeminjaman > 6:
            print("Maaf Peminjamanmu hanya sampai 5 hari")
        else:
            print("Peminjamanmu Telah Diterima")
    elif semester > 6:
        print("\nMaksimal Peminjaman 7 Hari")
        if lamaPeminjaman > 8:
            print("Maaf Peminjamanmu hanya sampai 7 hari")
        else:
            print("Peminjamanmu Telah Diterima")
    else:
        print("Peminjamanmu Telah Diterima")

namaPerangkat = list(jenisPerangkat.keys())[pilihan]
hargaSewaPerHari = jenisPerangkat[namaPerangkat]
biayaAdministrasi = hargaSewaPerHari * lamaPeminjaman

if lamaPeminjaman <= 3:
    biayaPerawatan = 0
else:
    biayaPerawatan = (lamaPeminjaman - 3) * 3000

diskon1 = 1.00
diskon2 = 0.50

if ipk >= 3.50:
    print("\nSelamat Anda Tidak Perlu Membayar Biaya Sewa")
    biayaAdminSetelahDiskon = biayaAdministrasi - (biayaAdministrasi * diskon1)
elif ipk >= 3.00 and ipk <= 3.49:
    print("Selamat anda mendapatkan diskon sebesar 50%")
    biayaAdminSetelahDiskon = biayaAdministrasi - (biayaAdministrasi * diskon2)
else:
    print("Maaf Anda Tidak Mendapatkan Diskon, Silahkan Bayar Biaya Sewa Sesuai Harga Sewa")
    biayaAdminSetelahDiskon = biayaAdministrasi

totalPembayaran = biayaAdminSetelahDiskon + biayaPerawatan

print("\n=== RINCIAN BIAYA SEWA ===")
print("Perangkat yang disewa :", namaPerangkat)
print("Biaya Administrasi (sebelum diskon) : Rp.", biayaAdministrasi)
print("Biaya Administrasi (setelah diskon) : Rp.", biayaAdminSetelahDiskon)
print("Biaya Perawatan : Rp.", biayaPerawatan)
print("Total Pembayaran : Rp.", totalPembayaran)

print("\n==== TOLONG BAYAR SESUAI DENGAN TOTAL BIAYA SEWA DI ATAS YA  ====")
uangDibayar = input(" (Masukkan nominal uang Anda): ")

print("Selamat Jalan, Jangan Lupa Kembalikan Perangkatnya yaa")
