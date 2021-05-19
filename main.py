from compiler import main as compiler
from ide import main as ide
import os

while True:
    os.system("clear")
#    try:
    print("""

--------------------------------------------------------
 __  __   __         ____            _       ____ 
|  \ \ \_/ /        /  __|          | |     /  __|
|   | \   /   ___  |  /       /\    | |    |  /
|  /   | |   |___| | |       /__\   | |    | |
| |    | |         |  \__   / __ \  | |__  |  \__
|_|    |_|          \____| /_/  \_\ |____|  \____|

--------------------------------------------------------
[1] ide
[2] compile (kinda not) 

        """)
    x = int(input("[ENTER] enter choice: "))
    if x == 1:
        ide()
    else:
        print("[RUNNING]")
        compiler()
#    except KeyboardInterrupt:
#        print("[!]")
#        quit()
