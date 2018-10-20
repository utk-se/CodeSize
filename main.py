import lizard
import argparse

def parsearg():
    parser = argparse.ArgumentParser(description="CodeSize")
    parser.add_argument("-f")
    parser.add_argument("-d")
    return parser



def main():
    print("Starting Program")
    args = parsearg()


if __name__ == '__main__':
    main()