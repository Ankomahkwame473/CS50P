import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um_sub = re.sub(r"[\w]+um[\w]+|[\w]+um|um[\w]+","",s.strip().lower())
    um_list = re.findall(r"um",um_sub)
    count = 0
    for _ in um_list:
        count += 1
    return count

if __name__ == "__main__":
    main()
