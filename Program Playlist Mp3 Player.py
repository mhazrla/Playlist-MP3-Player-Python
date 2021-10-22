# Muhammad Altaf Arya Amada // J0304201143
import os

class Node:
	def __init__(self, penyanyi = None, judul = None):
		self.penyanyi = penyanyi
		self.judul = judul
		self.next = None

class SLL:
	def __init__(self):
		self.head = None

	
	def anggota(self):
		print("\t     TUGAS PROYEK")
		print("\tMATA KULIAH STRUKTUR DATA")
		print("      PROGRAM STUDI TEKNIK KOMPUTER")
		print("\t  SEKOLAH VOKASI IPB")
		print("\n\n---------------------------------------------------------")
		print("|NO|NAMA ANGGOTA KELOMPOK\t|\t   NIM\t\t|")
		print("---------------------------------------------------------")
		print("|1.|Muhammad Hilmy Azkarillah\t|\tJ0304201054\t|")
		print("---------------------------------------------------------")
		print("|2.|Raihan Hafid Islamuddin\t|\tJ0304201068\t|")
		print("---------------------------------------------------------")
		print("|3.|Christina Sianturi\t\t|\tJ0304201076\t|")
		print("---------------------------------------------------------")
		print("|4.|Muhammad Altaf Arya Amada\t|\tJ0304201143\t|")
		print("---------------------------------------------------------")
		print("tekan [enter] untuk melanjutkan ")
		input()
		self.menu()
	
	def cetak(self):
		pos = self.head
		print("-----------------------------------------------------")
		print("|              Queue songs on Playlist              |")
		print("-----------------------------------------------------")
		print("|No.|      Nama Penyanyi       |     Judul Lagu     |")
		print("-----------------------------------------------------")
		n = 1
		# print("HEAD-->", end="", sep="")
		while pos != None:
			while n == 1:
					print("| %d |%-26s|%-20s|" %(n, pos.penyanyi.capitalize(), pos.judul.capitalize()), end="")
					print("<-- NOW PLAYING")
					print("-----------------------------------------------------")
					break
			while n > 1:
				print("| %d |%-26s|%-20s|" %(n, pos.penyanyi.capitalize(), pos.judul.capitalize()))
				print("-----------------------------------------------------")
				break
			n += 1
			pos = pos.next
			

		print("\ntekan [enter] untuk kembali ke halaman menu")
		input()
		self.menu()

# Christina Sianturi // J0304201076

	def tambahlagu(self, newpenyanyi, newjudul):
		newnode = Node(newpenyanyi, newjudul)
		print("Lagu : ", newpenyanyi," - ",newjudul, " ditambahkan ke playlist")
		if self.head == None:
			self.head = newnode
			self.tail = self.head		
		else:
			self.tail.next = newnode
			self.tail = newnode
			
		print("\ntekan [enter] untuk kembali ke halaman menu")
		input()
		self.menu()

	def cari(self, penyanyi, judul):
		current = self.head
		found = False
		while current and found is False:
			if current.penyanyi.capitalize() == penyanyi and current.judul.capitalize() == judul:
				found = True
			else:
				current = current.next
		return found
		
		print("\ntekan [enter] untuk kembali ke halaman menu")		
		input()
		self.menu() 
	
	def delx(self,x,y):
		if self.head == None:
			print("Playlist masih kosong")
			
		else:
			pos1 = self.head
			pos2 = self.head
			
			while pos1.next != None and pos1.penyanyi.capitalize() != x and pos1.judul.capitalize() != y:
				pos2 = pos1
				pos1 = pos1.next
			
			if pos1.penyanyi.capitalize() == x and pos1.judul.capitalize() == y: #Tanda ketemu
				#Ketika item di depan
				if pos1 == self.head:
					print("Lagu ", x, " - ", y, " telah dihapus dari playlist")
					self.head = self.head.next
				
				#Ketika item di belakang
				elif pos1.next == None:
					print("Lagu ", x, " - ", y, " telah dihapus dari playlist")
					pos2.next = None
				
				#Ketika item di tengah
				else:
					print("Lagu ", x, " - ", y, " telah dihapus dari playlist")
					pos2.next = pos1.next
			
			else:
				print("Lagu ", x, " - ", y, " tidak ada pada playlist")
				
		
		print("\ntekan [enter] untuk kembali ke halaman menu")
		input()
		self.menu()

# Raihan Hafid Islamuddin // J0304201068

	def banyaklagu(self):
		pos = self.head
		n = 0
		while pos != None:
			pos = pos.next
			n = n+1
		print("Jumlah lagu dalam playlist : ", n)
		print("\ntekan [enter] untuk kembali ke halaman menu")
		input()
		self.menu()

	def keluar(self):
		os.system("cls")
		print("Anda akan keluar program...")
		print("Terima kasih telah menggunakan aplikasi ini :)")

# Muhammad Hilmy Azkarillah // J0304201054
		
	def menu(self):
		os.system("cls")
		print("===============================")
		print("|  Mp3 Player Playlist Menu |")
		print("===============================")
		print("1. Menampilkan Playlist Lagu")
		print("2. Tambah Lagu")
		print("3. Cari Lagu")
		print("4. Hapus Lagu")
		print("5. Menghitung Banyaknya Lagu")
		print("6. Keluar dari Aplikasi Mp3 Player")
		print("===============================")
		pilih=str(input(("Silakan masukan pilihan anda: ")))	
		
		if(pilih=="1"):
			os.system("cls")
			print("=====================================================")
			print("|       Anda berada pada menu menampilkan lagu      |")   
			print("=====================================================\n")
			self.cetak()

		elif(pilih=="2"):
			os.system("cls")
			print("================================================")
			print("|    Anda berada pada menu menambahkan lagu    |")   
			print("================================================\n")
			a=input("Ingin menambah lagu? (Y/N):")
			os.system("cls")
			if a=="N":
				self.menu()
			else:
				print("==========================================")
				print("| Anda berada pada menu menambahkan lagu |")   
				print("==========================================\n")
				x = str(input("Masukkan nama penyanyi yang ingin ditambahkan: "))
				y = str(input("Masukkan judul lagu yang ingin ditambahkan: "))
				while x == "" or y == "":
					os.system("cls")
					print("Masukkan nama penyanyi dan judul lagu yang benar!")
					x = str(input("Masukkan nama penyanyi yang ingin ditambahkan: "))
					y = str(input("Masukkan judul lagu yang ingin ditambahkan: "))
				self.tambahlagu(x, y)

		elif(pilih=="3"):
			os.system("cls")
			print("==========================================")
			print("|   Anda berada pada menu mencari lagu   | ")   
			print("==========================================\n")
			a=input("Ingin mencari lagu? (Y/N):")
			os.system("cls")
			if a=="N":
				self.menu()
			else:
				current = self.head
				if current == None:
					print("Playlist masih kosong\n")
					print("tekan 'B' untuk kembali ke menu")
					x = str(input(""))
					while x == 'B':
						self.menu()
						return True
					while x != 'B':
						os.system("cls")
						print("Perintah tidak dikenal")
						print("Silahkan ulangi!\n")
						print("tekan 'B' untuk kembali ke menu")
						x = str(input(""))
					self.cari(x)
				else:
					print("Gunakan huruf kapital pada awal kalimat!\n")
					x = str(input("Nama penyanyi : "))
					y = str(input("Judul lagu : "))
					x.capitalize();y.capitalize()
					status = self.cari(x,y)
					if status == True:
						print("Lagu ditemukan pada playlist")
					else:                  
						print("Lagu tidak ditemukan pada playlist")
					
			print("\ntekan [enter] untuk kembali ke halaman menu")
			input()
			self.menu()


		elif(pilih=="4"):
			os.system("cls")
			print("==========================================")
			print("|  Anda berada pada menu menghapus lagu  |")   
			print("==========================================\n")
			if self.head != None:
				a=input("Ingin mencari lagu? (Y/N):")
				os.system("cls")
				if a=="N":
					self.menu()
				else:
					print("==========================================")
					print("|  Anda berada pada menu menghapus lagu  |")   
					print("==========================================")
					print("\nGunakan huruf kapital pada awal kalimat!\n")	
					x = str(input("Masukkan nama penyanyi yang ingin dihapus: "))
					y = str(input("Masukkan judul lagu yang ingin dihapus: "))
					x.capitalize();y.capitalize()
					self.delx(x,y)	
			else:
				print("Playlist masih kosong")
				print("\ntekan [enter] untuk kembali ke halaman menu")
				input()
				self.menu()
			
		elif(pilih=="5"):
			os.system("cls")
			print("==========================================")
			print("|   Anda berada pada menu jumlah lagu    |")   
			print("==========================================\n")			
			self.banyaklagu()
		
		elif(pilih=="6"):
			self.keluar()

			
if __name__ == "__main__":
    # execute only if run as a script
    l = SLL()
    l.anggota()
