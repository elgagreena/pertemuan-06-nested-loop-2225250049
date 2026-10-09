# Program: Tabel Perkalian dan Statistik
# Loop luar mengatur baris tabel.
# Loop dalam mengatur kolom tabel.
# total_baris menghitung jumlah pada setiap baris.
# total_semua menghitung jumlah seluruh hasil perkalian.
# count_genap menghitung banyak hasil perkalian yang genap.

print("Tabel Perkalian dan Statistik")

n = int(input("Masukkan n: "))

while n <= 0:
    print("n harus bilangan positif.")
    n = int(input("Masukkan n: "))

total_semua = 0
count_genap = 0

for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j

        print(f"{hasil:4}", end="")

        total_baris += hasil
        total_semua += hasil

        if hasil % 2 == 0:
            count_genap += 1

    print(f"   | jumlah baris = {total_baris}")

print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")
