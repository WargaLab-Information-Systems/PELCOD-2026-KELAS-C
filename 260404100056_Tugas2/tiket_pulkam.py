# ini data diri di-input atau disimpan langsung kedalam variabel sih?
student_name = "Tantra Firjatullah"
student_nim = "260404100056"
dest_city = "Malang"
luggage_weight = 12.5
is_ktm = True

print()
ticket_class = input("Masukkan tipe tiket (ekonomi atau eksekutif): ")
departure_day = input("Masukkan hari keberangkatan (weekday atau weekend): ")
print()

dest_price = 0
class_price = 0

if dest_city == "Surabaya" or dest_city == "Sumenep" or dest_city == "Malang":
    if dest_city == "Surabaya":
        dest_price = 25000
    elif dest_city == "Sumenep":
        dest_price = 45000
    elif dest_city == "Malang":
        dest_price = 60000

    if not(ticket_class == "eksekutif" and dest_city == "Surabaya"):
        if ticket_class == "eksekutif" or ticket_class == "ekonomi":
            if ticket_class == "ekonomi":
                class_price = 0
            elif ticket_class == "eksekutif":
                class_price = 25000

            ticket_price = dest_price + class_price
            weekend_extra = 0

            if departure_day == "weekday":
                weekend_extra = 0
            elif departure_day == "weekend":
                weekend_extra = ticket_price * 15/100

            subtotal = ticket_price + weekend_extra

            if is_ktm == True:
                diskon1 = subtotal * 10/100
            else:
                diskon1 = 0

            subtotal = subtotal - diskon1
            luggage_penalty = 0

            if luggage_weight > 0:
                if luggage_weight > 30:
                    print("Ditolak. Bagasi harus dikirim lewat kargo.")
                    print()
                else:
                    if luggage_weight > 0 and luggage_weight <= 20:
                        luggage_penalty = 0
                    elif luggage_weight > 20 and luggage_weight <= 30:
                        extra_kg = luggage_weight - 20
                        whole_extra_kg = int(extra_kg)
                        if extra_kg > whole_extra_kg:
                            whole_extra_kg = whole_extra_kg + 1
                        luggage_penalty = whole_extra_kg * 5000

                    total = subtotal + luggage_penalty

                    print(f"Nama: {student_name}")
                    print(f"NIM: {student_nim}")
                    print(f"Kota Tujuan: {dest_city}")
                    print(f"Bawa KTM?: {is_ktm}")
                    print(f"Berat Bagasi: {luggage_weight}kg")
                    print()
                    print(f"Harga destinasi: Rp{dest_price}")
                    print(f"Harga Kelas: Rp{class_price}")
                    print(f"Weekend?: Rp{int(weekend_extra)}")
                    print(f"Diskon 1: Rp{int(diskon1)}")
                    print()
                    print(f"Subtotal: Rp{int(subtotal)}")
                    print(f"Biaya Bagasi: Rp{int(luggage_penalty)}")
                    print()
                    print(f"Total: Rp{int(total)}")
                    print()
        else:
            print("Tipe kelas tidak valid.")
            print()
    else:
        print("Kelas eksekutif tidak tersedia untuk rute Surabaya. Pesanan ditolak.")
        print()
else:
    print("Kota tujuan tidak masuk dalam layanan kami.")
    print()
