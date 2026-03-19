# Amazon Echo 2 Reviews Analysis 📊

Proyek analitik ini bertujuan untuk mengeksplorasi dan menganalisis sentimen pengguna serta kepuasan pelanggan terhadap produk Amazon Echo. Menggunakan pendekatan statistik deskriptif dan visualisasi data, proyek ini menggali wawasan dari ulasan pelanggan historis.

## 🎯 Tujuan Proyek
Proyek ini dibuat untuk menjawab pertanyaan utama berikut:
* Bagaimana pengaruh varian warna terhadap tingkat kepuasan (rating) pelanggan Amazon Echo?
* Apakah status pembelian terverifikasi (*verified purchase*) memengaruhi kecenderungan pemberian rating yang lebih tinggi atau lebih rendah?
* Varian warna apa yang paling populer berdasarkan jumlah ulasan?

## 📂 Dataset
Dataset yang digunakan dalam proyek ini adalah `Amazon Echo 2 Reviews.csv`. 
Data ini mencakup informasi mengenai:
* Teks ulasan dan judul
* Rating (bintang 1 hingga 5)
* Varian warna produk
* Status verifikasi pengguna (*User Verified*)

## 🛠️ Teknologi & Library yang Digunakan
Proyek ini dibangun menggunakan bahasa pemrograman Python dengan beberapa *library* utama untuk analisis dan visualisasi data:
* **Pandas:** Untuk manipulasi data, pembersihan, dan perhitungan statistik deskriptif.
* **Matplotlib & Seaborn:** Untuk merancang dan membangun visualisasi grafik yang informatif dan menarik.

## 🚀 Cara Menjalankan Proyek
Kamu bisa menjalankan analisis ini secara lokal atau menggunakan platform *cloud* seperti Google Colab.

### Menggunakan Google Colab (Rekomendasi)
1. Buka [Google Colab](https://colab.research.google.com/).
2. Buat *notebook* baru.
3. Unggah file `Amazon Echo 2 Reviews.csv` ke bagian **Files** di menu sebelah kiri Colab.
4. Salin kode Python dari repositori ini dan jalankan (*run*) di *cell* Colab untuk melihat hasil perhitungan dan visualisasi grafiknya.

## 📈 Visualisasi yang Dihasilkan
Script dalam proyek ini akan menghasilkan tiga grafik utama:
1. **Jumlah Ulasan Berdasarkan Varian Warna** (Barplot)
2. **Rata-rata Rating Berdasarkan Varian Warna** (Barplot)
3. **Rata-rata Rating Berdasarkan Status Pembelian** (Barplot)

---
**Author:** Muhammad Thoriq Nabasa
