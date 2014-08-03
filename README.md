csv_perimeter_calculator
===============
This simple program reads in a list of point coordinates from a CSV file and then prints
out the perimeter length of the polygon that is defined by tracing the points in the listed order.

The polygon defined by the provided points can be irregular and possibly self intersecting.

### Files:

- perimeter.py: python script
- test_perimeter.py: unit tests
- sample_data/*: Some sample input data CSV files
- run.sh: simple bash script to run through all the sample files

### Running tests

    $ python -m unittest test_perimeter

### Running instructions

make sure the python file is executable

	$ chmod +x ./perimeter.py

then

	$ ./perimeter.py ./sample_data/triangle.csv

or

    $ ./perimeter.py ./sample_data