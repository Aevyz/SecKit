import metadata
from os import system, name, path

files: list = []

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def rm_all(f):
    files = []


def pf(f):
    if len(files) == 0:
        print("No Files")
    else:
        for item in files:
            print(item)


def add(f):
    clear()
    while True:
        input_string = input("Add File. Empty Line To Return\n")
        if input_string == "":
            print("Returning")
            return
        if path.isfile(input_string):
            files.append(input_string)
        else:
            print("File Does Not Exist")


def phelp(f):
    for key, value in exec_dict.items():
        print(key + "\t\t" + value[1])
    print()


exec_dict = {
    "add": (add, "\t\tAdds Files"),
    "pf": (pf, "\t\tPrint Files"),
    "rm all": (rm_all, "\tRemove Files"),
    "md": (metadata.main, "\t\tMetadata"),
    "metadata": (metadata.main, "Metadata"),
    "help": (phelp, "\tHelp")
}

if __name__ == '__main__':

    in_str: str = ""
    while not (in_str == "exit" or in_str == "quit"):
        in_str = input("> ")
        if in_str == "":
            continue
        else:
            if exec_dict.__contains__(in_str):
                exec_dict.get(in_str)[0](files)
            else:
                print("Invalid Command")



