def Somme(num):
	somme=0
	for i in range(num+1):
		somme += i
	return somme


choix=raw_input("Entre le nombre")
print Somme(int(choix))