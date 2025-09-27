from tabulate import tabulate as t
from pyttsx3 import speak as sp
import os

ToDoList=[]

def addTask(task):

  ToDoList.append(task)

  print(f"\n{t([[task]],tablefmt="fancy_grid")} \nis Successfully added to the list at {len(ToDoList)} Position.")

  sp(f"{task} is Successfully added to the list at {len(ToDoList)} Position.")

def viewTasks():

  if not ToDoList:
    print("The ToDo List is Empty.")
    sp("The ToDo List is Empty")

  else:   
    print("Tasks in the list:")

    print(f"\n{t(enumerate(ToDoList, start=1),tablefmt="fancy_grid")}\n")
    sp(ToDoList)

def deleteTask(index):

  if 1 <= index <= len(ToDoList):
    deleted_task = ToDoList.pop(index - 1)

    print(f"\n{t([[deleted_task]],tablefmt="fancy_grid")} \nis Successfully deleted from {index} Position from the list.")
    sp(f"{deleted_task} is Successfully deleted from {index} Position from the list.")

  else:
    print("Invalid task index.")
    sp("The Given index is Invalid")

def readFile(fileName):
 try: 

  with open(f"D:/VS CODE Programs/INTERNSHIPS/CODING SAMURAI/assets/{fileName}.txt","r") as f:
   
   print(f"Opening {fileName} File.")
   sp(f"Opening {fileName} File.")

   content=f.read()
   print(f"\n{content}")

 except Exception as e:
   print("\nThe File is not Found")
   sp("\nThe File is not Found")

def saveFile(fileName):
 
  with open(f"D:/VS CODE Programs/INTERNSHIPS/CODING SAMURAI/assets/{fileName}.txt","w") as f: 

   for index,task in enumerate(ToDoList,start=1):
    f.write(f"{index} : {task}\n")

  print(f"Saving {fileName} File")
  sp(f"Saving {fileName} File")

  print(f"Your file is successfully saved as {fileName}")
  sp(f"Your file is successfully saved as {fileName}")

if __name__=="__main__":
 while True:
  print("\nOptions:")
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Delete Task")
  print("4. Save File (TXT)")
  print("5. Read File (TXT)")
  print("6. Delete File (TXT)")
  print("7. Exit")

  choice = input("\nEnter your choice (1 to 7): ")   

  if choice == "1":
    task = input("Enter the task: ")
    addTask(task)

  elif choice == "2":
    viewTasks()

  elif choice == "3":
    index = int(input("Enter the task index to delete: "))
    deleteTask(index)

  elif  choice=="4":
   fileName=input("Set Name to the File: ")
   saveFile(fileName)

  elif choice=="5" :
    fileName=input("Enter Name of the File: ")
    readFile(fileName)

  elif choice=="6":
   try: 

    fileName=input("Enter Name of the File: ")

    print(f"Deleting {fileName} File")
    sp(f"Deleting {fileName} File")

    os.remove(f"D:/VS CODE Programs/INTERNSHIPS/CODING SAMURAI/assets/{fileName}.txt")

    print(f"The {fileName} file is successfully deleted.")
    sp(f"The {fileName} file is successfully deleted.")

   except Exception as e:
     print(f"There is no File with {fileName}")  
     sp(f"There is no File with {fileName}")  

  elif choice == "7":
    print("Exiting...")
    sp("Exiting...")
    break

  else:
    print("Invalid choice. Please try again.")
    sp("Invalid choice. Please try again.")
    
