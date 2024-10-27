### 61 ###
# reading files

import os

path = "~/Desktop/python/src/parts/output.txt" # or file_path = "src/parts/output.txt"
full_path = os.path.expanduser(path)

try:
    with open(full_path, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("The file was not found.")