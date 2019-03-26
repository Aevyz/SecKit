import tika
from tika import parser
import sys


def main(files=sys.argv[1:]):
    tika.initVM()

    if len(files) == 0:
        print("Usage: metadata [Path To First File] ... [Path to Last File] [-c]\n-c:\t Content Flag")
        sys.exit(0)
    else:
        content: bool = "-c" in files
        if "-c" in files:
            files.remove("-c")
        print_metadata(files, content)


def longify(key, longest):
    if len(key) < longest:
        return longify(key + " ", longest)
    else:
        return key


def print_metadata(directory, content):
    try:
        parsed = parser.from_file(directory[0])
        longest: int = 0;
        for s in parsed["metadata"]:
            if len(s) > longest:
                longest = len(s)
        print("-----------------------------------------START METADATA----------------------------------------")
        for key, value in parsed["metadata"].items():
            print(longify(key, longest) + '\t' + str(value))
        print("------------------------------------------END METADATA-----------------------------------------\n")
        if content:
            print("-----------------------------------------START CONTENT-----------------------------------------")
            print(parsed["content"])
            print("------------------------------------------END CONTENT------------------------------------------\n\n")
    except FileNotFoundError:
        print("File \"%s\" not Found" % directory[0])

    if len(directory) > 1:
        print_metadata(directory[1:], content)


if __name__ == "__main__":
    main()
