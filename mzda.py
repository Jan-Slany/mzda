import math
from prettytable import PrettyTable

run = True

while run:
	try:
		hrubaMzda = int(input("Zadej hrubou měsíční mzdu: "))
		pocetDeti = int(input("Zadej počet dětí: "))
	except ValueError as e:
		print("Zadej čísla!")
	except NameError as e:
		print("101 error, Nejde nic!")
	except Exception as e:
		print(e)

	# Slevy
	slevaPoplatnik = 2570

	try:
		match pocetDeti:
			case 0:
				slevaDeti = 0
			case 1:
				slevaDeti = 1267
			case 2:
				slevaDeti = 3127
			case 3:
				slevaDeti = 5447
			case default:
				slevaDeti = 5447
				for i in range(pocetDeti - 3):
					slevaDeti += 2320	

	except NameError as e:
		print("Nebylo zadáno žádné dítě!")
	except Exception as e:
		print(e)

	# Výpočet daně z příjmu
	try:
		zprijmu = (round(hrubaMzda, -3)/100)*15
		zprijmu = zprijmu - slevaDeti - slevaPoplatnik
		math.ceil(zprijmu)

	except NameError as e:
		print("Nebyl zadán potřebný údaj!")
	except Exception as e:
		print(e)

	# Výpočet daně z sociálního pojištění
	try:
		socialni = (hrubaMzda/100)*6.5
		math.ceil(socialni)

	except NameError as e:
		print("Nebyl zadán potřebný údaj!")
	except Exception as e:
		print(e)

	# Výpočet daně z zdravotního pojištění
	try:
		zdravotni = (hrubaMzda/100)*4.5
		math.ceil(zdravotni)

	except NameError as e:
		print("Nebyl zadán potřebný údaj!")
	except Exception as e:
		print(e)

	# Výpočet
	try:
		cistaMzda = hrubaMzda - zprijmu - socialni - zdravotni

	except NameError as e:
		print("Nebyl zadán potřebný údaj!")
	except Exception as e:
		print(e)

	# Zobrazení výsledku v tabulce
	try:
		table = PrettyTable(["čistá mzda:", math.ceil(cistaMzda)])

		table.add_row(["hrubá mzda:", hrubaMzda])
		table.add_row(["daň:", math.ceil(zprijmu)])
		table.add_row(["sociální pojištění:", math.ceil(socialni)])
		table.add_row(["zdravotní pojištění:", math.ceil(zdravotni)])

		print(table)

	except NameError as e:
		print("Nebyl zadán potřebný údaj!")
	except Exception as e:
		print(e)

	again = input("Chceš počítat dál? ").lower()

	if again != "ano":
		run = False
	else:
		print("")
