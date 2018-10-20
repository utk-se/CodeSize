import lizard
import lizard_ext
import argparse
import os

def parsearg():
    parser = argparse.ArgumentParser(description="CodeSize")
    parser.add_argument("-f")
    parser.add_argument("-d")
    return parser.parse_args()

def usageerror():
    print("ERROR: (Make sure you only specify one)")
    print("     -f {file}")
    print("     -d {directory}")
    print("Exiting program...")

def main():
    args = parsearg()
    file = args.f
    directory = args.d
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
        lfile = lizard.analyze_file(file)
        for func in lfile.function_list:
            print("Function Name: {}".format(func.long_name))
            print("Length: {}".format(func.length))

if __name__ == '__main__':
    main()