
Pertemuan 10 - String dan Pengolahan Teks

Nama: Mafatihun Nabila
NIM: 2225250918
Kelas: 3B

## Tujuan

Mengolah dan menormalisasi data teks dengan menggunakan fungsi dan method string pada Python agar data menjadi lebih bersih, seragam, dan mudah dibaca.

## Cara Menjalankan

```bash
python3 tugas/normalisasi_data_mahasiswa.py
```

## Algoritma

1. Program menerima input berupa nama lengkap mahasiswa dan kode kelas.
2. Nama dibersihkan dari spasi berlebih menggunakan strip() dan split(), kemudian setiap awal kata diubah menjadi huruf kapital menggunakan title().
3. Inisial dibuat dengan mengambil huruf pertama dari setiap kata pada nama, lalu menggabungkannya menjadi huruf kapital.
4. Kode kelas dibersihkan dari spasi berlebih, diubah menjadi huruf kapital menggunakan upper(), dan spasi antar kata diganti dengan tanda hubung menggunakan join().
5. Program menghitung jumlah kata pada nama lengkap menggunakan len() dan split().
6. Program menampilkan nama yang sudah dinormalisasi, kode kelas, inisial, dan jumlah kata ke terminal.

## Test Case

| No. | Input Nama | Input Kode Kelas | Hasil yang Diharapkan | Hasil Aktual | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | aan hendrayana | pmat a 2026 | Aan Hendrayana; PMAT-A-2026; AH | Aan Hendrayana; PMAT-A-2026; AH | Berhasil |
| 2 | fATHIYYAH mUTHMAINNAH | kelas b | Fathiyyah Muthmainnah; KELAS-B; FM | Fathiyyah Muthmainnah; KELAS-B; FM | Berhasil |
| 3 | BUDI | pmtk 01 | Budi; PMTK-01; B | Budi; PMTK-01; B | Berhasil |
| 4 | siti nur aisyah | kelas c | Siti Nur Aisyah; KELAS-C; SNA | Siti Nur Aisyah; KELAS-C; SNA | Berhasil |

## Refleksi

Salah satu masalah dalam pengolahan teks adalah penulisan nama yang memiliki spasi berlebih dan penggunaan huruf besar serta kecil yang tidak konsisten. Masalah ini dapat diperbaiki menggunakan strip(), split(), join(), dan title() untuk membersihkan spasi serta menyeragamkan penulisan nama. Dengan demikian, data menjadi lebih rapi dan mudah dibaca.
