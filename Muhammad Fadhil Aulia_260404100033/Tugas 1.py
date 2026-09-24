namaLengkap = "Muhammad Fadhil Aulia"
nim = "260404100033"
tempatLahir = "Madiun"
alamat = "Tambakmas, Kebonsari, Madiun"
hobi = "Menulis"

tahunLahir = int(input("Masukkan Tahun Lahir = "))
ipk = float(input("Masukkan IPK Anda = "))

print("\n===============================")
tahunSekarang = int(input("\nMasukkan Tahun Sekarang = "))
usia = tahunSekarang - tahunLahir
print("sekarang Usia Anda:", usia)
print("Usia Saya 10 Tahun Kedepan:", usia + 10)

print("\n===============================")
print("\nJumlah Karakter", namaLengkap, ":", len(namaLengkap))
tahunLahirKedepan = tahunLahir + 30

print("\n===============================")
print(f"\nNAMA LENGKAP SAYA: {namaLengkap}")
print(f"NIM: {nim}")
print(f"TEMPAT TANGGAL LAHIR: {tempatLahir}")
print(f"ALAMAT: {alamat}")
print(f"HOBI: {hobi}")
print(f"TAHUN LAHIR: {tahunLahir}")
print(f"USIA: {usia}")