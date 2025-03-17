# Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B))

# Find A intersection B
print(" ")
print(B.intersection(A))

# Is A subset of B
print(" ")
print(A.issubset(B))

# Are A and B disjoint sets
print(" ")
print(A.isdisjoint(B))

# Join A with B and B with A
print(" ")
print(A.union(B))
print(B.union(A))

# What is the symmetric difference between A and B
print(" ")
print(A.symmetric_difference(B))


# Delete the sets completely
print(" ")
del A, B
