print("CALCOLO SISTEMI 2x2 E 3x3 CON IL METODO DI CRAMER")
print()
print("metodo: (a/b)")
print("2x2 (a)")
print("3x3 (b)")
m = input()

if m == "a":
	while True:
		#valori dell'eq
		cx1 = int(input("inserire coeff di x (prima eq.)"))
		cy1 = int(input("inserire coeff di y (prima eq.)"))
		tn1 = int(input("inserire coeff noto (prima eq.)"))
		cx2 = int(input("inserire coeff di x (seconda eq.)"))
		cy2 = int(input("inserire coeff di y (seconda eq.)"))
		tn2 = int(input("inserire coeff noto (seconda eq.)"))

		print()
		print("l'equazione è giusta? (s/n)")
		print(str(cx1) + "X" + " + " + str(cy1) + "Y" + " = " + str(tn1))
		print(str(cx2) + "X" + " + " + str(cy2)+ "Y" + " = " + str(tn2))
		a = input()
		if a == "s":
			break

	#calcolo determinanti
	dx = (tn1*cy2) - (cy1*tn2)
	dy = (cx1*tn2) - (tn1*cx2)
	d = (cx1*cy2) - (cy1*cx2)

	#calcolo incognite e stampa risultato
	print()
	print("--risultato--")
	x = dx/d
	print("X =", x)
	y = dy/d
	print("Y =", y)

else:
	while True:
		#valori dell'eq
		cx1 = int(input("inserire coeff di x (prima eq.)"))
		cy1 = int(input("inserire coeff di y (prima eq.)"))
		cz1 = int(input("inserire coeff di z (prima eq.)"))
		tn1 = int(input("inserire coeff noto (prima eq.)"))
		cx2 = int(input("inserire coeff di x (seconda eq.)"))
		cy2 = int(input("inserire coeff di y (seconda eq.)"))
		cz2 = int(input("inserire coeff di z (seconda eq.)"))
		tn2 = int(input("inserire coeff noto (seconda eq.)"))
		cx3 = int(input("inserire coeff di x (terza eq.)"))
		cy3 = int(input("inserire coeff di y (terza eq.)"))
		cz3 = int(input("inserire coeff di z (terza eq.)"))
		tn3 = int(input("inserire coeff noto (terza eq.)"))

		print()
		print("l'equazione è giusta? (s/n)")
		print(str(cx1) + "X" + " + " + str(cy1) + "Y" + " + " + str(cz1) + "Z" + " = " + str(tn1))
		print(str(cx2) + "X" + " + " + str(cy2) + "Y" + " + " + str(cz2) + "Z" + " = " + str(tn2))
		print(str(cx3) + "X" + " + " + str(cy3) + "Y" + " + " + str(cz3) + "Z" + " = " + str(tn3))

		a = input()
		if a == "s":
			break

	#calcolo determinanti
	dx = ((tn1*cy2*cz3) + (cy1*cz2*tn3) + (cz1*tn2*cy3)) - ((tn3*cy2*tn1) + (cy3*cz2*tn1) + (cz3*tn2*cy1))
	dy = ((cx1*tn2*cz3) + (tn1*cz2*cx3) + (cz1*cx2*tn3)) - ((cx3*tn2*cz1) + (tn3*cz2*cx1) + (cz3*cx2*tn1))
	dz = ((cx1*cy2*tn3) + (cy1*tn2*cx3) + (tn1*cx2*cy3)) - ((cx3*cy2*tn1) + (cy3*tn2*cx1) + (tn3*cx2*cy1))
	d = ((cx1*cy2*cz3) + (cy1*cz2*cx3) + (cz1*cx2*cy3)) - ((cx3*cy2*cz1) + (cy3*cz2*cx1) + (cz3*cx2*cy1))

	#calcolo incognite e stampa risultato
	print()
	print("--risultato--")
	x = dx/d
	print("X =", x)
	y = dy/d
	print("Y =", y)
	z = dz/d
	print("Z =", z)



