### 60 ###
# writing files

# "w" - write
# "x" - exclusive creation
# "a" - append
# "b" - binary (image, video)
# "r" - read

text = "Hello World! :D"
file_path = "src/parts/output.txt" # use .expanduser() if u want the fp

try:
    with open(file_path, "w") as file:
        file.write(text)
        print(f"The file \"{file_path}\" was created.")

# handle error if using "x" instead of "w"
except FileExistsError:
    print("The file already exist.")