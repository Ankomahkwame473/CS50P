month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
while True:
    try:
        date = input("Date: ")
        a = str(int(date.split("/")[0]))
        b = str(int(date.split("/")[1]))
        c = str(int(date.split("/")[2]))
        if len(a) == 1:
            a = "0" + a
        if len(b) == 1:
            b = "0" + b
        if int(a) > 12 or int(b) > 31:
            continue
        print(f"{c}-{a}-{b}")
        break
    except ValueError:
        if "/" in date:
            continue
        date = date.split(" ")
        if "," not in date[1]:
            continue
        if date[0].isdigit():
            continue
        date[1] = date[1].replace(",","")
        if int(date[1]) > 31:
            continue
        if date[0] in month:
            a = str(month.index(date[0]) + 1)
            if len(a) == 1:
                a = "0" + a
            if len(date[1]) == 1:
                date[1] = "0" + date[1]
            print(f"{date[2]}-{a}-{date[1]}")
            break
        else:
            continue
