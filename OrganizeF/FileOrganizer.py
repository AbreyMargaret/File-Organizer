import os

directory_path = r"C:\Users\barce\python-projects\OrganizeF\Files"
directory_docs = r"C:\Users\barce\python-projects\OrganizeF\Files\Docs"


all_entries = os.listdir(directory_path)
all_docs = os.listdir(directory_docs)

print("========= FILE ORGANIZER ==============")

a = 1


for folders in all_entries:
    print(f"{a}.) {folders}")
    a += 1

enter = int(input("Select which folder: "))

def select_folder(enter):
    b = 1
    if enter == 1:
            print("Documents:")
            for docs in all_docs:
                   print(f"{b}.) {docs}")
                   b =+ 1

    elif enter == 2:
            print("Images:")
    elif enter == 3:
            print("PDF:")
    elif enter == 4:
            print("Python Projects:")



select_folder(enter)





        





