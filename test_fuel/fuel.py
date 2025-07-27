import sys
def main():
    print(gauge(convert(input("Fraction: ").strip())))

def convert(fraction):
    fraction = fraction.split("/")
    try:
        x = int(fraction[0])
    except ValueError:
        raise ValueError
    try:
        y = int(fraction[1])
    except ValueError:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    if x < 0 or y < 0:
        raise ValueError
    return round(((x/y)*100))
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return"F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
