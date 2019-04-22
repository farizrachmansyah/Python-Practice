A = 100
nilai = int(input("Masukkan nilai anda : "))

if nilai == A:
    skor = "A"
elif nilai >= 90:
    skor = "B"
elif nilai > 70:
    skor = "C"
elif nilai > 30:
    skor = "D"
else:
    skor = "E"

print("Skor anda = ", skor)
