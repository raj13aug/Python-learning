from pathlib import Path

Path(r"c:\Program\Microsoft")  # window file system and r mean raw it will remove extra slash \\
Path("/usr/local")  # linux filesystem
Path()  # refer to current folder
Path("ecommerce/__init___.py")  # current folder and sub folder
# one path object combine it another string
Path() / "ecommerce" / "__init__.py"
Path.home()      # Home directory of the current user


path = Path("ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()
print(path.name)  # print file name
print(path.stem)  # print file name without extension
print(path.suffix)  # only file extension
print(path.parent)

# only change the name and the extension of the file.
path = path.with_name("file.txt")
print(path)
print(path.absolute)
path = path.with_suffix(".txt")  # display extenstion of file in directory
print(path.parent)
