from pathlib import Path
from zipfile import ZipFile

with ZipFile("files.zip", "w") as zip:
    for path in Path(r"D:\python\2020-year\ecommerce").rglob("*.*"):
        zip.write(path)

with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo(r"D:\python\2020-year\ecommerce\__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")

#with statement in user defined objects you only need to add the methods __enter__() and __exit__() in the object methods. 
