import os

directory_path = r"C:\Users\barce\python-projects\OrganizeF\Files"
directory_docs = r"C:\Users\barce\python-projects\OrganizeF\Files\Docs"
directory_images = r"C:\Users\barce\python-projects\OrganizeF\Files\Images"
directory_pdf = r"C:\Users\barce\python-projects\OrganizeF\Files\PDF"
directory_pythonProject = r"C:\Users\barce\python-projects\OrganizeF\Files\PythonProjects"


all_entries = os.listdir(directory_path)
all_docs = os.listdir(directory_docs)
all_images = os.listdir(directory_images)
all_pdf = os.listdir(directory_pdf)
all_pythonProjects = os.listdir(directory_pythonProject)


def documents():
       b = 1
       for docs in all_docs:
                   print(f"{b}.) {docs}")
                   b += 1
       enter_doc = input("Select Doc by number: ")
       menu_features(enter_doc)


def images():
        c = 1
        for images in all_images:
                   print(f"{c}.) {images}")
                   c += 1
        enter_images = input("Select images by number: ")
        menu_features(enter_images)

def pdf():
        d = 1
        for pdf in all_pdf:
                   print(f"{d}.) {pdf}")
                   d += 1
        enter_pdf = input("Select PDF by number: ")
        menu_features(enter_pdf)


def python_project():
        e = 1
        for pythonProject in all_pythonProjects:
                   print(f"{e}.) {pythonProject}")
                   e += 1
        enter_pythonProject = input("Select Python Folder by number: ")
        menu_features(enter_pythonProject)


def menu_features(input):
        print("(a)Read b(Copy) c(Move) d(Delete)")
        if input == 'a':
                read()
        elif input == 'b':
                copy()
        elif input == 'c':
                move()
        elif input == 'd':
                delete()



def read():
        print("Read")

def copy():
        print("Copy")

def move():
        print("Move")

def delete():
        print("Delete")


print("========= FILE ORGANIZER ==============")

a = 1

for folders in all_entries:
    print(f"{a}.) {folders}")
    a += 1

enter = int(input("Select which folder: "))

def select_folder(enter):
    if enter == 1:
            print("\nDocuments:")
            documents()
    elif enter == 2:
            print("\nImages:")
            images()
    elif enter == 3:
            print("\nPDF:")
            pdf()
            
    elif enter == 4:
            print("\nPython Projects:")
            python_project()
            

select_folder(enter)




       






        





