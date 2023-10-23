#Lab 3
#Michaela Wojslaw
#GEOG 392
#Dr. Zhang
#October 22, 2023
#Parent Class to use for each shape identified in the text file
class a_shape():
    def __init__(self):
        pass
    def the_area(self):
        pass

#Child Classes for the shapes found in the text file (Circle, Triangle, and Rectangle)
#Circle Class
class circle(a_shape):
    def __init__(self, radius):
        super().__init__()
        self.radius= radius
    def the_area(self):
        return self.radius * self.radius * 3.14159
    
#Triangle Class
class triangle(a_shape):
    def __init__(self, the_base, height):
        super().__init__()
        self.the_base= the_base
        self.height= height
    def the_area(self):
        return self.the_base * self.height * 0.5

#Rectangle Class 
class rectangle(a_shape):
    def __init__(self, length, width):
        super().__init__()
        self.length= length
        self.width= width
    def the_area(self):
        return self.length * self.width
    
#Reading the text file
a_file= open(r'shape.txt.txt')
lines= a_file.readlines()
a_file.close()

#Creating the allshapes list
allshapes= [ ]
    
#Creating objects for each line in the text file and calculating the resulting area for each line/shape
for line in lines:
    components= line.split(',')
    a_shape= components [0]

    if a_shape == 'Circle':
        x = float (components[1])
        allshapes.append(circle(x))
    elif a_shape== 'Triangle':
        x = float (components[1])
        y = float (components[2])
        allshapes.append(triangle(x, y))
    elif a_shape== 'Rectangle':
        x = float (components[1])
        y = float (components[2])
        allshapes.append(rectangle(x, y))
    else:
        pass

for a_shape in allshapes:
    print(a_shape.the_area())