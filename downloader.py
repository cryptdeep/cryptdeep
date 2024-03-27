import subprocess
from colorama import init, Fore, Back, Style
init()
import os
import time
os.system("cls||clear")

print(f"{Fore.CYAN}[/]{Style.RESET_ALL} Paket kontrolleri yapılıyor...")
time.sleep(0)
print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Paket kontrolleri yapıldı.")

tmsg = f"{Fore.GREEN}Basarılı{Style.RESET_ALL}"
fmsg = f"{Fore.RED}Başarısız{Style.RESET_ALL}"
omsg = f"{Fore.CYAN}İndiriliyor{Style.RESET_ALL}"
emsg = f"{Fore.RED}Hata{Style.RESET_ALL}"

def uline(new_text):
    # Terminaldeki son satırı silerek ve yeni metni yazarak güncelle
    print(f"\033[1A\033[K{new_text}", end="", flush=True)

download_type = "normal"
download_name = "tool"
download_location = "../"

def pkgleek(x):
	if x == "update":
		print(f" >>> Pakatler {Fore.CYAN}Güncelleniyor{Style.RESET_ALL}")
		cmd = f"apt update && apt upgrade -y"
		process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		output, error = process.communicate()
		
		if process.returncode == 0:  # İşlem başarılı ise
		    uline(f" >>> Paketler {Fore.GREEN}Güncellendi{Style.RESET_ALL}")
		elif process.returncode == 1:  # İşlem başarısız ise
		    uline(f" >>> Paketler Güncellenirken {Fore.RED}Hata Oluştu{Style.RESET_ALL}")
		else:  # Diğer durumlar için
		    uline(f" >>> Paketler Güncellenirken {Fore.RED}Hata Oluştu{Style.RESET_ALL}")
		print()
		
	else:
		print(f" > {x} {omsg}")
		cmd = f"apt install {x} -y"
		process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		output, error = process.communicate()
		
		if process.returncode == 0:  # İşlem başarılı ise
		    uline(f" > {x}: {tmsg}")
		elif process.returncode == 1:  # İşlem başarısız ise
		    uline(f" > {x}: {emsg}")
		else:  # Diğer durumlar için
		    uline(f" > {x}: {emsg}")
		print()
		
def pipleek(x):
	if x == "update":
		print(f" >>> pip sürümü {Fore.CYAN}Güncelleniyor{Style.RESET_ALL}")
		cmd = f"pkg upgrade python-pip"
		process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		output, error = process.communicate()
		
		if process.returncode == 0:  # İşlem başarılı ise
		    uline(f" >>> pip sürümü {Fore.GREEN}Güncellendi{Style.RESET_ALL}")
		elif process.returncode == 1:  # İşlem başarısız ise
		    uline(f" >>> pip sürümü Güncellenirken {Fore.RED}Hata Oluştu{Style.RESET_ALL}")
		else:  # Diğer durumlar için
		    uline(f" >>> pip sürümü Güncellenirken {Fore.RED}Hata Oluştu{Style.RESET_ALL}")
		print()
		
	else:
		print(f" > {x} {omsg}")
		cmd = f"pip install {x}"
		process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		output, error = process.communicate()
		
		if process.returncode == 0:  # İşlem başarılı ise
		    uline(f" > {x}: {tmsg}")
		elif process.returncode == 1:  # İşlem başarısız ise
		    uline(f" > {x}: {emsg}")
		else:  # Diğer durumlar için
		    uline(f" > {x}: {emsg}")
		print()

def toolleek(x):
	module_name = x.rsplit('/', 1)[-1]
	print(f" >>> {module_name} {omsg}")
	cmd = f"git clone {x}"
	process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, error = process.communicate()
	
	
	if process.returncode == 0:
		uline(f" >>> {module_name} {tmsg}")
		os.system(f"mv {module_name} {download_location}")
	elif process.returncode == 1:
		uline(f" >>> {module_name} {emsg}")
	else:  # Diğer durumlar için
		uline(f" >>> {module_name} {emsg}")
	print()
	
		

if download_name == "package":
	if download_type == "normal":
		with open("apt_normal.txt", "r") as file:
			for line in file:
				pkgleek(line.strip())
		pkgleek("update")
	
	elif download_type == "all":
		with open("apt_normal.txt", "r") as file:
			for line in file:
				pkgleek(line.strip())
		with open("apt_all.txt", "r") as file:
			for line in file:
				pkgleek(line.strip())

elif download_name == "pip":
	if download_type == "normal":
		pipleek("update")
		processc = subprocess.Popen("pip list", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		outputc = processc.communicate()
		outputc_str = outputc[0].decode()  # Demetin ilk öğesini seçip bayt nesnesini dizeye dönüştür
 
		with open("pip_normal.txt", "r") as file:
			for line in file:
				if f"{line.strip()}" in outputc_str:
					print(f" > {line.strip()}: {tmsg}")
				else:
					pipleek(line.strip())
					
elif download_name == "tool":
	if len(download_location) != 0:
		process = subprocess.Popen(f"cd {download_location}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		output, error = process.communicate()
		if process.returncode == 0:  # İşlem başarılı ise
		    pass
		elif process.returncode == 1:  # İşlem başarısız ise
		    print("belirtilen yol bulunamadı")
		else:  # Diğer durumlar için
		    print("belirtilen yol bulunamadı")
		print()

	else:
		pass

	with open("tool_normal.txt", "r") as file:
		for line in file:
			toolleek(line.strip())