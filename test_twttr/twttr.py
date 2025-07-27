def main():
    shorten(input("Input: "))

def shorten(word):
    vowels = {"letters": "a" "e" "i" "o" "u" "A" "E" "I" "O" "U"}
    twitter_slang = []
    for i in range(len(word)):
        if word[i] in vowels["letters"]:
            twitter_slang += word[i]
            twitter_slang[i] = ""
        else:
            twitter_slang += word[i]
    return "".join(twitter_slang)


if __name__ == "__main__":
    main()
