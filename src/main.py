from pystyle import Colorate, Colors
import sys

def cprint(*args, sep=' ', error=False, file=None, end='\n', flush=True):
    print(Colorate.Horizontal(Colors.blue_to_green, "[INFO]") if error is not True else Colorate.Horizontal(Colors.red_to_yellow, "[ERROR]"), *args, sep=sep, file=file, end=end, flush=flush)

def cinput(prompt: str, default=None):
    try:
        return input(f"{Colorate.Horizontal(Colors.yellow_to_green, '[INFO]')} {prompt}")
    except (EOFError, KeyboardInterrupt):
        return default
cprint("Hola")
cinput("Enter: ")