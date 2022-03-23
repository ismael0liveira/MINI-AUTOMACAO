import socket
import os
import time
import pyfiglet

banner = pyfiglet.figlet_format("RECON!!")
print(banner+"\n")
time.sleep(1)
print("By: Ismael Oliveira\n\n")


#Classe principal site:

class Site:
	def __init__(self, dominio):
		self.dominio=dominio

#aqui eu crio o meu objeto site que será considerado por geral
time.sleep(1)
site=Site(dominio=input("\033[32;1mDigite o dominio: \033[m"))

class Recon(Site):

	print("\033[33;1mO dominio e: \033[m"+site.dominio)

	#Aqui eu pego o IP do domínio:
	endereco = socket.gethostbyname(site.dominio)
	print("\033[33;1mO ip do site e: \033[m"+endereco)

	'''
	Aqui eu estou criando uma espécie de botão de liga e desliga que por padrão vem desativado,
	setado com o valor "nao", mas quando a pessoa seta o valor "sim" ele é ligado e cai na condição
	do if / else, quando tem o valor sim ele ativa a ferramenta, se não, não ativa.
	'''

	def recon(self, nmap="nao", findomain="nao", arjun="nao"):
		self.nmap=nmap

		#pegando ip novamente:

		endereco = socket.gethostbyname(site.dominio)
		#condição do NMAP:

		if self.nmap=="sim":
			time.sleep(2)
			print("\033[33;1m\n\nExecutando o Nmap...\033[m\n\n")
			time.sleep(2)
			os.system("nmap -p 21,22,25,53,80,110,123,143,443,465,631,993,995 "+endereco)
		else:
			pass

		#Condição do Findomain:

		self.findomain=findomain
		if self.findomain == "sim":
			time.sleep(2)
			print("\033[33;1m\n\nExecutando Findomain!\033[m\n\n")
			time.sleep(2)
			os.system("findomain --output -t "+site.dominio)
		else:
			pass

		#Condição do Arjun:
		self.arjun=arjun
		if self.arjun=="findomain":
			time.sleep(2)
			print("\033[33;1m\n\nATENÇÃO!! Eu também irei executar o HTTPROBE para resolver os subdominios!!\033[m\n")
			time.sleep(2)
			print("\033[33;1m\nExecutando httprobe...\033[m\n")
			time.sleep(2)
			os.system("cat "+str(site.dominio)+".txt"+" | httprobe > resolvidos.txt")
			time.sleep(2)
			print("\033[33;1mExecutando arjun...\033[m\n\n")
			time.sleep(2)
			os.system("arjun -i resolvidos.txt")
		else:
			pass
		if self.arjun=="dominio":
			time.sleep(2)
			print("\033[33;1m\n\nExecutando arjun...\033[m\n")
			time.sleep(2)
			os.system("arjun -u "+"https://"+str(site.dominio))
		else:
			pass

site=Recon(dominio=site.dominio)
site.recon(findomain=input("\033[32;1mDeseja executar o findomain? [sim/nao]: \033[m"), \
nmap=input("\033[32;1mDeseja executar o nmap? [sim/nao]: \033[m"), \
arjun=input("\033[32;1mDeseja executar o arjun? Arquivo do findomain: [findomain] / Dominio principal: [dominio] / Nao: [nao]: \033[m"))
