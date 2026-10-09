Nama: Elga Greena Rahma Tazkia
NIM: 2225250049
Kelas: 3B

## Tujuan
Menggunakan nested loop, pola, akumulasi, dan pencacahan.

## Cara Menjalankan
python3 tugas/tabel_perkalian_dan_statistik.py

## Algoritma Tugas 3
1. Loop luar menentukan baris tabel perkalian.
2. Loop dalam menentukan kolom dan menghitung hasil perkalian.
3. Akumulator menghitung jumlah setiap baris dan total seluruh hasil perkalian.
4. Counter menghitung banyak hasil perkalian yang genap.

## Hasil Pengujian

| Input n | Hasil yang Diharapkan | Keluaran Aktual | Status |
|---|---|---|---|
| 1 | Total = 1, hasil genap = 0 | Total = 1, hasil genap = 0 | Berhasil |
| 2 | Total = 9, hasil genap = 3 | Total = 9, hasil genap = 3 | Berhasil |
| 3 | Total = 36, hasil genap = 5 | Total = 36, hasil genap = 5 | Berhasil |

## Analisis Efisiensi
Loop luar berjalan sebanyak n kali dan loop dalam berjalan sebanyak n kali untuk setiap iterasi loop luar. Jadi, badan loop dalam berjalan sebanyak n x n atau n^2 kali. Kompleksitas waktunya adalah O(n^2).

## Refleksi
Salah satu kesalahan dalam nested loop adalah menginisialisasi ulang variabel total_baris di luar loop luar. Akibatnya, jumlah setiap baris tidak dihitung secara terpisah. Cara memperbaikinya adalah menginisialisasi total_baris = 0 di dalam loop luar sebelum loop dalam dijalankan.

