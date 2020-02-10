#	Author: Heidi Sager
#	Due Date: 14 Nov. 2019
#	GISC9303 GIS Systems and Programming
#	Deliverable 2: Convert Decimal Degree to Degree Minute Second
#	------------------------------------------------------------------

#	Import libraries, I believe I ended up not needing "re" but left it just in case.
import re, math, decimal

#	Import to read the file with the data that will be manipulated, create the exporting file that will be written over with the data that is created (and that which came from the import file). 
in_file_name = r'd2RawListOfFarm.txt'
in_file_handler = open(in_file_name, 'r' ) 
out_file_name = r'sagerHResultNpFarm.txt'

#	Open the export file for writing.
out_file_handler = open(out_file_name, 'w', encoding='utf-8')

#	Remove the headers, move the script cursor one row downward.
in_file_handler.readline()

#	Create new headers on the export file.
out_file_handler.write('FarmID\tLongitude \tLatitude\tLong_d\tLong_m\tLong_s\tLat_D\tLat_M\tLat_S\n')

#	Double Check the headers look nice using a print statement (also helps for keeping track of columns after compiling and running in the terminal).
print('FarmID\tLongitude \tLatitude\tLong_d\tLong_m\tLong_s\tLat_D\tLat_M\tLat_S\n')


#	The for loop which will be manipulating the data row by row.
# 	x is the iterable variable, in_file_handler is the file imported.
for x in in_file_handler:

	#	I did have an .rstrip('\n') here but I tried running without and turns out the code still worked so I left it out since it wasn't really needed.

	#	Split the rows into separate columns by tab (\t).
	columns = x.split('\t')

	#	Make the first column (index = 0) of the data the "ID" column.
	id_all = columns[0]
	
	#	Make the second column (index = 1) of the data the "Easting" or "Longitude" column, I used "Decimal" to keep the trailing zeroes. I typically like "float", but it does not keep trailing zeros and for the sake of making the data look cohesive I wanted to keep them.
	easting = decimal.Decimal(columns[1]) ## Longitude or "Easting".
	
	#	Make the third column (index = 2) of the data the "Northing" or "Latitude" column. See above for use of "Decimal".
	northing =  decimal.Decimal(columns[2]) ## Latitude or "Northing".
	
	# --------------------------------------------------
	# Calculations for the longitude

	## Separating the longitude degrees from the minutes. This puts them in the form (min, deg) and can then be selected as needed for the following calculations
	easting_sep_deg_min = math.modf(easting) 

	# Degrees from Longitude, I needed to keep the negative for my if/else statement where I calculated the W/E directions.
	deg_long = int(easting_sep_deg_min[1])  

	# Degrees from Longitude without directional value (negative) - This is the variable I will be printing & exporting.
	deg_long_abs = "%02d" % (math.fabs(deg_long)) 
	
	# if/else to determine the directional component for degrees longitude, (East or West).
	if deg_long < 0:
		deg_direction_long = 'W'
	else: 
		deg_direction_long = 'E'

	# Minutes from Longitude with no decimal and including leading zeros, this is one that will be printed and exported.
	min_long = "%02d" % (int(math.fabs(easting_sep_deg_min[0] * 60))) 
	
	# Using modf to separate decimal from the degrees and multiply by 60 to get total minutes from longitude.
	long_min_to_get_sec = math.modf((easting_sep_deg_min[0]) * 60) 
	
	# Seconds from Longitude by multiplying the total minutes by 60 and formatted to 7 characters (decimal included) with 4 after the decimal (i.e. 00.0000). This looks nice when printed.
	sec_long = "%07.4f" % (math.fabs(round(long_min_to_get_sec[0] * 60, 4))) 

	# ---------------------------------------------------
	# Calculations for the latitude
	
	# Separating the latitude degrees from the minutes. This puts them in the form (min, deg) and can then be selected as needed for the following calculations.
	northing_sec_deg_min = math.modf(northing) 
	
	# Degrees from Latitude, I needed to keep the negative for my if/else statement where I calculated the N/S directions.
	deg_lat = int(math.fabs(northing_sec_deg_min[1])) 
	
	# Degrees from Latitude without directional value (negative) - This is the variable I will be printing & exporting.
	deg_lat_abs = "%02d" % (math.fabs(deg_lat)) 
	
	# if/else statements to determine the directional component for degrees latitude (North/South).
	if deg_lat < 0:
		deg_direction_lat = 'S'
	else:
		deg_direction_lat = 'N'

	# Minutes from Latitude with no decimal and including leading zeros, this is the one that will be printed and exported.
	min_lat = "%02d" % (int(math.fabs(northing_sec_deg_min[0] * 60))) 

	# Using modf to separate decimal from the degrees and multiply by 60 to get total minutes from latitude.
	lat_min_to_get_sec = math.modf(northing_sec_deg_min[0] * 60) 

	# Seconds from Latitude by multiplying the total minutes by 60 and formatted to 7 characters (decimal included) with 4 after the decimal (i.e. 00.0000). This looks nice when printed.
	sec_lat = "%07.4f" % (math.fabs( round(lat_min_to_get_sec[0] * 60, 4))) 

	# Resulting string of all the columns, tabs included.
	result = str(id_all) + '\t' + str(easting) + '\t' +  str(northing) + '\t' + str(deg_direction_long) + str(deg_long_abs) + '\t' + str(min_long) + '\t' + str(sec_long) + '\t' + str(deg_direction_lat) + str(deg_lat_abs) + '\t' + str(min_lat) + '\t' + str(sec_lat) + '\n' 
	
	# The export file that the result is written to.
	out_file_handler.write(result) 
	
	# Print to make sure the result is looking right.
	print(result)

# Close both files and end the code.
in_file_handler.close()
out_file_handler.close()