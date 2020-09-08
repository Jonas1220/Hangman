from os import system, name 
  
# define our clear function 
def clearConsole(): 
    # for windows 
    if name == 'nt': 
        x = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        x = system('clear') 
