from pathlib import Path
from time import ctime
import shutil

path = Path(r"D:\python\2020-year\ecommerce\class-arritibutes.py")

# path.exists()
# path.rename()
# path.unlink() # remove file

print(ctime(path.stat().st_ctime))  # read human format

# print(path.read_text())  #read the test file
# path.write_text("...")
# path.write_bytes()
# note:  with open("__init__.py", "r") as file:

# if you want to copy file, this path object is not the ideal way

source = Path(r"D:\python\2020-year\ecommerce\class-arritibutes.py")
target = path() / "__init__.py"
target.write_text(source.read_test())

# easier method of copy file
shutil.copy(source, target)
