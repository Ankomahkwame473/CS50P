price = 0
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
while True:
    try:
        item = input("Item: ").lower().title().strip()
        if item in menu:
            price += float(menu[item])
            print(f"Total: ${price:.2f}")
        else:
            pass
    except EOFError:
        print("")
        break
