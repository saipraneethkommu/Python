# Different set operations

a = {1, 2, 3, 4, 5}
b = {4, 1, 6, 7, 8}

# Union
print(a | b)

# Intersection
print(a & b)

# Difference
print("Difference: A - B", a - b)
print("Difference: B - A", b - a)

# Symmetric difference
print(a ^ b)

# Subset
print(a.issubset(b))

# Superset
print(b.issuperset(a))

# Disjoint
print(a.isdisjoint(b))

# Adding elements

a.add(9)

print(a)

# Removing elements

a.remove(9)

print(a)

