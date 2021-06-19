import math
class Circle1:
    def __init__(self, radius):
        self.radius = radius
    def circumference(self):
        return 2*math.pi*self.radius
    def are(self):
        self.area = math.pi*(self.radius**2)
        return self.area
    def __eq__(self, other):
        return self.radius == other.radius
    def __gt__(self, other):
        return self.radius > other.radius
rad1 = float(input('Enter the radius of Circle1 : '))
rad2 = float(input('Enter the radius of Circle2 : '))
c1 = Circle1(rad1)
c2 = Circle1(rad2)
print('The Circumference of Circle1 is : ', c1.circumference())
print('The Circumference of Circle2 is : ', c2.circumference())
print('The Area of Circle1 is : ', c1.are())
print('The Area of Circle2 is : ', c2.are())
print('C1 is equal to C2' if c1 == c2 else 'C1 is greater than C2' if c1 > c2 else 'C2 is greater than C1')
