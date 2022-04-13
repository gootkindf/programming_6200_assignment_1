"""
File   : dynamic_protocol.py
History: 25-Sep-2021

Accepts the users input and instructs him or her on how to prepare a solution given
stock concentrations and desired final concentrations and volumes, all provided by
the user.

To Run:
python3 dynamic_protocol.py
"""

def main():
	"""accepts user input and gives instructions"""
	final_vol = float(input("Please enter the final volume of the solution (ml): ")) # input volume

	nacl_stock = float(input("Please enter the NaCl stock (mM): ")) # input NaCl concentrations
	nacl_final = float(input("Please enter the NaCl final (mM): "))

	step1 = f"Add {str(final_vol * (nacl_final / nacl_stock))} ml NaCl\n" # create step 1 instructions

	mg_stock = float(input("Please enter the MgCl2 stock (mM): ")) # input MgCl2 concentrations
	mg_final = float(input("Please enter the MgCl2 final (mM): "))

	step2 = f"Add {str(final_vol * (mg_final / mg_stock))} ml MgCl2\n" # create step 2 instructions

	step3 = f"Add water to a final volume of {str(final_vol)} ml and mix" # create step 3 instructions

	print(step1 + step2 + step3) # print all instructions

if __name__ == '__main__':
	main()
