while True:
    try:
        fraction = input("Fraction: ").strip().split("/")
        x = int(fraction[0])
        y = int(fraction[1])
        if x > y:
            pass
        else:
            percent = round(((x/y)*100))
            if percent <= 1:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                print(f"{percent}%")
            break
    except ValueError or ZeroDivisionError:
        pass
