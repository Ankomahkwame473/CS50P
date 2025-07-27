import sys
from PIL import Image
from PIL import ImageOps
try:
    if len(sys.argv[0:]) == 3:
        if sys.argv[1].split(".")[1] == "jpg" or sys.argv[1].split(".")[1] == "jpeg" or sys.argv[1].split(".")[1] == "png":
            if sys.argv[2].split(".")[1] == "jpg" or sys.argv[2].split(".")[1] == "jpeg" or sys.argv[2].split(".")[1] == "png":
                if sys.argv[1].split(".")[1] == sys.argv[2].split(".")[1]:
                    shirt = Image.open("shirt.png")
                    size = shirt.size
                    image = Image.open(sys.argv[1])
                    image = ImageOps.fit(image, size)
                    image.paste(shirt, mask = shirt)
                    image.save(sys.argv[2])
                else:
                    sys.exit("Input and output have different extensions")
            else:
                sys.exit("Invalid output")
        else:
            sys.exit("Invalid Input")
    elif len(sys.argv[0:]) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")
except FileNotFoundError:
    sys.exit("Input does not exist")
