greeting = input("Greeting: ").strip().lower()
if greeting[0:5] == "hello":
    print("$0")
elif greeting[0:5] != "hello" and greeting[0] == "h":
    print("$20")
else:
    print("$100")
