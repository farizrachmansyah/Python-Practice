uts = float(input("Masukkan nilai UTS : "))
uas = float(input("Masukkan nilai UAS : "))
vclass = float(input("Masukkan nilai VClass : "))

rata = (uts+uas+vclass)/3
if rata <= 30:
    ipk = 'E'
elif rata <= 50:
    ipk = 'D'
elif rata <= 60:
    ipk = 'C'
elif rata <= 80:
    ipk = 'B'
else:
    ipk = 'A'

print("IPK Anda = ", ipk)
