punto = (3, 4)

punto = 3, 4 #tuple packing
x, y = punto #tuple unpacking
print(x, y)

set1 = set([1, 2, 3, 4, 5])
set2 = {4, 5, 6, 7, 8}
print(set1, set2)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.union(set2)) #da {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2)) #{4, 5}
print(set1.difference(set2)) #{1, 2, 3}
print(set1.symmetric_difference(set2)) #{1, 2, 3, 6, 7, 8}