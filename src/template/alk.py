import pyfiglet
import random
from colored import Fore, Back, Style

fonts = ["3-d","chunky","cosmike","kban"]

def return_py_art_code():
    font_r = random.choice(fonts)
    f = pyfiglet.figlet_format("ALk", font=font_r)
    print(Fore.cyan + f.strip() + Style.reset + "\n" + "- " + Fore.green + "Alkemist OSINT - - " + Fore.yellow + "Return Info ObjectID with projz API" + Style.reset)
