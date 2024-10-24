### 59 ###
# file detection

import os

path = "~/Desktop/python/src/parts/file_detection.py"

def fn(path):
    # if u want the fp
    return os.path.expanduser(path)

full_path = fn(path)

def check_path(full_path):
    if os.path.exists(full_path):
        return f"The location \"{full_path}\" exists."
    
    return "That location doesn't exist."

res = check_path(full_path)
print(res)