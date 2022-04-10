import math

hrubaMzda = int(input("Zadej hrubou měsíční mzdu: "))
pocetDeti = int(input("Zadej počet dětí: "))

zprijmu = (hrubaMzda/100)*15
math.ceil(zprijmu)

socialni = (hrubaMzda/100)*6.5
math.ceil(socialni)

zdravotni = (hrubaMzda/100)*4.5
math.ceil(zdravotni)

match pocetDeti:
	case 1:
		slevaDeti = 0
	case 2:
		slevaDeti = 0
	case 3:
		slevaDeti = 0
	case 4:
		slevaDeti = 0


cistaMzda = hrubaMzda - zprijmu - socialni - zdravotni

print(int(math.ceil(cistaMzda)))