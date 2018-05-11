def ctverec(velikost, x):
	radka = x + " " * (velikost - 2) + x
	print(x * velikost)
	print((radka + "\n") * (velikost - 3) + radka ) 
	print(x * velikost)

def lichy(n):
	return velikost % 2 == 1

def trojuhelnik(velikost, x):
	print(x * velikost)
	mezera = velikost - 4
	i = 1
	while mezera >= 0:
		print((" " * i) + x + (" " * mezera) + x)
		i = 1 + i 
		mezera = velikost - (2 + 2*i)

	if lichy(velikost):
		print((" " * i) + x)





tvar = input("Mam ti nakreslit ctverec (a) nebo trojuhelnik (b)?\n")
velikost = input("A jak velký?\n")
velikost = int(velikost)
x = "O"

if tvar == "a":
	print("ctverec")
	ctverec(velikost, x)
elif tvar == "b":
	print("trojuhelnik")
	trojuhelnik(velikost, x)
else:
	print ("ty jsi ale voresprut!")

print("")


