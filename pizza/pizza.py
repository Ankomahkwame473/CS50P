import sys
import csv
from tabulate import tabulate
try:
    if len(sys.argv[0:]) == 2:
        if sys.argv[1].split(".")[1] != "csv":
            sys.exit("Not a csv file")
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for line in reader:
                header = line
                break
            print(tabulate(reader, header, tablefmt ="grid"))
    elif len(sys.argv[0:]) == 1:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")
except FileNotFoundError:
    sys.exit("File does not exist")
