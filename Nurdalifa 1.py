print ('''\n~~~~~~~~~~~~~~~~~~~~~~        ~~~~~~~~~~~~~~~~~~~~
              APLIKASI MENGHITUNG GAJI
~~~~~~~~~~~~~~~~~~~~~        ~~~~~~~~~~~~~~~~~~~~~\n\n''')

def format_rupiah(angka):
    return "Rp {:,}".format(angka)
def hitung_gaji_total(hari_kerja, hari_kerja_tetap, gaji_pokok, rate_lembur, jam_lembur):
    gaji_per_hari = gaji_pokok // hari_kerja_tetap
    gaji_tetap = hari_kerja * gaji_per_hari
    gaji_lembur = jam_lembur * rate_lembur
    gaji_total = gaji_tetap + gaji_lembur
    return int(gaji_total)

#=====================================================================================#
nama  = (input("Nama Karyawan: "))
provesi = (input("Bidang Pekerjaan: "))
hari_kerja = int(input("jumlah hari bekerja: "))
hari_kerja_tetap = int(input("jumlah hari kerja tetap dalam satu bulan: "))
gaji_pokok = int(input("gaji pokok: "))
rate_lembur = int(input("gaji lembur tetap/jam: "))
jam_lembur = int(input("jumlah jam lembur pekerja: "))
gaji_total = hitung_gaji_total(hari_kerja, hari_kerja_tetap, gaji_pokok, rate_lembur, jam_lembur)

#======================================================================================#

print(f"\nTotal gaji Anda adalah:" ,format_rupiah(gaji_total),",00\n")
print ( '''
   ~_~  (Terima Kasih Telah Bekrja Dengan Baik)  ~_~
\n''')