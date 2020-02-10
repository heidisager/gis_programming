#	Author: Heidi A. Sager
#	Due Date: 5 Dec. 2019
#	GISC9303 GIS Systems and Programming
#	Deliverable 3: Manipulate Street Address
#	------------------------------------------------------------------

#	Import libraries
import os
#	Import the reading file which is assumed to exist on the instructor's machine
in_file_name = r'./d3RawData/d3RawListOfFarm.txt'
#	Open the file for reading
in_file_handler = open(in_file_name, 'r' ) 
#	Skip the first line by moving script cursor down one line, since it is incorrect headings
skip_first_line = in_file_handler.readline()
#	Create a new file directory on the machine using the file naming convention for my name
new_path = 'c:/temp/sagerHD3ProcData/'
#	If the new file directory doesn't exist yet, make it. If it does, just use that file directory already created to save the newly written file
try:
	os.mkdir(new_path)
except OSError:
	new_path 
else:
	new_path
#	Create a new text file with the info to be written on it
out_file_name = r'c:/temp/sagerHD3ProcData/sagerHListOfFarm.txt'
#	Open that file up to be written on
out_file_handler = open(out_file_name, 'w')
#	Create top row with the new headers wanted for the fields that will be created from the full address
out_file_handler.write('FarmID \t Address \t StreetNum \t StreetName \t SufType \t Dir \t City\tProvince\tPostalCode\n')
#	Define the functions, my iterable variable is going to be each_row
def my_address_functions():
	#	for statement to use one record at a time, (going line-by-line)
	for each_row in in_file_handler:
		#	Split the columns first by the tab delimiter to get the FarmID and Address separate
		cols = each_row.split('\t')
		#	FarmID values are grabbed here
		farm_id = cols[0]
		#	Remove the \n at the end of the string for the total address and make the entire address its own variable
		address_total = cols[1].rstrip('\n')
		#	Split the address by commas to get the different parts
		cols_address = address_total.split(', ')
		#	make street_address_total only the street address (index = 0, entire first part)
		street_address_total = cols_address[0]
		#	Grab the city part of the address (index = 1, only the city is here)
		city_all = cols_address[1]
		#	I called region the last part with the province (index = 0) and postal code (index = 1)
		region = cols_address[2].split(' ')
		#	Make province column
		province = region[0]
		#	Make Postal Code column
		postal_code = ' '.join(region[1:])
		#	Need to create columns of the street address to get them sorted out below
		cols_street_address = street_address_total.split(' ')
		#	Make the StreetNum column (index =0)
		street_num = cols_street_address[0]
		#	Since the Street Number has been removed, we can make a new variable that doesn't have it here
		cols_street_address_no_number = cols_street_address[1:]
		#	Using an 'if' statement to see if the address has a direction component, and if it does to create a variable of the direction component
		if cols_street_address[-1] == 'N' or cols_street_address[-1] == 'S' or cols_street_address[-1] == 'E' or cols_street_address[-1] == 'W' or cols_street_address[-1] == 'SW' or cols_street_address[-1] == 'NW' or cols_street_address[-1] == 'NE' or cols_street_address[-1] == 'SE':
			#	Create the variable that the direction component will become
			directional = cols_street_address[-1]
			#	If it does have a direction component, make a variable that removes it from the rest of the address
			street_name = cols_street_address_no_number[:-1]
		#	If it doesn't have a direction component, some variables need to be changed
		else:
			#	If no directional component, then the direction is blank in the output
			directional = ' '
			#	If no direction component, then the last index will be the SufType
			suf_type = cols_street_address_no_number[-1]
			#	Once the last parts (directional component and SufType) have been removed, then join the rest of the address parts to create only the street name since it's left over
			street_name_only = ' '.join(cols_street_address_no_number[:-1])
		#	Write the results in the newly created file
		out_file_handler.write(farm_id + '\t' + str(address_total) + '\t' +  street_num + '\t' + street_name_only + '\t' + suf_type + '\t' + directional + '\t' + city_all + '\t' + province + '\t' + postal_code + '\n') 
# The defined function and its input from up above (with first row of input file removed)
my_address_functions()
#	Close both of the opened files
in_file_handler.close()
out_file_handler.close()