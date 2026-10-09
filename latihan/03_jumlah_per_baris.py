# Program: Jumlah per Baris
# Loop luar menentukan baris.
# Loop dalam menghitung hasil perkalian pada setiap baris.
# total_baris direset setiap kali baris baru dimulai.

for i in range(1, 5):
    total_baris = 0

    for j in range(1, 4):
        total_baris += i * j

    print(f"Jumlah baris {i} = {total_baris}")
    