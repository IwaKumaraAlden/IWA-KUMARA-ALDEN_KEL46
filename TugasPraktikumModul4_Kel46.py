"""
Kelompok 46

Anggota Kelompok :
    1. Sinatrio Seto Wahyudi - (21120126140163)
    2. Rafly Gunawan - (21120126140185)
    3. Lukman Fatihi Trisofa - (21120126140143)
    4. Iwa Kumara Alden - (21120126130062)
"""
import random

# ===================== DATA =====================
nama_menu = ["Indomie Telur", "Nasi Telur", "Kopi Susu"]
harga_menu = [8000, 9000, 6000]

nama_bahan = ["Indomie", "Telur", "Nasi", "Kopi"]
resep = [
    [1, 1, 0, 0],   # Indomie Telur
    [0, 1, 1, 0],   # Nasi Telur
    [0, 0, 0, 1],   # Kopi Susu
]

nama_pelanggan = ["Seto", "Lukman", "Rafly", "Alden"]


# ===================== FUNCTION =====================
# Function return tanpa parameter
def nama_acak():
    return random.choice(nama_pelanggan)


# Function return dengan parameter
def waktu_tunggu(jumlah_pesanan):
    return jumlah_pesanan * 3


# Function non-return tanpa parameter
def tampilkan_menu():
    print("\n=== MENU ===")
    for i in range(len(nama_menu)):
        print(i + 1, ".", nama_menu[i], "- Rp", harga_menu[i])


# Function non-return dengan parameter
def gelombang_pelanggan(warung):
    jumlah = random.randint(2, 4)
    print("\nGelombang pelanggan datang:", jumlah, "orang")
    for i in range(jumlah):
        menu = random.randint(0, len(nama_menu) - 1)
        warung.tambah_pesanan(nama_acak(), menu)


# ===================== CLASS & METHOD =====================
class Warung:
    def __init__(self):
        self.stok = [4, 4, 3, 3]
        self.antrean = []
        self.pendapatan = 0
        self.ditolak = 0

    # method return tanpa parameter
    def jumlah_antrean(self):
        return len(self.antrean)

    # method return dengan parameter
    def bahan_cukup(self, menu):
        for i in range(len(self.stok)):
            if self.stok[i] < resep[menu][i]:
                return False
        return True

    # method non-return dengan parameter
    def tambah_pesanan(self, nama, menu):
        self.antrean.append([nama, menu])
        print("Pesanan masuk:", nama, "->", nama_menu[menu])

    # method non-return tanpa parameter
    def tampilkan_stok(self):
        print("\n=== STOK BAHAN ===")
        for i in range(len(self.stok)):
            print(nama_bahan[i], ":", self.stok[i])

    # method non-return tanpa parameter
    def proses_antrean(self):
        if self.jumlah_antrean() == 0:
            print("Antrean kosong.")
            return
        print("\nEstimasi waktu tunggu:", waktu_tunggu(self.jumlah_antrean()), "menit")
        while self.jumlah_antrean() > 0:
            pesanan = self.antrean.pop(0)
            nama = pesanan[0]
            menu = pesanan[1]
            if self.bahan_cukup(menu):
                for i in range(len(self.stok)):
                    self.stok[i] -= resep[menu][i]
                self.pendapatan += harga_menu[menu]
                print("[OK]", nama, "-", nama_menu[menu], "selesai dimasak")
            else:
                self.ditolak += 1
                print("[DITOLAK]", nama, "-", nama_menu[menu], "(bahan habis)")

    # method non-return tanpa parameter
    def tampilkan_laporan(self):
        print("\n=== LAPORAN ===")
        print("Pendapatan:", self.pendapatan)
        print("Pesanan ditolak:", self.ditolak)


# ===================== PROGRAM UTAMA =====================
warung = Warung()
print("=== WARUNG BURJO TENGAH MALAM ===")
print(">>> KELOMPOK 46 <<<")

pilihan = -1
while pilihan != 0:
    print("\n1. Lihat menu")
    print("2. Lihat stok")
    print("3. Tambah pesanan")
    print("4. Gelombang pelanggan datang")
    print("5. Proses antrean")
    print("6. Laporan")
    print("0. Keluar")
    pilihan = int(input("Pilih: "))

    if pilihan == 1:
        tampilkan_menu()
    elif pilihan == 2:
        warung.tampilkan_stok()
    elif pilihan == 3:
        tampilkan_menu()
        nama = input("Nama pelanggan: ")
        nomor = int(input("Nomor menu: "))
        if nomor >= 1 and nomor <= len(nama_menu):
            warung.tambah_pesanan(nama, nomor - 1)
