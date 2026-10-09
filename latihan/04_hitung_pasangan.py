# Program: Menghitung Pasangan
# Loop luar dan loop dalam membentuk pasangan i dan j.
# Kondisi menentukan pasangan yang dihitung.
# Counter bertambah hanya jika i + j <= n.

n = int(input("Masukkan n: "))

while n <= 0:
    print("n harus bilangan positif.")
    n = int(input("Masukkan n: "))

count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j <= n:
            count += 1

print(f"Banyak pasangan = {count}")
