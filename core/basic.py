def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

##
def all_unique(lst):
        return len(lst) == len(set(lst))

def listFunction():
    x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
    y = [1, 2, 3, 4, 5]
    print(all_unique(x))
    print(all_unique(y))


    l = [9, 8, 6, 5]
    print(l[1:2]);