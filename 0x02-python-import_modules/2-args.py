#!/usr/bin/python3
if __name__=="__main__":
    import sys
    arg = sys.argv
    num_of_arguement = len(arg) - 1

    if num_of_arguement > 1:
        print("{}:arguements".format(num_of_arguement))
        for x in range(1, num_of_arguement + 1):
            print("{}: {}".format(x, arg[x]))

    elif num_of_arguement == 0:
        print("{} :arguments".format(num_of_arguement))

    else:
        print("{} argument:".format(size))
        print("{}: {}".format(size, arg[1]))

