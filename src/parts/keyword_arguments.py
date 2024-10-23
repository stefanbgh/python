### 33 ###
# keyword arguments
# *args **kwargs

def ka(*args, **kwargs):
    print("--------------------------")

    for arg in args:
        print(arg)

    # print("------------------------")
    # for kwarg in kwargs.values():
    #     print(f"{kwarg}", end=" ")
    # print()

    print("--------------------------")
    print(f"{kwargs.get("first_name")} {kwargs.get("last_name")} {kwargs.get("dash")} {kwargs.get("version")}")
    print("--------------------------")

ka(3, 2, 1, "Wazzzzupppp!", first_name="Sponge", last_name="Bob", dash="-", version="Square Pants")