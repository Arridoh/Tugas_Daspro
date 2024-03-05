nama = input('Masukkan nama anda : ')
hari_kerja = int(input('Masukkan kehadiran : '))

# Tetapkan kehadiran perbulan & gaji
hari_kerja_perbulan = 24
gaji = 3500000

# setiap 1 hari lembur mendapatkan gaji tambahan Rp.150,000
# ketika hari kerja lebih dari hari kerja perbulan
# maka tambahan gaji hanya didapat dari gaji lembur
if hari_kerja > hari_kerja_perbulan :
    harilembur = hari_kerja - hari_kerja_perbulan
    lembur = (harilembur)* 150000
    hari_kerja1 = hari_kerja
    hari_kerja1 = hari_kerja_perbulan    
    Totalgaji= int((hari_kerja1/hari_kerja_perbulan)*gaji)
    Totalgaji += lembur
else :
    lembur = 0
    Totalgaji= int((hari_kerja/hari_kerja_perbulan)*gaji)

Totalgaji = f"{Totalgaji:,}"
print("\nNama:", nama)
print(f"Kehadiran anda: {hari_kerja} hari")
if lembur > 0:
    print(f"Anda lembur selama {harilembur} hari.")
else :
    print("Anda tidak lembur")
print(f"gaji yang didapatkan {nama} bulan ini: Rp.", Totalgaji)