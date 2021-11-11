# Chris, Kaite, ELeni
# CS-151
# 11/11/21
#Lab8

#take in list
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
        print(line)
    file_name.close()
    return list

def pop_random_name(list1):
    student_name = random.randrange(list1)
    list1.pop(student_name)
    return student_name

def main():
    list1 = load_name_list("Lab8-names.txt")
    name = pop_random_name(list1)
    pop_random_name(list1)
    choice = input("Do you want to continue? ")
    choice.strip().lower()
    if choice == "yes":
        pop_random_name(list1)
    elif choice == "no":
        sys.exit()
    else:
        print("Invalid entry")


main()