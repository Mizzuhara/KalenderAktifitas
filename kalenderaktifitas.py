import datetime

class KalenderAktifitas:
    def __init__(self) :
        self.kalender = {}

    def tambah_aktifitas(self,tanggal,aktifitas):
        if tanggal in self.kalender:
            self.kalender[tanggal].append(aktifitas)
        else:
            self.kalender[tanggal] = [aktifitas]
        print(f"aktifitas '{aktifitas}' Di tambahkan Pada {tanggal}")

    def lihat_aktifitas(self,tanggal):
        if tanggal in self.kalender:
            print(f"Aktifitas Pada {tanggal} : ")
            for i,aktifitas in enumerate (self.kalender[tanggal], start=1):
                print(f"{i}. {aktifitas}")
        else:
            print(f"tidak ada aktifitas pada {tanggal}")
    
    def hapus_aktifitas(self,tanggal,nomor):
        if tanggal in self.kalender and 0 < nomor <= len(self.kalender[tanggal]):
            aktifitas = self.kalender[tanggal].pop(nomor-1)
            print(f"Aktifitas '{aktifitas}' Di hapus dari {tanggal}")
            if not self.kalender[tanggal]:
                del self.kalender[tanggal]
            else:
                print("Aktifitas Tidak Di temukan")
    
    def tampilkan_semua(self):
        if self.kalender:
            print("Daftar Semua Aktifitas :")
            for tanggal, aktifitas_list in sorted(self.kalender.items()):
                print(f"\ntanggal: {tanggal}")
                for i,aktifitas in enumerate(aktifitas_list,start=1):
                    print(f"{i}. {aktifitas}")
        else:
            print("Tidak Ada Aktifitas yang tercatat")

def validasi_tanggal(tanggal):
    try:
        datetime.datetime.strptime(tanggal, "%Y-%M-%d")
        return True
    except ValueError:
        return False
        
def main():
        app= KalenderAktifitas()
        while True:
            print("\nAplikasi kalender Aktifitas")
            print("1. tambah Aktifitas")
            print("2. Lihat Aktifitas Berdasarkan Tanggal")
            print("3. Hapus Aktifitas")
            print("4. Tampilkan Semua Aktifitas")
            print("5. keluar")
            pilihan = input("Pilihan menu (1-5) : ")

            if pilihan == "1":
                tanggal =input("Masukkan tanggal (YYYY-MM-DD) : ")
                if validasi_tanggal(tanggal):
                    aktifitas= input("masukkan Aktifitas : ")
                    app.tambah_aktifitas(tanggal,aktifitas)
                else:
                    print("format tanggal Tidak valid. gunakan Format YYYY-MM-DD.")
            
            elif pilihan =="2":
                tanggal = input("masukkan tanggal (YYYY-MM-DD) : ")
                if validasi_tanggal(tanggal):
                    app.lihat_aktifitas(tanggal)
                else:
                    print("Format Tanggal Tidak Valid ")
            elif pilihan == "3":
                tanggal= input("Masukkan tanggal (YYYY-MM-DD) :")
                if validasi_tanggal(tanggal):
                    app.lihat_aktifitas(tanggal)
                    try:
                        nomor = int(input("Pilih Nomor Aktifitas yang Ingin Di hapus : "))
                        app.hapus_aktifitas(tanggal,nomor)
                    except ValueError:
                        print("Input Nomor Tidak valid.")
                else:
                   print("format tanggal Tidak valid. gunakan Format YYYY-MM-DD.")
            elif pilihan == "4":
                app.tampilkan_semua()
            elif pilihan == "5":
                print("Terima kasih telah menggunakan program kalender Aktifitas.")
                break
            else:
                print("Pilihan Tidak Valid.Silahkan Coba Lagi.")

if __name__ == "__main__":
    main()   