import sys

file = "bakery.csv"

try:
    name_exe_file, number = sys.argv
except ValueError:
    print(f"Used: {sys.argv[0]} NUMBER")
    sys.exit()


file_to_write=open(file, 'a', encoding='utf-8')
file_to_write.write(f"{number}\n")
file_to_write.close()
