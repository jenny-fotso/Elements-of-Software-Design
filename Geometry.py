#  File: Geometry.py

#  Description: developping several classes fundamental to geometry-
#               Point, Sphere, Cube, and Cylinder

#  Student Name: Jenny Fotso    

#  Student UT EID: 

#  Course Name: CS 313E

#  Unique Number: 52235

#  Date Created: 02/14/2021

#  Date Last Modified: 02/14/2021

import sys
import math

def read_p():
    #read in P coordinates
    coord_p = sys.stdin.readline()
    p_list = coord_p.split(' ')
    px = float(p_list[0])
    py = float(p_list[1])
    pz = float(p_list[2])
    #print('p: ', px, py, pz)
    return px, py, pz

    #read in Q coordinates
def read_q():
    coord_q = sys.stdin.readline()
    q_list = coord_q.split(' ')
    qx = float(q_list[0])
    qy = float(q_list[1])
    qz = float(q_list[2])
    #print('q: ', qx, qy, qz)
    return qx, qy, qz

    #read in center and radius of sphereA
def read_sphereA():
    info_sphereA = sys.stdin.readline()
    sphereA_list = info_sphereA.split(' ')
    sphereAx = float(sphereA_list[0])
    sphereAy = float(sphereA_list[1])
    sphereAz = float(sphereA_list[2])
    sphereAradius = float(sphereA_list[3])
    #print('sphereA: ', sphereAx, sphereAy, sphereAz, sphereAradius)
    return sphereAx, sphereAy, sphereAz, sphereAradius


    #read in center and radius of sphereB
def read_sphereB():
    info_sphereB = sys.stdin.readline()
    sphereB_list = info_sphereB.split(' ')
    sphereBx = float(sphereB_list[0])
    sphereBy = float(sphereB_list[1])
    sphereBz = float(sphereB_list[2])
    sphereBradius = float(sphereB_list[3])
    #print('sphereB: ', sphereBx, sphereBy, sphereBz, sphereBradius)
    return sphereBx, sphereBy, sphereBz, sphereBradius
    
    #read in center and side of cubeA
def read_cubeA():
    info_cubeA = sys.stdin.readline()
    cubeA_list = info_cubeA.split(' ')
    cubeAx = float(cubeA_list[0])
    cubeAy = float(cubeA_list[1])
    cubeAz = float(cubeA_list[2])
    cubeAside = float(cubeA_list[3])
    #print('cubeA: ', cubeAx, cubeAy, cubeAz, cubeAside)
    return cubeAx, cubeAy, cubeAz, cubeAside

    #read in center and side of cubeB
def read_cubeB():
    info_cubeB = sys.stdin.readline()
    cubeB_list = info_cubeB.split(' ')
    cubeBx = float(cubeB_list[0])
    cubeBy = float(cubeB_list[1])
    cubeBz = float(cubeB_list[2])
    cubeBside = float(cubeB_list[3])
    #print('cubeB: ', cubeBx, cubeBy, cubeBz, cubeBside)
    return cubeBx, cubeBy, cubeBz, cubeBside

    #read in the center, radius, height of cylA
def read_cylA():
    info_cylA = sys.stdin.readline()
    cylA_list = info_cylA.split(' ')
    cylAx = float(cylA_list[0])
    cylAy = float(cylA_list[1])
    cylAz = float(cylA_list[2])
    cylAradius = float(cylA_list[3])
    cylAheight = float(cylA_list[4])
    #print('cylA: ', cylAx, cylAy, cylAz, cylAradius, cylAheight)
    return cylAx, cylAy, cylAz, cylAradius, cylAheight

    #read in the center, radius, height of cylB
def read_cylB():
    info_cylB = sys.stdin.readline()
    cylB_list = info_cylB.split(' ')
    cylBx = float(cylB_list[0])
    cylBy = float(cylB_list[1])
    cylBz = float(cylB_list[2])
    cylBradius = float(cylB_list[3])
    cylBheight = float(cylB_list[4])
    #print('cylB: ', cylBx, cylBy, cylBz, cylBradius, cylBheight)
    return cylBx, cylBy, cylBz, cylBradius, cylBheight
    


class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
    self.x = x
    self.y = y
    self.z = z

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
    return '(' + str(x) +' ,' + str(y) + ' ,' + str(z) + ')'

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
    distance = math.sqrt(math.pow(other.x - self.x, 2) + math.pow(other.y - self.y, 2) + math.pow(other.z - self.z, 2)* 1.0)
    return distance

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
      tol = 1.0e-6
      return ((abs(self.x - other.x) < tol ) and abs(self.y - other.y) < tol and abs(self.z - other.z) < tol)

class Sphere (object):
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
        self.x = x
        self.y = y 
        self.z = z
        self.radius = radius
    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__ (self):
        return '(' + str(x) +' ,' + str(y) + ' ,' + str(z) + '), Radius: ' + str(radius)

    # compute surface area of Sphere
    # returns a floating point number
    def area (self):
        A = 4 * math.pi * math.pow(radius,2)
        A = float(A)
        return A

    # compute volume of a Sphere
    # returns a floating point number
    def volume (self):
        V = (4/3) * math.pi * math.pow(radius, 3)
        V = float(V)
        return V

    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point (self, p):
        print('p.x: ', p.x)
        p.x = float(p.x)
        return math.pow(p.x - self.x, 2 ) + math.pow( p.y - self.y, 2 ) + math.pow( p.y - self.y, 2 ) < math.pow(self.radius, 2)

    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, other):
        P = [self.x, self.y, self.z]
        Q = [other.x, other.y, other.z]
        distance = math.sqrt(math.pow(other.x - self.x, 2) + math.pow(other.y - self.y, 2) + math.pow(other.z - self.z, 2)* 1.0)
        return self.radius > distance + other.radius or other.radius > self.radius + distance

    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly 
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube (self, a_cube):
        center_to_vert = a_cube.side * math.sqrt(3)
        P = [self.x, self.y, self.z]
        Q = [a_cube.x, a_cube.y, a_cube.z]
        distance = math.sqrt(math.pow(a_cube.x - self.x, 2) + math.pow(a_cube.y - self.y, 2) + math.pow(a_cube.z - self.z, 2)* 1.0)
        return self.radius > distance + center_to_vert

    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl (self, a_cyl):
        P = [self.x, self.y, self.z]
        Q = [a_cyl.x, a_cyl.y, a_cyl.z]
        distance = math.sqrt(math.pow(a_cyl.x - self.x, 2) + math.pow(a_cyl.y - self.y, 2) + math.pow(a_cyl.z - self.z, 2)* 1.0)
        half_height = a_cyl.height/2
        return self.radius > (distance + a_cyl.radius) and (distance + half_height)

    # determine if another Sphere intersects this Sphere
    # other is a Sphere object
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean
    def does_intersect_sphere (self, other):
        P = [self.x, self.y, self.z]
        Q = [other.x, other.y, other.z]
        distance = math.sqrt(math.pow(other.x - self.x, 2) + math.pow(other.y - self.y, 2) + math.pow(other.z - self.z, 2)* 1.0)
        return self.radius + other.radius >= distance

    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # strictly inside or not strictly outside the other
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube (self, a_cube):
        center_to_vert = a_cube.side * math.sqrt(3)
        P = [self.x, self.y, self.z]
        Q = [a_cube.x, a_cube.y, a_cube.z]
        distance = math.sqrt(math.pow(a_cube.x - self.x, 2) + math.pow(a_cube.y - self.y, 2) + math.pow(a_cube.z - self.z, 2)* 1.0)
        return self.radius + center_to_vert >= distance

    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube (self):
        cube_side = (2*self.radius)/math.sqrt(2)
        cube_volume = math.pow(cube_side, 3)
        return cube_volume

class Cube (object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__ (self, x = 0, y = 0, z = 0, side = 1):
        self.x = x
        self.y = y 
        self.z = z
        self.side = side

    # string representation of a Cube of the form: 
    # Center: (x, y, z), Side: value
    def __str__ (self, x, y, z, side):
        return '(' + str(x) +' ,' + str(y) + ' ,' + str(z) + '), Side: ' + str(side)

    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area (self, side):
        A = 6 * math.pow(side, 2)
        A = float(A)
        return A

    # compute volume of a Cube
    # returns a floating point number
    def volume (self, side):
        V = math.pow(side, 3)
        V = float(V)
        return V

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point (self, x, y, z, p, side):
        x_min = self.x - (self.side/2)
        x_max = self.x + (self.side/2)
        y_min = self.y - (self.side/2)
        y_max = self.y + (self.side/2)
        z_min = self.z - (self.side/2)
        z_max = self.z + (self.side/2)
        return (x_min < p.x < x_max) and (y_min < p.y < y_max) and (z_min < p.z < z_max)
            

    # determine if a Sphere is strictly inside this Cube 
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        pass

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube (self, other):
        pass

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder (self, a_cyl):
        pass

    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube (self, other):
        pass

    # determine the volume of intersection if this Cube 
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume (self, other):
        pass

    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere (self):
        pass

class Cylinder (object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
        self.x = x
        self.y = y 
        self.z = z
        self.radius = radius
        self.height = height


    # returns a string representation of a Cylinder of the form: 
    # Center: (x, y, z), Radius: value, Height: value
    def __str__ (self, x, y, z, radius, height):
        return '(' + str(x) +' ,' + str(y) + ' ,' + str(z) + '), Radius ' + str(radius) + ', Height: ' + str(height)


    # compute surface area of Cylinder
    # returns a floating point number
    def area (self, radius, height):
        A = (2 * math.pi * radius * height) + (2 * math.pi * math.pow(radius, 2))
        A = float(A)
        return A

    # compute volume of a Cylinder
    # returns a floating point number
    def volume (self, radius, height):
        V = math.pi * math.pow(self.radius, 2) * self.height
        V = float(V)
        return V

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point (self, x, y, z, radius, height, p):
        x_min = self.x - (self.radius)
        x_max = self.x + (self.radius)
        y_min = self.y - (self.radius)
        y_max = self.y + (self.radius)
        z_min = self.z - (self.height/2)
        z_max = self.z + (self.height/2)
        return (x_min < p.x < x_max) and (y_min < p.y < y_max) and (z_min < p.z < z_max)


    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        pass

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube (self, a_cube):
        pass

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder (self, other):
        pass

    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
    def does_intersect_cylinder (self, other):
        pass

def main():
    # read data from standard input

    # read the coordinates of the first Point p
    px, py, pz = read_p()
    # create a Point object 
    p = Point(px, py, pz)

    # read the coordinates of the second Point q
    qx, qy, qz = read_q()
    # create a Point object
    q = Point(qx, qy, qz)

    # read the coordinates of the center and radius of sphereA
    sphereAx, sphereAy, sphereAz, sphereAradius = read_sphereA()
    # create a Sphere object
    sphereA = Sphere(sphereAx, sphereAy, sphereAz, sphereAradius)

    # read the coordinates of the center and radius of sphereB
    sphereBx, sphereBy, sphereBz, sphereBradius = read_sphereB()
    # create a Sphere object
    sphereB = Sphere(sphereBx, sphereBy, sphereBz, sphereBradius)

    # read the coordinates of the center and side of cubeA
    cubeAx, cubeAy, cubeAz, cubeAside = read_cubeA()
    # create a Cube object 
    cubeA = Cube(cubeAx, cubeAy, cubeAz, cubeAside)

    # read the coordinates of the center and side of cubeB
    cubeBx, cubeBy, cubeBz, cubeBside = read_cubeB()
    # create a Cube object 
    cubeB = Cube(cubeBx, cubeBy, cubeBz, cubeBside)

    # read the coordinates of the center, radius and height of cylA
    cylAx, cylAy, cylAz, cylAradius, cylAheight = read_cylA()
    # create a Cylinder object 
    cylA = Cylinder(cylAx, cylAy, cylAz, cylAradius, cylAheight)

    # read the coordinates of the center, radius and height of cylB
    cylBx, cylBy, cylBz, cylBradius, cylBheight = read_cylB()
    # create a Cylinder object
    cylB = Cylinder(cylBx, cylBy, cylBz, cylBradius, cylBheight)


    # print if the distance of p from the origin is greater 
    # than the distance of q from the origin
    p_dto = p.distance_to_origin()
    q_dto = q.distance_to_origin()
    if p_dto > q_dto:
        print('Distance of Point p from the origin is greater than the distance of Point q from the origin')
    else:
        print('Distance of Point p from the origin is not greater than the distance of Point q from the origin')


    # print if Point p is inside sphereA
    if sphereA.is_inside_point(p):
        word = 'is'
    else:
        word = 'is not' 
    print('Point p', word, 'inside sphereA')


    # print if sphereB is inside sphereA
    if sphereA.is_inside_sphere(sphereB):
        word = 'is'
    else:
        word = 'is not'
    print('sphereB', word, 'inside sphereA')


    # print if cubeA is inside sphereA
    if sphereA.is_inside_cube(cubeA):
        word = 'is'
    else:
        word = 'is not'
    print('cubeA', word, 'inside sphereA')


    # print if cylA is inside sphereA
    if sphereA.is_inside_cyl(cylA):
        word = 'is'
    else:
        word = 'is not'
    print('cylA', word, 'inside sphereA')


    # print if sphereA intersects with sphereB
    if sphereB.does_intersect_sphere(sphereA):
        word = 'does'
    else:
        word = 'does not'
    print('sphereA', word, 'intersect sphereB')


    # print if cubeB intersects with sphereB
    if sphereB.does_intersect_cube(cubeB):
        print('cubeB does intersect sphereB')
    else:
        print('cubeB does not intersect sphereB')
    

    # print if the volume of the largest Cube that is circumscribed 
    # by sphereA is greater than the volume of cylA
    cube_vol = sphereA.circumscribe_cube()
    cylA_vol = cylA.volume()
    #print(cube_vol)
    #print (cylA_vol)
    if cube_vol > cylA_vol:
        print('Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA')
    else:
        print('Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA')




    # print if Point p is inside cubeA
    if cubeA.is_inside_point(p):
        print('Point p is inside cubeA')
    else:
        print('Point p is not inside cubeA')

    # print if sphereA is inside cubeA
    if cubeA.is_inside_sphere(sphereA):
        print('sphereA is inside cubeA')
    else:
        print('sphereA is not inside cubeA')

    # print if cubeB is inside cubeA
    if cubeA.is_inside_cube(cubeB):
        print('cubeB is inside cubeA')
    else:
        print('cubeB is not inside cubeA')

    # print if cylA is inside cubeA
    if cubeA.is_inside_cyl(cylA):
        print('cylA (is inside cubeA')
    else:
        print('cylA is not inside cubeA')

    # print if cubeA intersects with cubeB
    if cubeB.does_intersect_cube(cubeA):
        print('cubeA does intersect cubeB')
    else:
        print('cubeA does not intersect cubeB')

    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA

    # print if the surface area of the largest Sphere object inscribed 
    # by cubeA is greater than the surface area of cylA




    # print if Point p is inside cylA
    if cylA.is_inside_point(p):
        print('Point p is inside cylA')
    else:
        print('Point p is not inside cylA')

    # print if sphereA is inside cylA
    if cylA.is_inside_sphere(sphereA):
      print('sphereA is inside cylA')
    else:
      print('sphereA is not inside cylA')

    # print if cubeA is inside cylA
    if cylA.is_inside_cube(cubeA):
      print('cubeA is inside cylA')
    else:
      print('cubeA is not inside cylA')

    # print if cylB is inside cylA
    if cylA.is_inside_cylinder(cylB):
      print('cylB is inside cylA')
    else:
      print('cylB is not inside cylA')

    # print if cylB intersects with cylA
    if cylA.does_intersect_cylinder(cylB):
      print('cylB does intersect cylA')
    else:
      print('cylB does not intersect cylA')

if __name__ == "__main__":
    main()
