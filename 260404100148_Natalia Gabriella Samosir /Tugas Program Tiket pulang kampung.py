# ==========================================
# PROGRAM 2 - TIKET BUS PULANG KAMPUNG
# ==========================================

# Data diri
nama = "Natalia Gabriella Samosir"
nim = "260404100148"
kota_tujuan = "Bali"
berat_bagasi = 17.0
punya_ktm = True

print("======================================")
print("       TIKET BUS PULANG KAMPUNG")
print("======================================")

# Input
kelas_tiket = input("Masukkan kelas tiket (ekonomi/eksekutif): ").lower()
hari = input("Masukkan hari (weekday/weekend): ").lower()

# Menentukan tarif kota
if kota_tujuan.lower() == "surabaya":
    tarif_dasar = 250000

elif kota_tujuan.lower() == "jakarta":
    tarif_dasar = 450000

elif kota_tujuan.lower() == "bali":
    tarif_dasar = 600000

else:
    tarif_dasar = 0
    print("\nKota tujuan tidak dilayani.")

# Jika kota tersedia
if tarif_dasar > 0:

    # Menentukan kelas tiket
    if kelas_tiket == "ekonomi":
        tambahan_kelas = 0

    elif kelas_tiket == "eksekutif":

        if kota_tujuan.lower() == "surabaya":
            print("\nKelas eksekutif tidak tersedia untuk Surabaya.")
            tambahan_kelas = -1
        else:
            tambahan_kelas = 250000

    else:
        print("\nKelas tiket tidak valid.")
        tambahan_kelas = -1

    # Jika kelas valid
    if tambahan_kelas >= 0:

        harga = tarif_dasar + tambahan_kelas

        # Tambahan weekend
        if hari == "weekend":
            harga = harga * 1.15

        elif hari == "weekday":
            harga = harga

        else:
            print("\nHari keberangkatan tidak valid.")
            harga = -1

        # Jika hari valid
        if harga >= 0:

            # Diskon KTM
            if punya_ktm == True:
                diskon = harga * 0.10
            else:
                diskon = 0

            harga_setelah_diskon = harga - diskon

            # Biaya bagasi
            if berat_bagasi <= 20:
                biaya_bagasi = 0

            elif berat_bagasi <= 30:
                kelebihan = berat_bagasi - 20
                biaya_bagasi = kelebihan * 50000

            else:
                print("\nBagasi lebih dari 30 kg.")
                print("Bagasi harus dikirim melalui kargo.")
                biaya_bagasi = -1

            # Jika bagasi memenuhi syarat
            if biaya_bagasi >= 0:

                total = harga_setelah_diskon + biaya_bagasi

                # Output
                print("\n======================================")
                print("          DETAIL PEMESANAN")
                print("======================================")

                print("Nama           :", nama)
                print("NIM            :", nim)
                print("Kota Tujuan    :", kota_tujuan)
                print("Kelas Tiket    :", kelas_tiket)
                print("Hari           :", hari)
                print("Berat Bagasi   :", berat_bagasi, "kg")
                print("Punya KTM      :", punya_ktm)

                print("--------------------------------------")
                print("Tarif Dasar    : Rp", int(tarif_dasar))
                print("Tambahan Kelas : Rp", int(tambahan_kelas))
                print("Diskon KTM     : Rp", int(diskon))
                print("Biaya Bagasi   : Rp", int(biaya_bagasi))
                print("--------------------------------------")
                print("TOTAL BAYAR    : Rp", int(total))

                print("======================================")
                print("       PEMESANAN BERHASIL!")
                print("       SELAMAT JALAN!")
                print("======================================")