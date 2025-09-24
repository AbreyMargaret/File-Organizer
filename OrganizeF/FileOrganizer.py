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


def list_choose_file(folder_path):
        print()
        while True:
         print("==== FILES ====")
         files = os.listdir(folder_path)
         print("0.) Back ")
         for i, f in enumerate(files, start = 1):
                print(f"{i}.) {f}")
         choice = int(input("\nSelect file by number: "))
         
         if choice == 0:
                break
         chosen_file = files [choice - 1]
         file_path = os.path.join(folder_path, chosen_file)
         print(f"\nYou selected: {chosen_file} ")
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


def select_folder():
        while True:
                print("\n========= FILE ORGANIZER ==============")
                print("0.) Create folder")
                all_entries = os.listdir(directory_path) 
                
                for a, folders in enumerate(all_entries, start = 1):
                 print(f"{a}.) {folders}")
                

                enter = int(input("Select which folder: "))
                
                if enter == 0:
                  print("\nCreate new Folder")
                  new_file = (input("Name: "))
                  os.mkdir(os.path.join(directory_path, new_file))
                  print(f"{new_file} created successfully")
                
                else: 
                        chosen_folder = all_entries[enter - 1]
                        folder_path = os.path.join(directory_path, chosen_folder)
                        list_choose_file(folder_path)





select_folder()




       






        





