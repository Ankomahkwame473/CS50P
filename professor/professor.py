import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        tries = 0
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x+y

        while tries < 3:
            try:
                sum = input(f"{x} + {y} = ")
                if int(sum) == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1

            except ValueError:
                print("EEE")
                tries += 1
        if tries == 3:
            print(f"{x} + {y} = {answer}" )
            
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level > 0 and level <= 3:
                return level
            else:
                continue
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        num = random.randint(0,9)
    elif level == 2:
        num = random.randint(10,99)
    elif level == 3:
        num = random.randint(100,999)
    else:
        raise ValueError
    return num

if __name__ == "__main__":
    main()
