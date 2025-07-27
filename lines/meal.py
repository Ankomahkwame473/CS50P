def main():
    #me
    t = convert(input("What time is it? "))
    if t >= 7 and t <= 8:
        print("breakfast time")
    elif t >= 12 and t <= 13:
        print("lunch time")
    elif t >= 18 and t <= 19:
        print("dinner time")
    else:
        print("")


def convert(time):
    time = time.split(":")
    converted_time = int(time[0])+(int(time[1])/60)
    return round(converted_time, 2)

if __name__ == "__main__":
    main()
