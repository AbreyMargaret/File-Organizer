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


def images():
        c = 1
        for images in all_images:
                   print(f"{c}.) {images}")
                   c += 1

def pdf():
        d = 1
        for pdf in all_pdf:
                   print(f"{d}.) {pdf}")
                   d += 1

def python_project():
        e = 1
        for pythonProject in all_pythonProjects:
                   print(f"{e}.) {pythonProject}")
                   e += 1
        


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
    elif enter == 3:
            print("\nPDF:")
            
    elif enter == 4:
            print("\nPython Projects:")
            

select_folder(enter)




       






        





