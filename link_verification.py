import os
                
def printAllTheValidPath(path_list):
    for path in path_list:
        if not os.path.isfile(path) and not os.path.isdir(path):
            print('This paths does not exist: ')
            print(path)
        elif os.path.isfile(path):
            pass
        else:
            for file_path in os.listdir(path):
                full_path = os.path.join(path, file_path)
                printAllTheValidPath(full_path)

def main():
    input_path_string = input("Enter the paths for the folders or the files: ")
    path_string = input_path_string.replace("\\", "\\\\")
    print(path_string)
    #if(len(printAllTheValidPath(path_string)) > 0):
    printAllTheValidPath(path_string)
    
if __name__ == "__main__":
    main()