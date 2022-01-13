import os
from re import I
#In this code you can insert paths of files of all types and folder
#After all path write '|' whitout space

#After entering the paths, and the words for the replacing, the paths that will change will be printed and if these paths are what you have chosen, send 'yes' 

#This function goes through all the existing files and prints them using the other function
def helpFunction(path_list, old_word, new_word):
    #if it is not a csv or json file
    path_string = path_list[0]
    if len(path_list) == 1 and not (path_string.endswith('.json') or path_string.endswith('.csv') or os.path.isdir(path_string)):
        print('No csv or json files in gives directory')
        #raise Exception('check directory')
    #if it is a single csv or json file 
    elif len(path_list) == 1 and os.path.isfile(path_string):
        getInToTheFile(path_string, old_word, new_word)
    #If it is several files, or folders or both
    elif len(path_list) > 1 or os.path.isdir(path_string):
        for path in path_list:
            if os.path.isfile(path) and not (path.endswith('.json') or path.endswith('.csv')):
                print('No csv or json files in gives directory')
                #raise Exception('check directory')
            elif path.endswith('.json') or path.endswith('.csv'):
                getInToTheFile(path, old_word, new_word)
            else:
                getInToTheFolder(path, old_word, new_word)
                
#This function reading the file, finding and replacing the words
def getInToTheFile(file_path, old_word, new_word):
    print("new file :\n", file_path)
    #read input file
    fin = open(file_path, 'r')
    #read file contents to string
    data = fin.read()
    print("data: \n" + data)
    #replace all occurrences of the required string
    data = data.replace(old_word, new_word)
    print("After replacing: \n" + data + '\n')
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open(file_path,'w')
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()

#This function find all the files in a folder    
def getInToTheFolder(path_folder, old_word, new_word):
    for path in os.listdir(path_folder):
        full_path = os.path.join(path_folder, path)
        if full_path.endswith('.json') or full_path.endswith('.csv'):
            getInToTheFile(full_path, old_word, new_word)
        elif os.path.isfile(full_path) and not (full_path.endswith('.json') or full_path.endswith('.csv')):
            pass
        else:
           getInToTheFolder(full_path, old_word, new_word)

#This function prints all the json and csv files we have selected
def printAllTheValidPath(path_list):
    for path in path_list:
        if os.path.isfile(path):
            if path.endswith('.json') or path.endswith('.csv'):
                print(path)
        else:
            for file_path in os.listdir(path):
                full_path = os.path.join(path, file_path)
                printAllTheValidPath(full_path)

def string_to_list(string):
    return string.split('|')






def main():
    input_path_string = input("Enter the paths for the folders or the files: ")
    path_string = input_path_string.replace("\\", "\\\\")
    print(path_string)
    old_word = input("Enter the word/s you want to replace: ")
    new_word = input("Enter the new word/s: ")
    print('Files to change: ')
    paths_list = string_to_list(path_string)
    printAllTheValidPath(paths_list)
    startToReplace = input('Are you sure you want to change this files? (yes or no) ')
    if(startToReplace == 'yes'):
        helpFunction(paths_list, old_word, new_word)
    
if __name__ == "__main__":
    main()