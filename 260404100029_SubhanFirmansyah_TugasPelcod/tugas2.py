print("PEMINJAMAN PERANGKAT PERPUSTAKAAN KAMPUS")

nama = input("Masukan Nama Anda : ")
semester = int(input("Mahasiswa Semester : "))
nim = input("Masukan NIM anda : ")
ipk = float(input("Masukan IPK anda : "))
mahasiswa_aktif = input("\nApakah anda adalah mahasiswa aktif? (ya/tidak) : ")
if mahasiswa_aktif == "ya" :
    mahasiswa_aktif = True
else :
    mahasiswa_aktif = False
punya_denda = input("apakah anda memiliki denda yang tidak terbayar? (ya/tidak) : ")
if punya_denda == "ya" :
    punya_denda = True
else : 
    punya_denda = False

print("\nTersedia jenis perangkat sebagai berikut:")
print("1. Laptop")
print("2. Tablet")
jenis_perangkat = (input("\nJenis perangkat apa yang anda pinjam? (laptop/tablet) : "))

if mahasiswa_aktif == False :
    print("Peminjaman Ditolak!")
    exit("Peminjaman dihentikan karena mahasiswa tidak aktif.")
elif mahasiswa_aktif == True :
    if punya_denda == True :
        print("Peminjaman Ditolak!")
        exit("Peminjaman dihentikan karena mahasiswa memiliki denda yang belum dibayar.")

lama_peminjaman = int(input("Berapa hari lama peminjaman : "))
if (semester >= 1 and semester <= 2) and lama_peminjaman <= 3 :
    print("Peminjaman Dikonfirmasi!")
elif (semester >= 3 and semester <= 6) and lama_peminjaman <= 5 :
    print("Peminjaman Dikonfirmasi!")
elif (semester >= 7) and lama_peminjaman <= 7 :
    print("Peminjaman Dikonfirmasi!")
else :
    print("Peminjaman Tidak Dapak Dikonfirmasi!")
    if lama_peminjaman > 3 and semester >= 1 and semester <= 2 :
        print("Batas peminjaman untuk semester 1-2 Maksimal 3 hari.")
    elif lama_peminjaman > 5 and semester >= 3 and semester <= 6 :
        print("Batas peminjaman untuk semester 3-6 Maksimal 5 hari.")
    elif lama_peminjaman > 7 and semester >= 7 :
        print("Batas peminjaman untuk semester 7 ke atas Maksimal 7 hari.")
    exit("Peminjaman dihentikan karena lama peminjaman melebihi batas yang ditentukan untuk semester anda.")

if jenis_perangkat == "laptop" :
    print("\nBiaya Administrasi = Rp 50.000")
    biaya_administrasi = 50000
elif jenis_perangkat == "tablet" :
    print("\nBiaya Administrasi = Rp 30.000")
    biaya_administrasi = 30000

if ipk >= 3.50 :
    potongan_biaya = biaya_administrasi * 0
elif ipk >= 3.00 and ipk <= 3.49 :
    potongan_biaya = biaya_administrasi * 50/100
elif ipk <= 2.99 :
    potongan_biaya = biaya_administrasi

if lama_peminjaman >= 4:
    biaya_perawatan = lama_peminjaman * 3000
else:
    biaya_perawatan = 0

total_biaya = potongan_biaya + biaya_perawatan

print("\nNama :", nama)
print("Jenis Perangkat peminjaman :", jenis_perangkat)
print("Lama Peminjaman :", lama_peminjaman, "hari")
print("Biaya Administrasi : Rp", int(biaya_administrasi))
print("Potongan Biaya Administrasi : Rp", int(potongan_biaya))
print("Biaya Perawatan : Rp", int(biaya_perawatan), "untuk", lama_peminjaman, "hari")
print("Total Biaya : Rp", int(total_biaya)) 