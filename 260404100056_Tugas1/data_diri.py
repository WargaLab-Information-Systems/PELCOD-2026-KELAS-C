# Taruh data di dalam variabel
student_name = "Tantra Firjatullah"
student_nim = "260404100056"
student_bornIn = "Sampang"
student_address = "Jalan Mutiara, Gg. 2, No. 14"
student_hobby = "Membaca"

# student_name = input("Masukkan Nama: ")
# student_nim = input("Masukkan NIM: ")
# student_bornIn = input("Masukkan Tempat Lahir: ")
# student_address = input("Masukkan Alamat: ")
# student_hobby = input("Masukkan Hobby: ")

# Input tahun lahir dan IPK mahasiswa
print()
student_birthYear = int(input("Masukkan tahun kelahiran kamu: "))
student_GPA = float(input("Masukkan IPK kamu: "))
print()

# tahun saat ini
current_year = 2026

# Hitung dan tampilkan umur saat ini
student_age = current_year - student_birthYear

if (student_birthYear < current_year and student_birthYear > 1900) and (student_GPA >= 0 and student_GPA <= 4) :
    print("Umur kamu sekarang =", student_age)
    print(f"Umur kamu 10 tahun kedepan = {student_age + 10}")
    print(f"Nama kamu memiliki {len(student_name)} karakter!")
    print("kamu berumur 30 tahun pada tahun", (student_birthYear + 30))
    print()

    # Tampilkan seluruh data diri
    print(f"Nama: {student_name}")
    print(f"NIM: {student_nim}")
    print(f"Lahir di: {student_bornIn}, pada tahun {student_birthYear}")
    print(f"Alamat: {student_address}")
    print(f"IPK : {student_GPA}")
    print(f"Hobby: {student_hobby}")
    print()

    # Tampilkan seluruh tipe variabel yang digunakan
    print("variabel student_name bertipe", type(student_name))
    print("variabel student_nim bertipe", type(student_nim))
    print("variabel student_bornIn bertipe", type(student_bornIn))
    print("variabel student_birthYear bertipe", type(student_birthYear))
    print("variabel student_address bertipe", type(student_address))
    print("variabel student_GPA bertipe", type(student_GPA))
    print("variabel student_hobby bertipe", type(student_hobby))
    print("variabel current_year bertipe", type(current_year))
    print("variabel student_age bertipe", type(student_age))
    print()
else:
    print("Data yang di-input tidak valid!")
