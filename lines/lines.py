import sys

try:
    if len(sys.argv[0:]) == 2:
        if sys.argv[1].split(".")[1] != "py":
            sys.exit("Not a python file")
        count = 0
        with open("code.txt", "w") as code:
            code.write(open(sys.argv[1]).read())
        with open("code.txt", "r") as code:
            for line in code:
                line = line.strip()
                if line.startswith("#"):
                    #print(f"{line} {count} no count")
                    pass
                elif len(line) == 0:
                    #print(f"{line} {count} no count")
                    pass
                else:
                    count += 1
                    #print(f"{line} {count} count")
            print(count)
    elif len(sys.argv[0:]) == 1:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")
except FileNotFoundError:
    sys.exit("File does not exist")
