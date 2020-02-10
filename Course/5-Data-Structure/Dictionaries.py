# It's collection of key value pairs also immutable tupes
# both line is common
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)

# edit value

point["x"] = 10
print(point)

# add value
point["z"] = 20
print(point)

if "a" in point:
    print(point["a"])

# Get method

print(point.get("a"))   # the value doesn't existed, it showing as none value.
print(point.get("a", 0))

# delete

del point["x"]
print(point)


for key in point:
    print(key, point[key])


for x in point.items():
    print(x)

for key, value in point.items():
    print(key, value)
