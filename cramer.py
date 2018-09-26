while True:
	#valori dell'eq
	cx1 = int(input("inserire coeff di x (prima eq.)"))
	cy1 = int(input("inserire coeff di y (prima eq.)"))
	tn1 = int(input("inserire coeff noto (prima eq.)"))
	cx2 = int(input("inserire coeff di x (prima eq.)"))
	cy2 = int(input("inserire coeff di y (prima eq.)"))
	tn2 = int(input("inserire coeff noto (prima eq.)"))

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

#calcolo incognite
x = dx/d
print("X =", x)
y = dy/d
print("Y =", y)



