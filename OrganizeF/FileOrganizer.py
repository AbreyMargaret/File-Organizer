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
       enter_doc = int(input("Select Doc by number: "))
       chosen_file = all_docs[enter_doc - 1]
       file_path = os.path.join(directory_docs, chosen_file)

       print(f"\nYou selected: {chosen_file}")
       feature_choice = input("(a) Read  (b) Copy  (c) Move  (d) Delete: ")

       menu_features(feature_choice,file_path)


def images():
        c = 1
        for images in all_images:
                   print(f"{c}.) {images}")
                   c += 1
        enter_images = int(input("Select images by number: "))
        chosen_file = all_images[enter_images - 1]
        file_path = os.path.join(directory_images, chosen_file)
        print(f"\nYou selected: {chosen_file}")
        feature_choice = input("(a) Read  (b) Copy  (c) Move  (d) Delete: ")
        menu_features(feature_choice,file_path)

def pdf():
        d = 1
        for pdf in all_pdf:
                   print(f"{d}.) {pdf}")
                   d += 1
        enter_pdf = int(input("Select PDF by number: "))
        chosen_file = all_pdf[enter_pdf - 1]
        file_path = os.path.join(directory_pdf, chosen_file)
        print(f"\nYou selected: {chosen_file}")
        feature_choice = input("(a) Read  (b) Copy  (c) Move  (d) Delete: ")
        menu_features(feature_choice, file_path)
        
        


def python_project():
        e = 1
        for pythonProject in all_pythonProjects:
                   print(f"{e}.) {pythonProject}")
                   e += 1
        enter_pythonProject = input("Select Python Folder by number: ")
        menu_features(enter_pythonProject)


def menu_features(input, file_path):
        if input == 'a':
                read(file_path)
        elif input == 'b':
                copy(file_path)
        elif input == 'c':
                move(file_path)
        elif input == 'd':
                delete(file_path)



def read(file_path):
         os.startfile(file_path)
        

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




       






        





