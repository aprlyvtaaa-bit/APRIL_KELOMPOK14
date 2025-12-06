import tkinter as tk
from tkinter import messagebox

# ===============================
# DATA ATM (VARIABLE & ARRAY)
# ===============================
saldo = 500000  # tipe data integer
riwayat = []    # array/list untuk menyimpan transaksi


# ===============================
# FUNCTION & METHOD
# ===============================
def update_riwayat(teks):
    """Menambah teks ke list riwayat"""
    riwayat.append(teks)


def cek_saldo():
    messagebox.showinfo("Saldo", f"Saldo Anda saat ini: Rp {saldo:,}")
    update_riwayat("Cek saldo")


def tarik_tunai():
    global saldo

    try:
        input_nilai = entry_jumlah.get().strip()
        
        # Hitung jumlah titik dalam input
        jumlah_titik = input_nilai.count('.')
        
        if jumlah_titik > 1:
            # Format 1.000.000 (titik sebagai pemisah ribuan) - hapus semua titik
            input_nilai = input_nilai.replace('.', '')
            jumlah = int(input_nilai)
        elif jumlah_titik == 1:
            # Cek apakah format 100.00 (desimal) atau 1000.0 (ribuan)
            parts = input_nilai.split('.')
            if len(parts[0]) <= 3 and len(parts[1]) <= 2:
                # Format 100.00 = 100 ribu
                jumlah = int(float(input_nilai) * 1000)
            else:
                # Format 1000.000 - hapus titik
                input_nilai = input_nilai.replace('.', '')
                jumlah = int(input_nilai)
        else:
            # Tidak ada titik, langsung convert
            jumlah = int(input_nilai)

        # Pengkondisian
        if jumlah <= 0:
            messagebox.showerror("Error", "Jumlah harus lebih dari 0!")
            return
        if jumlah > 10000000:
            messagebox.showerror("Error", "Jumlah maksimal Rp 10.000.000!")
            return
        if jumlah > saldo:
            messagebox.showerror("Error", "Saldo tidak cukup!")
            return

        saldo -= jumlah
        messagebox.showinfo("Berhasil", f"Anda menarik Rp {jumlah:,}\nSaldo tersisa: Rp {saldo:,}")
        update_riwayat(f"Tarik tunai: Rp {jumlah:,}")

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")


def setor_tunai():
    global saldo

    try:
        input_nilai = entry_jumlah.get().strip()
        
        # Hitung jumlah titik dalam input
        jumlah_titik = input_nilai.count('.')
        
        if jumlah_titik > 1:
            # Format 1.000.000 (titik sebagai pemisah ribuan) - hapus semua titik
            input_nilai = input_nilai.replace('.', '')
            jumlah = int(input_nilai)
        elif jumlah_titik == 1:
            # Cek apakah format 100.00 (desimal) atau 1000.0 (ribuan)
            parts = input_nilai.split('.')
            if len(parts[0]) <= 3 and len(parts[1]) <= 2:
                # Format 100.00 = 100 ribu
                jumlah = int(float(input_nilai) * 1000)
            else:
                # Format 1000.000 - hapus titik
                input_nilai = input_nilai.replace('.', '')
                jumlah = int(input_nilai)
        else:
            # Tidak ada titik, langsung convert
            jumlah = int(input_nilai)
            
        if jumlah <= 0:
            messagebox.showerror("Error", "Jumlah setor harus lebih dari 0!")
            return
        if jumlah > 10000000:
            messagebox.showerror("Error", "Jumlah maksimal Rp 10.000.000!")
            return

        saldo += jumlah
        messagebox.showinfo("Berhasil", f"Anda menyetor Rp {jumlah:,}\nSaldo sekarang: Rp {saldo:,}")
        update_riwayat(f"Setor tunai: Rp {jumlah:,}")

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")


def lihat_riwayat():
    if not riwayat:
        messagebox.showinfo("Riwayat", "Belum ada transaksi.")
        return

    # Perulangan untuk menyusun teks riwayat
    teks = ""
    for item in riwayat:
        teks += f"- {item}\n"

    messagebox.showinfo("Riwayat Transaksi", teks)


# ===============================
# GUI PROGRAMMING
# ===============================
root = tk.Tk()
root.title("Simulasi ATM")
root.geometry("350x350")

label_judul = tk.Label(root, text="SIMULASI ATM", font=("Arial", 16, "bold"))
label_judul.pack(pady=5)

label_kelompok = tk.Label(root, text="KELOMPOK 14", font=("Arial", 12, "bold"))
label_kelompok.pack(pady=5)

label_jumlah = tk.Label(root, text="Masukkan Jumlah:")
label_jumlah.pack()

entry_jumlah = tk.Entry(root, width=20)
entry_jumlah.pack(pady=5)

btn_cek = tk.Button(root, text="Cek Saldo", width=20, command=cek_saldo)
btn_cek.pack(pady=5)

btn_tarik = tk.Button(root, text="Tarik Tunai", width=20, command=tarik_tunai)
btn_tarik.pack(pady=5)

btn_setor = tk.Button(root, text="Setor Tunai", width=20, command=setor_tunai)
btn_setor.pack(pady=5)

btn_riwayat = tk.Button(root, text="Riwayat Transaksi", width=20, command=lihat_riwayat)
btn_riwayat.pack(pady=15)

root.mainloop()
