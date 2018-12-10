import lizard
import argparse
import os


class Width:
    def __init__(self, total_width, leading_space, leading_tab):
        self.total_width = total_width
        self.leading_space = leading_space
        self.leading_tab = leading_tab

    total_width = 0
    leading_space = 0
    leading_tab = 0


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
            print("         Leading Space(s): {}".format(widths[i].leading_space))
            print("         Leading Tab(s): {}".format(widths[i].leading_tab))
            i = i + 1


def printfilescsv(lfiles, widths):
    """
    Prints the relevant contents of the file out in csv form
    :param lfiles:
    :return:
    """
    i = 0
    print("File, Function, Total Width, Leading Space(s), Leading Tabs")
    for lfile in lfiles:
        for func in lfile.function_list:
            print("{},\"{}\",{}, {}".format(lfile.filename,
                                            func.long_name,
                                            widths[i].total_width,
                                            widths[i].leading_space,
                                            widths[i].leading_tab))
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
                if func.start_line - 2 < i < (func.start_line + func.length - 1):
                    total_width = len(line)
                    if total_width > width.total_width:
                        # Get the leading whitespace width total
                        leading_length = total_width - len(line.lstrip())
                        # Now that we've got the leading length, get the beginning characters
                        line_beginning = line[:leading_length]
                        # Get the leading spaces and tabs
                        leading_space = line_beginning.count(' ')
                        leading_tab = line_beginning.count('\t')
                        width = Width(total_width, leading_space, leading_tab)
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
