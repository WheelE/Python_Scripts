import os

path = "C:\\Users\\Eric\\Desktop\\Test"

# The listdir() function will return a list of all the files and directories in
# directory stored in path, we'll loop through each of these setting name to 
# each file/directory
for name in os.listdir(path):

    # Build the path to the file or directory by concatenating the name to the
    # directory path
    file = path + "\\" +name 
    
    # The path.isfile() function will return true if the path we've constructed
    # above is a path for a file, otherwise it will return false.  If we have a
    # file, we delete it using the remove() function.
if os.path.isfile(file):
    print(os.path.isfile(file))
    os.remove(file)