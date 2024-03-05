nama = input("Masukkan nama anda: ")
jumlah_hari_kerja = int(input("Masukkan jumlah hari kerja dalam sebulan: "))
jam_kerja_per_hari = int(input("Masukkan jam kerja per hari: "))
gaji_per_hari = 100000

total_gaji = jumlah_hari_kerja * gaji_per_hari * jam_kerja_per_hari

if jam_kerja_per_hari > 8:
    gaji_per_jam_lembur = 10000
    lembur = (jam_kerja_per_hari - 8) * gaji_per_jam_lembur
    total_gaji += lembur
# Menggunakan string formatting untuk menambahkan titik sebagai pemisah ribuan
total_gaji = f"{total_gaji:,.2f}"

print("\nNama:",nama)
print("Total gaji yang diterima",nama,"adalah: Rp.",total_gaji)