from math import (radians, sin, cos)

###
# this class represents a straight piece of wire
#
class Wire(object):

    ###
    # instance method
    #
    # @param length - length of wire
    # @param diameter - diameter of wire
    #
    def __init__(self, length, diameter):
        # store attributes
        self._length = length
        self._diameter = diameter

        # init other attributes to None, so they must be set later
        self._p1 = (None, None, None)
        self._p2 = (None, None, None)


    ###
    # rotate a point around the x,y,z axis
    #
    # @param p - the point to rotate, a 3 element tuple of (x,y,z)
    # @param angles - a 3 element tuple of the amount to rotate in degrees around the x, y, and z axis
    # @returns - the rotated point
    #
    def _rotate_point(self, p, angles):
        
        # rotate point about x axis
        newp = self._rotate_x(p, angles[0])

        # rotate point about y axis
        newp = self._rotate_y(newp, angles[1])

        # rotate point about z axis
        newp = self._rotate_z(newp, angles[2])

        return newp

    
    ###
    # rotate a point around the x axis
    #
    # @param p - the point
    # @param theta - the amount to rotate
    # @returns - the new point
    #
    def _rotate_x(self, p, theta):

        # compute sin(theta) and cos(theta)
        sin_t = sin(radians(theta))
        cos_t = cos(radians(theta))

        # multiply point by rotation matrix
        return self._multiply_matrix(p, (1, 0, 0, 0, cos_t, -sin_t, 0, sin_t, cos_t))

    
    ###
    # rotate a point around the y axis
    #
    # @param p - the point
    # @param theta - the amount to rotate
    # @returns - the new point
    #
    def _rotate_y(self, p, theta):

        # compute sin(theta) and cos(theta)
        sin_t = sin(radians(theta))
        cos_t = cos(radians(theta))

        # multiply point by rotation matrix
        return self._multiply_matrix(p, (cos_t, 0, sin_t, 0, 1, 0, -sin_t, 0, cos_t))

    
    ###
    # rotate a point around the z axis
    #
    # @param p - the point
    # @param theta - the amount to rotate
    # @returns - the new point
    #
    def _rotate_z(self, p, theta):

        # compute sin(theta) and cos(theta)
        sin_t = sin(radians(theta))
        cos_t = cos(radians(theta))

        # multiply point by rotation matrix
        return self._multiply_matrix(p, (cos_t, -sin_t, 0, sin_t, cos_t, 0, 0, 0, 1))

    
    ###
    # multiple a point by a matrix
    #
    # @param p - the 3 element tuple (x, y, z) point to multiply
    # @param m - the 9 element tuple (a,b,c,d,e,f,g,h,i) representing the 3x3 matrix [ a b c ; d e f ; g h i ]
    # @returns - the new point
    def _multiply_matrix(self, p, m):

        # get x,y,z from p
        (x, y, z) = p

        # get (a, b, c, d, e, f, g, h, i) from m
        (a, b, c, d, e, f, g, h, i) = m

        # do math
        newx = (a * x) + (b * y) + (c * z)
        newy = (d * x) + (e * y) + (f * z)
        newz = (g * x) + (h * y) + (i * z)
        
        # return new p
        return (newx, newy, newz)


    ###
    # translate a point by the delta specified
    #
    # @param p - the (x, y, z) point to translate
    # @param delta - the (dx, dy, dz) amount to translate the point by
    # @returns - the translated point
    #
    def _translate_point(self, p, delta):
        return (p[0] + delta[0], p[1] + delta[1], p[2] + delta[2])


    ###
    # set the position of the wire by setting it's center position, and rotation
    #
    # @param position - (x,y,z) of center of wire
    # @param rotation - (rx,ry,rz) degrees rotation around each axis
    #
    def setCenter(self, position, rotation):
        
        #
        # we're going to rotate the line as if the center is at (0, 0, 0),
        # and then reposition it to center
        #

        # compute p1 and p2 as if centered at (0,0,0)
        p1 = (-self._length/2, 0, 0)
        p2 = (self._length/2, 0, 0)

        # rotation p1 and p2 around x,y,z axes by rotation
        p1 = self._rotate_point(p1, rotation)
        p2 = self._rotate_point(p2, rotation)

        # reposition p1 and p2 to position
        p1 = self._translate_point(p1, position)
        p2 = self._translate_point(p2, position)

        # now that p1 and p2 are computed, remember them
        self._p1 = p1
        self._p2 = p2


    ###
    # set the position of the wire by setting its P1 position, and rotation
    #
    # @param position - (x,y,z) of P1 of wire
    # @param rotation - (rx,ry,rz) degrees rotation around each axis
    #
    def setP1(self, position, rotation):

        # compute p2 as if p1 was at the center (0, 0 ,0)
        p2 = (self._length/2, 0, 0)

        # rotate p2 around x,y,z axis
        p2 = self._rotate_point(p2, rotation)

        # reposition p1 and p2 to point specified
        self._p1 = position
        self._p2 = self._translate_point(p2, p1)


    ###
    # set the position of the wire by setting its P2 position, and rotation
    #
    # @param position - (x,y,z) of P2 of wire
    # @param rotation - (rx,ry,rz) degrees rotation around each axis
    #
    def setP2(self, position, rotation):

        # compute p1 as if p2 was at the center (0, 0 ,0)
        p1 = (-self._length/2, 0, 0)

        # rotate p1 around x,y,z axis
        p1 = self._rotate_point(p1, rotation)

        # reposition p1 and p2 to point specified
        self._p1 = self._translate_point(p1, p2)
        self._p2 = position


