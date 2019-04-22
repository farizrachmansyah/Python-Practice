# Tugas AP 2B
# Kelompok:
# 1. Ahmad Rifaldy Mandaya
# 2. Dicky Millian
# 3. Fariz Rachmansyah
# Kelas 1IA09

# python versi 3


def penjumlahan():
	hasil = 0
	wadah = int(input("Masukkan Angka Max. Pertambahan : "))
	for i in range(wadah):
		i += 1
		print("Hasil dari", i, "+", hasil, "=", hasil+i)
		hasil = hasil + i


def perkalian():
	hasil = 1
	wadah = int(input("Masukkan Angka Max. Perkalian : "))
	for i in range(wadah):
		i += 1
		print("Hasil dari", i, "*", hasil, "=", hasil*i)
		hasil = hasil * i


def main():
	ulang = True
	while ulang:
		print("======= Perhitungan Sederhana List =======")
		print()
		print("1. Penjumlahan")
		print("2. Perkalian")
		print("3. Exit")
		pil = int(input("Masukkan pilihan anda [1-3] : "))

		if pil == 1:
			penjumlahan()
			tanya = input("Do you wanna repeat it [yes or no]? ")
			if tanya == "y" or tanya == "Y":
				print()
				ulang = True
			else:
				ulang = False
		elif pil == 2:
			perkalian()
			tanya = input("Do you wanna repeat it [yes or no]? ")
			if tanya == "y" or tanya == "Y":
				ulang = True
			else:
				ulang = False
		elif pil == 3:
			ulang = False
		else:
			print("Salah Input Bos!")
			print()


main()
