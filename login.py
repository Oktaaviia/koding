import csv
import os

def cetak_selamat_datang():
    print("=" * 40)
    print("Selamat datang di SmartBibit")
    print("=" * 40)

def registrasi():
    print("=== Registrasi ===")
    while True:
        nama = input('Masukkan nama anda: ').strip().lower() 
        password = input('Masukkan PIN (5 digit): ')
        if len(password) != 5 or not password.isdigit():
            print('PIN harus terdiri dari 5 digit angka.')
        else:
            with open('pengguna.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([nama, password, 'user'])
            print("Registrasi berhasil!")
            break

def login():
    print("=== Login ===")
    while True:
        nama = input('Masukkan nama anda: ').strip().lower()  
        password = input('Masukkan PIN: ')
       
        if not os.path.exists('pengguna.csv'):
            print("Anda belum melakukan registrasi. Silakan registrasi terlebih dahulu.")
            return None
        
        with open('pengguna.csv', 'r') as file:
            reader = csv.reader(file)
            ditemukan = False
            for row in reader:
                if row[0] == nama:
                    ditemukan = True  
                    if row[1] == password:
                        if nama == 'petani' and password == '24240':
                            print("Login admin berhasil!")
                            return 'admin'  
                        else:
                            print(f"Login berhasil! Selamat datang, {nama}.")
                            return 'user' 
                    else:
                        print("PIN salah. Silakan coba lagi.")
                        return None  
            
            if not ditemukan:
                print(f"Nama '{nama}' tidak ditemukan. Anda belum melakukan registrasi.")
                return None  
def main():
    cetak_selamat_datang()
    while True:
        print("\n=== Menu ===")
        print("1. Registrasi")
        print("2. Login")
        pilihan = input("Pilih menu (1/2): ")

        if pilihan == '1':
            registrasi()
        elif pilihan == '2':
            hasil_login = login()
            if hasil_login == 'user':
                print("Menu Pengguna belum ada hehe.")
            elif hasil_login == 'admin':
                print("Menu Admin belum ada hehe.")
            elif hasil_login is None:
                continue  
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()