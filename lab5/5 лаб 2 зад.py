class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

circ = Circle(radius=50)
print(circ.get_radius())
circ.set_radius(60)
print(circ.get_radius())