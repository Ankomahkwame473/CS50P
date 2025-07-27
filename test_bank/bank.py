def main():
    value(input("Greeting: ").lower())


def value(greeting):
    if greeting[0:5] == "hello":
        return int(0)
    elif greeting[0:5] != "hello" and greeting[0] == "h":
        return int(20)
    else:
        return int(100)


if __name__ == "__main__":
    main()
