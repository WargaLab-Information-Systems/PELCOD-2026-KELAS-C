
nama = input ("masukkan nama :")
usia  =int (input("masukkan usia :"))
tinggi_badan = int (input ("masukkan tinggi badan :"))

harga_tiket = 50000
harga_fast_track = 25000

if usia >= 12 and tinggi_badan >= 140:
    fast_track = input ("apakah kamu ingin membeli fast track? (y/n) : ")
    if fast_track == "y" :
        total_harga = harga_tiket + harga_fast_track
        status_tiket = "fast track"
    else :
        total_harga = harga_tiket
        status_tiket= "reguler"

    print ("hasil cek verifikasi tiket dan harga tiket")
    print ("nama : ", nama)
    print ("usia : ", usia)
    print ("tinggi badan : ", tinggi_badan)
    print ("status tiket : ", status_tiket)
    print ("total harga tiket : ", total_harga)
else :
    print("")
    print(nama, "karena usia kamu tidak memenuhi syarat untuk naik wahana ini")