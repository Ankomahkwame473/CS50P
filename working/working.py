import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time = re.search("^(([0-1])?[0-9])(:[0-5][0-9])? (AM|PM) to (([0-1])?[0-9])(:[0-5][0-9])? (PM|AM)$",s.strip())
    if time:
        if time.group(3) or time.group(7):
            if int(time.group(3).replace(":","")) >= 60 or int(time.group(7).replace(":","")) >= 60:
                raise ValueError
        if int(time.group(1)) <= 12 and int(time.group(1))> 0 and int(time.group(5)) <= 12 and int(time.group(5))> 0:
            if time.group(4) == "AM" and time.group(8) == "PM":
                convert_time = int(time.group(5)) + 12
                if convert_time == 24:
                    convert_time = str("00")
                    if time.group(3) and time.group(7):
                        return f"{convert_time}{time.group(7)} to {time.group(1)}{time.group(3)}"
                    elif time.group(3) and not time.group(7):
                        return f"{convert_time}:00 to {time.group(1)}{time.group(3)}"
                    elif time.group(7) and not time.group(3):
                        return f"{convert_time}{time.group(7)} to {time.group(1)}:00"
                    else:
                        return f"{convert_time}:00 to {time.group(1)}:00"
                if time.group(3) and time.group(7):
                    if len(time.group(1)) == 1:
                        return f"0{time.group(1)}{time.group(3)} to {convert_time}{time.group(7)}"
                    else:
                        return f"{time.group(1)}{time.group(3)} to {convert_time}{time.group(7)}"
                elif time.group(3) and not time.group(7):
                    if len(time.group(1)) == 1:
                        return f"0{time.group(1)}{time.group(3)} to {convert_time}:00"
                    else:
                        return f"{time.group(1)}{time.group(3)} to {convert_time}:00"
                elif time.group(7) and not time.group(3):
                    if len(time.group(1)) == 1:
                        return f"0{time.group(1)}:00 to {convert_time}{time.group(7)}"
                    else:
                        return f"{time.group(1)}:00 to {convert_time}{time.group(7)}"
                else:
                    if len(time.group(1)) == 1:
                        return f"0{time.group(1)}:00 to {convert_time}:00"
                    else:
                        return f"{time.group(1)}:00 to {convert_time}:00"
            elif time.group(4) == "PM" and time.group(8) == "AM":
                convert_time = int(time.group(1)) + 12
                if convert_time == 24:
                    convert_time = str("00")
                    if time.group(3) and time.group(7):
                        return f"{time.group(5)}{time.group(7)} to {convert_time}{time.group(3)}"
                    elif time.group(3) and not time.group(7):
                        return f"{time.group(5)}:00 to {convert_time}{time.group(3)}"
                    elif time.group(7) and not time.group(3):
                        return f"{time.group(5)}{time.group(7)} to {convert_time}:00"
                    else:
                        return f"{time.group(5)}:00 to {convert_time}:00"
                if time.group(3) and time.group(7):
                    if len(time.group(5)) == 1:
                        return f"{convert_time}{time.group(3)} to 0{time.group(5)}{time.group(7)}"
                    else:
                        return f"{convert_time}{time.group(3)} to {time.group(5)}{time.group(7)}"
                elif time.group(3) and not time.group(7):
                    if len(time.group(5)) == 1:
                        return f"{convert_time}{time.group(3)} to 0{time.group(5)}:00"
                    else:
                        return f"{convert_time}{time.group(3)} to {time.group(5)}:00"
                elif time.group(7) and not time.group(3):
                    if len(time.group(5)) == 1:
                        return f"{convert_time}:00 to 0{time.group(5)}{time.group(7)}"
                    else:
                        return f"{convert_time}:00 to {time.group(5)}{time.group(7)}"
                else:
                    if len(time.group(5)) == 1:
                        return f"{convert_time}:00 to 0{time.group(5)}:00"
                    else:
                        return f"{convert_time}:00 to {time.group(5)}:00"
        else:
            raise ValueError
    else:
        raise ValueError

if __name__ == "__main__":
    main()
