import sys

file = "bakery.csv"
file_read = open(file, "r", encoding="utf-8")

name_exe_file, *argv = sys.argv
if len(argv) == 0:
    print(file_read.read())
elif len(argv) == 1:
    number_line = int(argv[0])
    for line in file_read.read().splitlines()[number_line-1:]:
        print(line)
elif len(argv) == 2:
    number_line_start = int(argv[0])
    number_line_stop = int(argv[1])
    for line in file_read.read().splitlines()[number_line_start-1:number_line_stop]:
        print(line)

else:
    print(f"Used: {sys.argv[0]} show all file")
    print(f"Used: {sys.argv[0]} NUMBER show start file from number line")
    print(f"Used: {sys.argv[0]} NUMBER NUMBER show start file from line to line")
    sys.exit()


