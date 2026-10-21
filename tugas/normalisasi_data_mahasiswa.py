def normalisasi_nama(nama):
    # Membersihkan spasi berlebih dan mengubah ke format title case
    nama_bersih = " ".join(nama.strip().split())
    return nama_bersih.title()

def buat_inisial(nama):
    # Mengambil huruf pertama dari setiap kata untuk membuat inisial
    kata = normalisasi_nama(nama).split()
    inisial = "".join([k[0] for k in kata])
    return inisial

def normalisasi_kode(kode):
    # Membersihkan spasi, mengubah ke uppercase, dan mengganti spasi dengan "-"
    kode_bersih = kode.strip().upper()
    return "-".join(kode_bersih.split())

# Input Data
nama_input = input("Nama: ")
kode_input = input("Kode kelas: ")

# Proses Normalisasi Data
nama_hasil = normalisasi_nama(nama_input)
kode_hasil = normalisasi_kode(kode_input)
jumlah_kata = len(nama_hasil.split())
inisial_hasil = buat_inisial(nama_input)

# Menampilkan Hasil Output
print(f"\nNama bersih : {nama_hasil}")
print(f"Kode kelas  : {kode_hasil}")
print(f"Jumlah kata : {jumlah_kata}")
print(f"Inisial     : {inisial_hasil}")