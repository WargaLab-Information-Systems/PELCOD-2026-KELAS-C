# data diri
nama = 'subhan firmansyah'
nim = '260404100029'
tempat_lahir = 'sampang'
alamat = 'sampang'
hobi = 'main game'
# input tahun lahir dan ipk
tahun_lahir=int(input("masukkan tahun lahir anda:"))
ipk =float(input("masukkan ipk anda:"))
# hitung dan tampilkan
tahun_sekarang= 2026
umur_sekarang=  tahun_sekarang-tahun_lahir
jumlah_karakter_nama = len(nama)
# tampilkan seluruh data diri
print("\nDATA DIRI SAYA:")
print("nama saya:", nama)
print("nim saya:", nim)
print("tempat lahir saya:",tempat_lahir)
print("alamlat saya:", alamat)
print("hobi saya:", hobi)
print("umur saya sekarang:", umur_sekarang)
print("umur saya 10 tahun lagi:", umur_sekarang+10)
print("jumlah karakter nama termasuk spasi:", jumlah_karakter_nama)
print("tahun saat saya berumur 30 tahun:", tahun_lahir+30)
# type data semua variabel
print("\nTYPE DATA SEMUA VARIABEL:")
print("nama:", type(nama))
print("nim:", type(nim))
print("tempat lahir:", type(tempat_lahir))
print("alamat:", type(alamat))
print("hobi:", type(hobi))
print("tahun lahir:", type(tahun_lahir))
print("ipk:", type(ipk))
print("tahun sekarang:", type(tahun_sekarang))
print("umur sekarang:", type(umur_sekarang))
print("jumlah karakter nama:", type(jumlah_karakter_nama))