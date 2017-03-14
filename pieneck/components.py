
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
    # set the position of the wire by setting it's center position, and rotation
    #
    # @param position - (x,y,z) of center of wire
    # @param rotation - (rx,ry,rz) degrees rotation around each axis
    #
    def setCenter(self, position, rotation):
        pass


    ###
    # set the position of the wire by setting its P1 position, and rotation
    #
    # @param position - (x,y,z) of P1 of wire
    # @param rotation - (rx,ry,rz) degrees rotation around each axis
    #
    def setP1(self, position, rotation):
        pass


    ###
    # set the position of the wire by setting its P2 position, and rotation
    #
    # @param position - (x,y,z) of P2 of wire
    # @param rotation - (rx,ry,rz) degrees rotation around each axis
    #
    def setP2(self, position, rotation):
        pass


