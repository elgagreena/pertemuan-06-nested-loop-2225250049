# PERTEMUAN 06 — NESTED LOOP, POLA, AKUMULASI, DAN PENCACAHAN

## Identitas Mahasiswa

Nama  : Elga Greena Rahma Tazkia
NIM   : 2225250049
Kelas : 3B
Mata Kuliah : Algoritma dan Pemrograman Pendidikan Matematika

## Tujuan Pembelajaran

Melalui praktikum ini, saya mempelajari penggunaan nested loop atau perulangan bersarang, pembuatan pola menggunakan perulangan, akumulasi untuk menghitung jumlah, serta pencacahan untuk menghitung banyaknya kejadian yang memenuhi kondisi tertentu.

## Struktur Folder

pertemuan-06-nested-loop-2225250049/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_pasangan_indeks.py
│   ├── 02_pola_segitiga.py
│   ├── 03_jumlah_per_baris.py
│   └── 04_hitung_pasangan.py
└── tugas/
    └── tabel_perkalian_dan_statistik.py

## Cara Menjalankan Program

1. Buka folder pertemuan-06-nested-loop-2225250049 di Visual Studio Code.
2. Buka terminal pada folder tersebut.
3. Jalankan program yang ingin diuji dengan perintah berikut.

Latihan 1:
python latihan/01_pasangan_indeks.py

Latihan 2:
python latihan/02_pola_segitiga.py

Latihan 3:
python latihan/03_jumlah_per_baris.py

Latihan 4:
python latihan/04_hitung_pasangan.py

Tugas 3:
python tugas/tabel_perkalian_dan_statistik.py

## Ringkasan Latihan

### Latihan 1 — Pasangan Indeks

Program menggunakan dua perulangan bersarang untuk menampilkan pasangan nilai i dan j. Variabel count digunakan untuk menghitung seluruh pasangan yang dihasilkan.

Dengan i dari 1 sampai 3 dan j dari 1 sampai 4, terdapat 12 pasangan.

### Latihan 2 — Pola Segitiga

Program meminta masukan bilangan positif n. Jika n kurang dari atau sama dengan nol, program meminta masukan kembali.

Perulangan luar menentukan baris, sedangkan perulangan dalam mencetak tanda bintang sesuai nomor baris.

### Latihan 3 — Jumlah per Baris

Program menggunakan nested loop untuk menghitung jumlah hasil perkalian pada setiap baris. Variabel total_baris diatur kembali menjadi nol setiap kali memasuki baris baru.

Hasil pengujian:
- Baris 1 = 6
- Baris 2 = 12
- Baris 3 = 18
- Baris 4 = 24

### Latihan 4 — Menghitung Pasangan

Program menghitung pasangan nilai i dan j yang memenuhi kondisi i + j <= n. Variabel count bertambah satu setiap kali kondisi tersebut terpenuhi.

Hasil yang diharapkan:
- n = 2 menghasilkan 1 pasangan.
- n = 3 menghasilkan 3 pasangan.
- n = 5 menghasilkan 10 pasangan.

## Tugas 3 — Tabel Perkalian dan Statistik

Program menampilkan tabel perkalian berukuran n × n, menghitung jumlah setiap baris, menghitung total seluruh hasil perkalian, serta menghitung banyaknya hasil perkalian yang genap.

### Algoritma

1. Menampilkan judul program.
2. Meminta masukan bilangan positif n.
3. Jika n kurang dari atau sama dengan nol, meminta masukan kembali.
4. Menginisialisasi total_semua dan count_genap dengan nilai nol.
5. Menggunakan perulangan luar untuk menentukan baris tabel.
6. Menginisialisasi total_baris dengan nol pada setiap baris.
7. Menggunakan perulangan dalam untuk menentukan kolom dan menghitung hasil perkalian i × j.
8. Menampilkan hasil perkalian.
9. Menambahkan hasil perkalian ke total_baris dan total_semua.
10. Jika hasil perkalian genap, menambah count_genap sebanyak satu.
11. Setelah satu baris selesai, menampilkan jumlah baris tersebut.
12. Setelah seluruh tabel selesai, menampilkan total seluruh hasil dan banyak hasil genap.

### Hasil Pengujian Tugas 3

Pengujian dengan n = 1:
- Total seluruh hasil = 1
- Banyak hasil genap = 0

Pengujian dengan n = 2:
- Jumlah baris pertama = 3
- Jumlah baris kedua = 6
- Total seluruh hasil = 9
- Banyak hasil genap = 3

Pengujian dengan n = 3:
- Jumlah baris pertama = 6
- Jumlah baris kedua = 12
- Jumlah baris ketiga = 18
- Total seluruh hasil = 36
- Banyak hasil genap = 5

## Analisis Efisiensi

Pada Tugas 3, perulangan luar berjalan sebanyak n kali dan setiap perulangan luar menjalankan perulangan dalam sebanyak n kali. Oleh karena itu, jumlah operasi utama bertambah sebanding dengan n². Kompleksitas waktu program adalah O(n²).

## Refleksi

Melalui praktikum ini, saya memahami bahwa nested loop dapat digunakan untuk menyelesaikan masalah yang melibatkan baris dan kolom. Saya juga belajar bahwa variabel akumulasi perlu diinisialisasi sesuai kebutuhan. Variabel jumlah baris harus diatur kembali pada setiap baris, sedangkan total keseluruhan dan pencacah hasil genap tetap berjalan sampai seluruh tabel selesai diproses.

## Sumber dan Bantuan

1. Materi Pertemuan 06 — Nested Loop, Pola, Akumulasi, dan Pencacahan.
2. ChatGPT, digunakan sebagai bantuan untuk memahami konsep, menyusun program, dan memeriksa hasil pengujian.