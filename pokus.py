cesta = input("Ahoj, vítej v domě paní Láryfáry. Tumáš dej si pár vanilkových rohlíčků.\nTy jsi jistě přišel hledat poklad mého neboštíka manžela, viď? Sama nevím, kam ho ten starý pirát schoval, ale klidně to tu celé prošmejdi, já budu zatím v kuchyni.\nStojíš ve velké vstupní hale, vede z ní patero dveří a jedno starodávné schodiště.\nPrvní dveře (a) máš za zády, těmi jsi vešel, dvoje jsou nalevo (b, c), za jedměmi z nich právě mizí paní Láryfáry,\nčtvrté prochízejí protější stěnou (d) a poslední (e) jsou těsně vedle vchodu na schodiště (f).\n\nKudy se vydáš při hledání pokladu?\n"	)
bzum = ["a", "b", "d", "e", "f"]
if cesta in bzum:
	print("Už mě to nebaví..")
else:
	print (""Dáš si ještě rohlíček?"")
