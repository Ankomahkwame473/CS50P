question = input("What is the Answer to the Great question of Life, the Universe, and Everything? ").strip().lower()
if question == str(42):
    print("Yes")
elif question == "forty-two":
    print("Yes")
elif question == "forty two":
    print("Yes")
else:
    print("No")
