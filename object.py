import math

def sphere(r):
    pi = math.pi
    vol = (4 * pi * r**3) / 3
    return vol

# r = float(input('Give me a radius: '))
# print('Vol of the sphere is ', sphere(r))

class Sphere:
    def __init__(self, r):
        self.r = r
    def vol(self):
        pi = math.pi
        vol = (4 * pi * self.r**3) / 3
        return vol
    def surface(self):
        surf = 4 * math.pi * self.r**2
        return surf






# end
