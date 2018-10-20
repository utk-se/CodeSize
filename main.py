import lizard
import argparse
import os


def parsearg():
    """
    Parses the arguments
    :return:
    """
    parser = argparse.ArgumentParser(description="CodeSize")
    parser.add_argument("-f")
    parser.add_argument("-d")
    parser.add_argument("--csv", action='store_true')
    return parser.parse_args()


def usageerror():
    """
    Returns an error to the user
    :return:
    """
    print("ERROR: (Make sure you only specify one)")
    print("     -f {file}")
    print("     -d {directory}")
    print("Exiting program...")


def printfiles(lfiles):
    """
    Prints the relevant contents of the files out
    :param lfiles:
    :return:
    """
    for lfile in lfiles:
        print("File: {}".format(lfile.filename))
        for func in lfile.function_list:
            print("     Function Name: {}".format(func.long_name))
            print("         Length: {}".format(func.length))
            print("         Start: {}".format(func.start_line))
            print("         Ends: {}".format(func.start_line + func.length - 1))


def printfilescsv(lfiles):
    """
    Prints the relevant contents of the file out in csv form
    :param lfiles:
    :return:
    """
    print("File, Function, Length")
    for lfile in lfiles:
        for func in lfile.function_list:
            print("{},\"{}\",{}".format(lfile.filename, func.long_name, func.length))


def main():
    args = parsearg()
    file = args.f
    directory = args.d
    csv = args.csv
    lfiles = []
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
        lfiles.append(lfile)

    # If it is a directory
    if directory is not None:
        for (root, subdir, files) in os.walk(directory):
            for file in files:
                fullpath = os.path.join(root, file)
                lfile = lizard.analyze_file(fullpath)
                lfiles.append(lfile)

    if csv is True:
        printfilescsv(lfiles)
    elif csv is False:
        printfiles(lfiles)


if __name__ == '__main__':
    main()
