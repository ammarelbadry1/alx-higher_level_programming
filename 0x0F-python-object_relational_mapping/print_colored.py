def printc(*args, **kwargs):
    print("\033[1;32m", end="")
    for arg in args:
        print("", arg, end="")
    print("\033[1;97m")
