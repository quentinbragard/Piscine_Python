from vector import *
v1 = Vector([0, 1, 2, 3])
print(v1.__dict__)
print(type(v1.coordinates[0]))
print(v1.coordinates)

v2 = Vector(3)
print(v2.__dict__)
print(type(v2.coordinates[0]))
print(v2.coordinates)

v3 = Vector(0,3)
print(v2.__dict__)
print(type(v3.coordinates[0]))
print(v3.coordinates)


v1.__mul__(0)
print(v1.__dict__)
