from pyfiglet import Figlet
import random
import sys
figlet = Figlet()
a = figlet.getFonts()
if len(sys.argv[0:]) == 1:
    f = random.choice(a)
    words = input("Input: ")
    figlet.setFont(font=f)
    print(figlet.renderText(words))
elif len(sys.argv[0:]) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in a:
    f = sys.argv[2]
    words = input("Input: ")
    figlet.setFont(font=f)
    print(figlet.renderText(words))
else:
    sys.exit("Invalid usage")
