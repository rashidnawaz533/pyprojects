class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, other):
        result = Vector(self.i+other.i, self.j+other.j, self.k+other.k)
        return result

    def __mul__(self, other):
        result = Vector(self.i*other.i, self.j*other.j, self.k*other.k)
        return result

    def __str__(self):
        return f"Vector {self.i}i + {self.j}j + {self.k}k"


v1 = Vector(1,2,3)
v2 = Vector(3,4,5)

print(v1 + v2)
print(v1*v2)