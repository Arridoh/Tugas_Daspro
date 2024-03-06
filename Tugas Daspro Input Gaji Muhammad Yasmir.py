welcome = '''
=====================================================================
============================Welcome To===============================
=====================================================================
======================Pengecekan Penggajian==========================
=====================================================================
'''
print (welcome)
print ("Silahkan Isi Data Dibawah Ini Untuk Menentukan Gaji Anda")
nama = str (input ("Masukan Nama Anda: "))
hari_kerja = int(input ("Masukan Hari Kerja: "))
hari_kerja_perbulan = int (25)
gaji_pokok = 2500000
uang_lembur = 250000

if hari_kerja>hari_kerja_perbulan:
    lembur= (hari_kerja-hari_kerja_perbulan)*uang_lembur
else:
    lembur= 0

total_gaji = int ((hari_kerja/hari_kerja_perbulan)*gaji_pokok+lembur)

print ("\nNama Karyawan:",nama)
print ("Gaji Anda Bulan Ini Rp. {:,}".format (total_gaji))