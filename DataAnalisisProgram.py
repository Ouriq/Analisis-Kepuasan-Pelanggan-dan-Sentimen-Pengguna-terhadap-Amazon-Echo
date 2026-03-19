# Mengimpor library pandas untuk manipulasi data
import pandas as pd

# 1. MEMUAT DATA
# Ganti nama file sesuai dengan lokasi file Anda jika diperlukan
df = pd.read_csv('Amazon Echo 2 Reviews.csv')

# Menampilkan 5 baris pertama untuk melihat sekilas isi data
print("--- 5 Baris Pertama Dataset ---")
display(df.head())

# 2. MEMBERSIHKAN DATA (Opsional tapi disarankan)
# Mengecek apakah ada data yang kosong (Missing Values)
print("\n--- Jumlah Data Kosong per Kolom ---")
print(df.isnull().sum())

# 3. ANALISIS DESKRIPTIF
print("\n--- HASIL ANALISIS ---")

# a. Menghitung Rata-rata Rating Keseluruhan
rata_rata_rating = df['Rating'].mean()
print(f"1. Rata-rata Rating Keseluruhan: {rata_rata_rating:.2f} dari 5.0")

# b. Melihat Distribusi Warna (Berapa banyak ulasan untuk setiap warna?)
distribusi_warna = df['Review Color'].value_counts()
print("\n2. Jumlah Ulasan Berdasarkan Varian Warna:")
print(distribusi_warna)

# c. Menganalisis Rata-rata Rating Berdasarkan Warna
# Ini menjawab: "Apakah warna tertentu memiliki rating yang lebih baik?"
rating_per_warna = df.groupby('Review Color')['Rating'].mean().round(2)
print("\n3. Rata-rata Rating Berdasarkan Warna:")
print(rating_per_warna)

# d. Menganalisis Pengaruh Status 'Verified Purchase' terhadap Rating
rating_verified = df.groupby('User Verified')['Rating'].mean().round(2)
print("\n4. Rata-rata Rating Berdasarkan Status Pembelian:")
print(rating_verified)