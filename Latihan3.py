nilai1 = float(input("Masukkan nilai 1 : "))
nilai2 = float(input("Masukkan nilai 2 : "))
nilai3 = float(input("Masukkan nilai 3 : "))

rata = (nilai1+nilai2+nilai3)/3

if rata >= 80:
    skor = "A"
elif rata >= 60:
    skor = "B"
elif rata >= 50:
    skor = "C"
elif rata >= 30:
    skor = "D"
else:
    skor = "E"

print()
print("Rata - rata = {:.2f}".format(rata))
print("Skor anda = ", skor)
