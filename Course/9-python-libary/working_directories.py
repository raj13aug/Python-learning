from pathlib import Path

path = Path(r"D:\python\2020-year\ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# We have a path object that represents a directory.

# A geneator object as the name implies returns a new value every time we iterate.

# when we are working with larger list of items, instead of storing all those items into memory, use generator object.

print(path.iterdir())

for p in path.iterdir():
    print(p)

# It show the dirctory and files under ecommerce

# List comprehension which petty similar

paths = [p for p in path.iterdir()]
print(paths)

# it display Posixpath object  --> linux,  windowpath object --> window

paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

# Note: drawback use comprehension, cannot search patten and don't search recursively and only achive this glob method.

paths.glob("*.py")

py_files = [p for p in paths.glob("*.py")]
print(py_files)

# rglob --> shot for recursive block

py_files = [p for p in paths.rglob("*.py")]
print(py_files)
