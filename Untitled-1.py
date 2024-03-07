print ('''\n==============________________________============
              PROGRAM PERHITUNGAN GAJI
==============________________________============\n\n''')

#-----------------------format Rupiah---------------------#

def format_rupiah(angka):
    return "Rp {:,}".format(angka)

                        #~MENGHITUNG~#
#----------------------------------------------------------#
def hitung_gaji_total(hari_kerja, hari_kerja_tetap, gaji_pokok, rate_lembur, jam_lembur):
    gaji_per_hari = gaji_pokok // hari_kerja_tetap
    gaji_tetap = hari_kerja * gaji_per_hari
    gaji_lembur = jam_lembur * rate_lembur
    gaji_total = gaji_tetap + gaji_lembur
    return int(gaji_total)

                    #~MEMINTA PENGGUNA MENGISI~#
#-----------------------------------------------------------#
nama  = (input("Masukkan Nama Pekerja: "))
provesi = (input("Masukkan provesi pekerja: "))
hari_kerja = int(input("Masukkan jumlah hari bekerja: "))
hari_kerja_tetap = int(input("Masukkan jumlah hari kerja tetap dalam satu bulan: "))
gaji_pokok = int(input("Masukkan gaji pokok: "))
rate_lembur = int(input("Masukkan gaji lembur tetap/jam: "))
jam_lembur = int(input("Masukkan jumlah jam lembur pekerja: "))
gaji_total = hitung_gaji_total(hari_kerja, hari_kerja_tetap, gaji_pokok, rate_lembur, jam_lembur)

                        #~TAMPILKAN HASIL#~
#---------------------------------------------------------------#
print(f"\nTotal gaji Anda adalah:" ,format_rupiah(gaji_total),",00\n")
print ( '''>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<
   ~_~  (Terima Kasih Telah Bekrja Dengan Baik)  ~_~
>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<\n''')