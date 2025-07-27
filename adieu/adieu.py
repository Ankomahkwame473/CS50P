names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print("")
        if len(names) == 1:
            print(f"Adieu, adieu, to {names[0]}")
            break
        elif len(names) == 2:
            print(f"Adieu, adieu, to {names[0]} and {names[1]}")
            break
        elif len(names) > 1:
            for i in range(len(names)-1):
                names[i] = names[i] + ","
            names[len(names)-1] = "and " + names[len(names)-1]
            print(f"Adieu, adieu, to {" ".join(names)}")
            break
