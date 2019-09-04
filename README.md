# Wintravel-Map
Generates travel time GIS maps.

It grabs data from multiple points in columns 2 and 3 from a CSV file called "center of mass.csv", converts them to longitude and latitude

The main file is getdata.py


Here's the format of the center of mass.csv
Col1 - PAUID (or the identifier used for shapefiles)
Col2 - MEAN_X, the x coordinate (in ESPG - 3347 format)
Col3 - MEAN_Y, the y coordinate (in ESPG - 3347 format)
Col4 after (Not actually used)

The outputs are as follows:


Current bug: The output files will output as results.txt, which is mass.csv, but with a new column at the end saying the differences between the two location in time.
