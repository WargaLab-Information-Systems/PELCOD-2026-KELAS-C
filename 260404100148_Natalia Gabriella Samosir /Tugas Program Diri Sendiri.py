# ==========================================
# PROGRAM 1 - DATA DIRI
# ==========================================

# Data diri
nama = "Natalia Gabriella Samosir"
nim = "260404100148"
tempat_lahir = "Jakarta, 13-12-2007"
alamat = "Jl. Reformasi II No. 78, Jakarta"
hobi = "Menyanyi dan Menari"

# Input
tahun_lahir = int(input("Masukkan tahun lahir : "))
ipk = float(input("Masukkan IPK          : "))

# Proses
tahun_sekarang = 2026
umur = tahun_sekarang - tahun_lahir
umur_10_tahun = umur + 10
jumlah_karakter = len(nama)
tahun_umur_30 = tahun_lahir + 30

# Output
print("\n===================================")
print("          DATA DIRI MAHASISWA")
print("===================================")

print("Nama Lengkap       :", nama)
print("NIM                :", nim)
print("Tempat Lahir       :", tempat_lahir)
print("Alamat             :", alamat)
print("Hobi               :", hobi)
print("Tahun Lahir        :", tahun_lahir)
print("IPK                :", ipk)

print("-----------------------------------")
print("Umur Saat Ini      :", umur, "tahun")
print("Umur 10 Tahun Lagi :", umur_10_tahun, "tahun")
print("Jumlah Karakter    :", jumlah_karakter)
print("Umur 30 Tahun      :", tahun_umur_30)

print("-----------------------------------")
print("Tipe Data Variabel")
print("Nama               :", type(nama))
print("NIM                :", type(nim))
print("Tempat Lahir       :", type(tempat_lahir))
print("Alamat             :", type(alamat))
print("Hobi               :", type(hobi))
print("Tahun Lahir        :", type(tahun_lahir))
print("IPK                :", type(ipk))
print("===================================")