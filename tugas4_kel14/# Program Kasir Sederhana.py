# Program Kasir Sederhana

class Kasir:
    def __init__(self):
        self.daftar_belanja = []
        self.total_harga = 0

    # METHOD non-return type (tanpa parameter)
    def tampilkan_menu(self):
        print("\n===== MENU TOKO =====")
        print("1. Nasi Goreng - Rp15000")
        print("2. Mie Ayam    - Rp12000")
        print("3. Es Teh      - Rp5000")
        print("4. Es Jeruk    - Rp7000")
        print("5. Selesai dan Hitung Total")

    # METHOD non-return type (dengan parameter)
    def tambah_item(self, nama, harga):
        self.daftar_belanja.append((nama, harga))
        self.total_harga += harga
        print(f"{nama} berhasil ditambahkan ke keranjang.")

# FUNCTION return type (tanpa parameter)
def input_menu():
    try:
        pilihan = int(input("\nPilih menu (1-5): "))
        return pilihan
    except ValueError:
        print("Input tidak valid. Masukkan angka 1-5.")
        return 0

# FUNCTION return type (dengan parameter)
def hitung_diskon(total):
    if total >= 50000:
        return total * 0.1  # diskon 10%
    elif total >= 30000:
        return total * 0.05  # diskon 5%
    else:
        return 0

# FUNCTION non-return type (tanpa parameter)
def sambutan():
    print("===== SELAMAT DATANG DI KASIR KELOMPOK 14 =====")

# FUNCTION non-return type (dengan parameter)
def cetak_struk(kasir):
    print("\n===== STRUK PEMBELIAN =====")
    for item, harga in kasir.daftar_belanja:
        print(f"{item:15} Rp{harga}")
    print("-----------------------------")
    print(f"Total Harga   : Rp{kasir.total_harga}")

    diskon = hitung_diskon(kasir.total_harga)
    print(f"Diskon        : Rp{diskon}")
    print(f"Total Bayar   : Rp{kasir.total_harga - diskon}")
    print("=============================")
    print("Terima kasih telah berbelanja!")

# PROGRAM UTAMA
def main():
    sambutan()
    kasir = Kasir()
    while True:
        kasir.tampilkan_menu()
        pilihan = input_menu()

        if pilihan == 1:
            kasir.tambah_item("Nasi Goreng", 15000)
        elif pilihan == 2:
            kasir.tambah_item("Mie Ayam", 12000)
        elif pilihan == 3:
            kasir.tambah_item("Es Teh", 5000)
        elif pilihan == 4:
            kasir.tambah_item("Es Jeruk", 7000)
        elif pilihan == 5:
            cetak_struk(kasir)
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# Jalankan program
main()
