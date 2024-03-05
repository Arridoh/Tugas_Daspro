nama = input('Masukkan nama anda : ')
hari_kerja = int(input('Masukkan kehadiran : '))
if hari_kerja <= 32 :
    hari_kerja_perbulan = 24
    gaji = 3500000

    if hari_kerja > hari_kerja_perbulan :
        harilembur = hari_kerja - hari_kerja_perbulan
        lembur = (harilembur)* 150000
        hari_kerja1 = hari_kerja
        hari_kerja1 = hari_kerja_perbulan    
    else :
        lembur = 0

    Totalgaji= int((hari_kerja1/hari_kerja_perbulan)*gaji + lembur)
    Totalgaji = f"{Totalgaji:,}"
    print("\nNama :", nama)
    print(f"Kehadiran anda : {hari_kerja} hari")
    if lembur > 0:
        print(f"Anda lembur selama {harilembur} hari.")
    else :
        print("Anda tidak lembur")
    print(f"gaji yang didapatkan {nama} adalah Rp.", Totalgaji)
else :
    print('\nKehadiran yang diinputkan tidak sesuai, mohon coba lagi', nama)