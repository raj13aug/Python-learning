Make private of self.tags from the outside you need to preface it with 2 underlines.

print(cloud.__dict__)
print(cloud._TagCloud__tags)


The private members, these private members are still accessible from the outside.
