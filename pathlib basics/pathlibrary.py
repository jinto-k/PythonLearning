from pathlib import  Path

# Absolute path
# eg: on windows  c:\program Files\Microsoft
# eg: on mac  /user/local/bin

# Relative path

path = Path("ecommerce")
print(path.exists())

path1 = Path("email")
# path1.mkdir()  #  make directory
# path1.rmdir()   # remove directory


path2 = Path()  #  no arguments mean current directory

for file in path2.glob('*'):
    print(file)

# first parameter of glob is the files to be searched
# * means everything. *.* means all files of all types
# we can also specify like *.py or *.xls
# just glob('*') means look for directories
# glob gives a generator object as the return value, which is iterable
