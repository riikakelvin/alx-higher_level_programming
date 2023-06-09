#!/usr/bin/python3
if __name__=="__main__":
    import sys
    
    arg = sys.argv
    num = len(arg) - 1

    if num > 1:
        print("{} arguments:".format(num))
        for x in range(1, num + 1):
            print("{}: {}".format(x, arg[x]))

    elif num == 0:
        print("{} arguments.".format(num))

    else:
        print("{} argument:".format(num))
        print("{}: {}".format(num, arg[1]))
