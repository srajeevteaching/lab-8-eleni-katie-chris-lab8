# Chris, Kaite, ELeni
# CS-151
# 11/11/21
#Lab8

#take in list
#turn it into a string
#randomize it
#pop out name of student that is used
#continue if desired

import random
import sys

def load_name_list(fname):
    list = []
    file_name = open(fname ,"r")
    for line in file_name:
        list.append(line)
    file_name.close()
    return list

def pop_random_name(list1):
    if len(list1) > 0:
       return list1.pop(random.randrange(len(list1)))
    else:
        print("All out of names!")
        sys.exit()

def main():
    list1 = load_name_list("Lab8-names.txt")
    while True:
        print(pop_random_name(list1))
        if input("press [y] for another name ") == "y":
            continue
        break
main()