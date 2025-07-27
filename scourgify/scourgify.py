import sys
import csv
try:
    if len(sys.argv[0:]) == 3:
        if sys.argv[1].split(".")[1] != "csv" and sys.argv[2].split(".")[2] != "csv":
            sys.exit("Not a csv file")
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            with open(sys.argv[2], "w") as after:
                after.write(f"first,last,house\n")
                for line in reader:
                    last,first = line["name"].split(",")
                    house = line["house"]
                    student = f"{first.strip()},{last},{house}"
                    after.write(f"{student}\n")
    elif len(sys.argv[0:]) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")
except FileNotFoundError:
    sys.exit("File does not exist")
