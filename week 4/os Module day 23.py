import os

print(os.getcwd())  # THis tells us the cwd (Current working Directory)

os.chdir('C:\\Users\TOSHIBA\pythonProject\Coding-Journey')  # This does ch-dir (Change Directory)
print(os.getcwd())

print('\n'.join(os.listdir('C:\\Users\TOSHIBA\pythonProject\Personal projects')))    # Lists all the file in directory

os.chdir('C:\\Users\TOSHIBA\pythonProject\Personal projects')
try:
    os.mkdir('Games Created')   # Creates a Single New folder
    os.makedirs('Games Created\\New Projects\\File To Be Deleted!')  # Creates Multiple Folder/ Make directories
except Exception as g:
    print('\n',g)


os.chdir('Games Created\\New Projects')
try:
    os.rename('Latest Projects', 'Renamed USing Python')
    print("Renaming File Successful")
except Exception as J:
    print('Renaming File Failed')

# print(os.environ.get('Path')) # This Can be done to get all the paths
paths = '\n'.join(os.environ.get('Path').split(';'))
print(paths)

print(os.path.join('C:\\', 'Geronimo books.txt'))   # Eliminates the need of slashes


print(os.path.exists('C:\\Users\TOSHIBA')) # A boolean variable will be given which checks if the path exists

print(os.path.isfile('C:\\Users\TOSHIBA'))   # A boolean variable will be given which checks if the File exists
print(os.path.isdir('C:\\Users\TOSHIBA'))   # if the Directory exists
