#!/usr/bin/python3
if __name__=="__main__":
    import sys

    add_total = 0
    for x in range(len(sys.argv) - 1):
       add_total = add_total + int(sys.argv[i + 1])
    print("{}".format(add_total))

