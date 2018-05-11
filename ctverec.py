def ctverec(velikost, d="-", e="|", f="+"):
	
	vnitrek = e + " " * (velikost - 2) + e
	kraj = f + d *  (velikost - 2) + f

	print(kraj)
	for i in range(velikost - 2):
		print(vnitrek)
	print(kraj)

def lichy(n):
	return velikost % 2 == 1

def trojuhelnik(velikost, x='_', a="\\", b="/", c="V"):
	
	print(x * velikost)
	mezera = velikost - 4
	i = 1
	while mezera >= 0:
		print((" " * i) + a + (" " * mezera) + b)
		i = 1 + i 
		mezera = velikost - (2 + 2*i)

	if lichy(velikost):
		print((" " * i) + c)



def main ():
	povolene = ["a", "b"]
	tvar = input("Mam ti nakreslit ctverec (a) nebo trojuhelnik (b)?\n")
	if tvar not in povolene:
		print ("ty jsi ale voresprut!")
		return
	velikost = input("A jak velky?\n")
	velikost = int(velikost)
		

	if tvar == "a":
		print("ctverec")
		ctverec(velikost)
	elif tvar == "b":
		print("trojuhelnik")
		trojuhelnik(velikost)

	print("")

main()

