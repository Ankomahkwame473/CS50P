import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'<iframe (.+)?src="(https?://(www\.)?youtube\.com/embed/[a-zA-Z0-9]+)"(.+)?></iframe>', s.strip())
    if match:
        link = match.group(2)
        clean = re.sub(r"https?://(www\.)?youtube\.com/embed","https://youtu.be", link)
        return clean
    else:
        return


if __name__ == "__main__":
    main()
