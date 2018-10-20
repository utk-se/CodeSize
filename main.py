import lizard
import argparse
import os

def parsearg():
    parser = argparse.ArgumentParser(description="CodeSize")
    parser.add_argument("-f")
    parser.add_argument("-d")
    parser.add_argument("--csv", action='store_true')
    return parser.parse_args()

def usageerror():
    print("ERROR: (Make sure you only specify one)")
    print("     -f {file}")
    print("     -d {directory}")
    print("Exiting program...")

def printfile(file):
    lfile = lizard.analyze_file(file)
    print("File: {}".format(file))
    for func in lfile.function_list:
        print("     Function Name: {}".format(func.long_name))
        print("     Length: {}".format(func.length))

def printfilecsv(file):
    lfile = lizard.analyze_file(file)
    for func in lfile.function_list:
        print("{},\"{}\",{}".format(file, func.long_name, func.length))


def main():
    args = parsearg()
    file = args.f
    directory = args.d
    csv = args.csv
    # If neither are specified
    if file is None and directory is None:
        usageerror()
        return
    # If both are specified
    if file is not None and directory is not None:
        usageerror()
        return

    # If it is a file
    if file is not None:
        if csv is True:
            print("File, Function, Length")
            printfilecsv(file)
        else:
            printfile(file)


    if directory is not None:
        for (root, subdir, files) in os.walk(directory):
            if csv is True:
                print("File, Function, Length")
            for file in files:
                fullpath = os.path.join(root, file)
                if csv is True:
                    printfilecsv(fullpath)
                else:
                    printfile(fullpath)

if __name__ == '__main__':
    main()