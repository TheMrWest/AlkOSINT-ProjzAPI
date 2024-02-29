from src.api import pjz
from src.template import alk
from colored import Fore, Back, Style

import sys
import json
import os

ow = pjz.OSINTProjz()
alk.return_py_art_code()

def create_path(name_file, info):
    osf = os.path.dirname(__file__)
    try:
        os.mkdir(osf + "/out")
    except FileExistsError:
        pass

    with open(osf + f"/out/{name_file}.json", 'w', encoding="utf-8") as cw:
        cw.write(info)

def return_info_object(x):
    info = ow.return_objectId(x)
    return info

if __name__ == "__main__":
    sys.argv.remove(sys.argv[0])
    if len(sys.argv) > 1:
        if "--object" == sys.argv[0]:
            if sys.argv[1].startswith("https://www.projz.com/"):
                infp = return_info_object(sys.argv[1])
                if infp != 0:
                    r_json = json.dumps(infp[1] ,ensure_ascii=False, indent=4)
                    print("---")
                    print(r_json)
                    if "--out" in sys.argv:
                        create_path(infp[0], r_json)
                else:
                    print("- " + Fore.white + Back.yellow + " Not Found." + Back.green + " Please, try again" + Style.reset)
            else:
                print("- " + Fore.white + Back.yellow + " Invalid Link." + Back.green + " Please, write the valid link " + Style.reset)
        else:
            print("- " + Back.yellow + " Invalid Param." + Back.red + " use:" + Back.cyan + " $ python main.py --object {link} " + Style.reset)
    else:
        print("- " + Back.yellow + " Invalid Param. Plase, read " + Back.red + "'README.md'" + Style.reset)
