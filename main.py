import lizard
import argparse
import os
import re

class Width:
    def __init__(self, total_width, leadingwhitespace):
        self.total_width = total_width
        self.leadingwhitespace = leadingwhitespace

    total_width = 0
    leadingwhitespace = 0

def parsearg():
    """
    Parses the arguments
    :return:
    """
    parser = argparse.ArgumentParser(description="CodeSize")
    parser.add_argument("-f")
    parser.add_argument("-d")
    parser.add_argument('-l',
                        action='append')
    parser.add_argument("--csv",
                        action='store_true')
    return parser.parse_args()


def usageerror():
    """
    Returns an error to the user
    :return:
    """
    print("ERROR: (Make sure you only specify one)")
    print("     -f {file}")
    print("     -d {directory}")
    print("     -l {extension}")
    print("Exiting program...")


def printfiles(lfiles, widths):
    """
    Prints the relevant contents of the files out
    :param lfiles:
    :return:
    """
    i = 0
    for lfile in lfiles:
        print("File: {}".format(lfile.filename))
        for func in lfile.function_list:
            print("     Function Name: {}".format(func.long_name))
            print("         Length: {}".format(func.length))
            print("         Start: {}".format(func.start_line))
            print("         Ends: {}".format(func.start_line + func.length - 1))
            print("         Width: {}".format(widths[i].total_width))
            print("         Leading Whitespace: {}".format(widths[i].leadingwhitespace))
            i = i + 1


def printfilescsv(lfiles, widths):
    """
    Prints the relevant contents of the file out in csv form
    :param lfiles:
    :return:
    """
    i = 0
    print("File, Function, Total Width, Leading Whitespace (tabs / spaces)")
    for lfile in lfiles:
        for func in lfile.function_list:
            print("{},\"{}\",{}, {}".format(lfile.filename, 
											func.long_name,
											widths[i].total_width, 
											widths[i].leadingwhitespace))
            i = i + 1


def getmaximumwidth(lfiles):
    """
    Expects a list of files (as a lizard files) and will return the maximum width for each function
    :param lfiles:
    :return:
    """
    widths = []
    for lfile in lfiles:
        for func in lfile.function_list:
            width = Width
            file = open(lfile.filename, "r")
            for i, line in enumerate(file):
                # line.replace("\t", "    ")
                if func.start_line-2 < i < (func.start_line + func.length - 1):
                    if len(line) > width.total_width:
                        total_width = len(line)
                        leadingwhitespace = len(re.match(r"\s*", line).group())
                        width = Width(total_width, leadingwhitespace)
            widths.append(width)
    return widths



def main():
    args = parsearg()
    file = args.f
    directory = args.d
    csv = args.csv
    extensions = args.l
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
                if extensions:
                    for extension in extensions:
                        if extension in fullpath:
                            lfile = lizard.analyze_file(fullpath)
                            lfiles.append(lfile)
                else:
                    lfile = lizard.analyze_file(fullpath)
                    lfiles.append(lfile)

    widths = getmaximumwidth(lfiles)

    if csv is True:
        printfilescsv(lfiles, widths)
    elif csv is False:
        printfiles(lfiles, widths)


if __name__ == '__main__':
    main()
