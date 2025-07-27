def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    alphanum = {
        "alphabets": "A" "B" "C" "D" "E" "F" "G" "H" "I" "J" "K" "L" "M" "N" "O" "P" "Q" "R" "S" "T" "U" "V" "W" "X" "Y" "Z",
        "numbers": "0" "1" "2" "3" "4" "5" "6" "7" "8" "9",
        "special_char": " " "." "?" "/" "'" ";" ":" ">" "<" "," "!" "@" "#" "$" "%" "^" "&" "*" "(" ")" "_" "-" "=" "+" "[" "]" "{" "}",
    }
    alph = set(list(alphanum["alphabets"]))
    numb = set(list(alphanum["numbers"]))
    cond1 = set(list(s[0:2]))
    spec_char = set(list(alphanum["special_char"]))
    cond5 = set(s).intersection(spec_char)
    common_cond1 = alph.intersection(cond1)
    s = list(s)
    if len(common_cond1) == 2 and len(cond5) == 0:
         if len(s) > 1 and len(s) < 7 :
            k = set(s)
            cond4 = numb.intersection(k)
            if len(cond4) == 0:
                return True
            number = []
            position = []
            for i in range(len(s)):
                if s[i] in alphanum["numbers"]:
                    number += s[i]
                    position += str(i)
            if int(number[0]) == 0:
                return False
            cond3 = set(list(s[int(position[0]):len(s)]))
            common_cond3 = alph.intersection(cond3)
            if len(common_cond3) == 0:
                return True
         else:
              return False
    else:
        return False
if __name__ == "__main__":
    main()
