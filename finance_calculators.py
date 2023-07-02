
# imporing math to use .pow() method in compound calculation
# task isntruction push as to use .pow() I don't realy know what is
# benefit of using this method 
# in bond calculation we use "**" argument
import math
# I added loop to the task it's make code a bit more complicated 
# Loop to keep menu On when user give uncorrected answer
while True:	
	print("\ninvestment\t- to calculate the amount of interest you'll earn on "
			+"your investment\nbond\t\t- to calculate the amount you'll "
			+"have to pay on a home loan\nexit\t\t- to Exit\n\n")
	menu = input("Enter either 'investment' or 'bond' "
					+"from the menu above to proceed: ")
	# incase user Enter nothing, empty string will generate error 
	# in line 14 'menu = menu[0]  	
	if menu== "":
		continue
	menu = menu[0].lower()

	if menu == "i":
		amount = float(input('write amount of money: '))
		interest_rate =  float(input('write intrest_rate(1-100): '))/100
		years = int(input('write for how many years you wish to invest: '))
		interest = input('write "s" for simple or "c" for compound: ')
		# sub menu simple calculation
		if interest.lower() == 's':
			result_s = amount * (1 + interest_rate*years)
			result_s = round(result_s, 2) 
			print("\nAfter %s years you got back %s of " %(years, result_s)
					+ "your money")					
			# after calculation program ends			
			break
		# sub menu  compound calculation
		elif interest == 'c':			
			result_c = amount * math.pow((1 + interest_rate),years)
			result_c = round(result_c, 2)
			print(f"\nAfter {years} years you got back {result_c} of "
					+ "your money")
			break
		else:
			print("\nError")
	
	elif menu == "b":
		house_value = float(input('write value of the house: '))
		interest_rate = float(input('write intrest_rate(1-100): '))/1200
		months = float(input('write for how many months you want take loan: '))
		repayment = ((interest_rate * house_value)
						/ (1 - (1 + interest_rate)**(-months)))
		repayment = round(repayment, 2)
		print("\nYou have to pay %s for next %s months" %(repayment, int(months)))
		break
	
	elif menu == 'e':
		break
	else:
		print("\nError")