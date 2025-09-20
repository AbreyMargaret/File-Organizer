import os

directory_path = r"C:\Users\barce\python-projects\OrganizeF\Files"

all_entries = os.listdir(directory_path)

print("========= FILE ORGANIZER ==============")

a = 1

for folders in all_entries:
    print(f"{a}.) {folders}")
    a += 1

enter = int(input("Select which folder: "))

def select_folder(enter):
    if enter == 1:
            print("Documents:")
    elif enter == 2:
            print("Images:")
    elif enter == 3:
            print("PDF:")
    elif enter == 4:
            print("Python Projects:")



select_folder(enter)



        





