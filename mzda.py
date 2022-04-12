import math
from prettytable import PrettyTable

hrubaMzda = int(input("Zadej hrubou měsíční mzdu: "))
pocetDeti = int(input("Zadej počet dětí: "))

# Slevy
slevaPoplatnik = 2570

match pocetDeti:
	case 1:
		slevaDeti = 1267
	case 2:
		slevaDeti = 3127
	case 3:
		slevaDeti = 5447
	case default:
		slevaDeti = 5447
		for i in pocetDeti:
			slevaDeti =+ 2320
		print(slevaDeti)	

# Výpočet daně z příjmu
zprijmu = (round(hrubaMzda, -3)/100)*15
zprijmu = zprijmu - slevaDeti - slevaPoplatnik
math.ceil(zprijmu)

# Výpočet daně z sociálního pojištění
socialni = (hrubaMzda/100)*6.5
math.ceil(socialni)

# Výpočet daně z zdravotního pojištění
zdravotni = (hrubaMzda/100)*4.5
math.ceil(zdravotni)

# Výpočet
cistaMzda = hrubaMzda - zprijmu - socialni - zdravotni

# Zobrazení výsledku v tabulce
table = PrettyTable(["čistá mzda:", math.ceil(cistaMzda)])

table.add_row(["hrubá mzda:", hrubaMzda])
table.add_row(["daň:", math.ceil(zprijmu)])
table.add_row(["sociální pojištění:", math.ceil(socialni)])
table.add_row(["zdravotní pojištění:", math.ceil(zdravotni)])

print(table)
