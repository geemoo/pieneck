###
# abstract class for properties
#
class Property(object):

    ###
    # is this object a property?
    #
    # @returns - true
    #
    def isProperty(self):
        return True


    ###
    # is this object a geometry component?
    #
    # @returns - false
    #
    def isGeometry(self):
        return False


###
# this class represents an excitation source in the simulation
# at the moment, this is an abstract class
#
class Source(Property):
    

    ###
    # instance method
    #
    def __init__(self):
        
        # call super
        super(Source, self).__init__()

        # create variables to hold things we need
        self._attached = None
        self._position = None


    ###
    # attach a source to a geometry object
    #
    # @param component - the geometry component to attach to
    # @param position - the position to attach to
    # @returns - none
    #
    def attach(self, component, position):
        
        # store component and position
        self._attached = component
        self._position = position


###
# class to represent a voltage source in the system
#
class VoltageSource(Source):

    # 
    # define constants
    #
    APPLIED_E_FIELD = 0


    ###
    # instance method
    #
    # @param voltage - voltage value, can be a scalar or complex value
    # @param flags - used to alter the type of voltage source.  defaults to "applied-e-field", can be "applied-e-field"
    #
    def __init__(self, voltage, flags = None):

        # call super constructor
        super(VoltageSource, self).__init__()

        # store voltage
        self._voltage = voltage

        # parse sourcetype if set
        if flags is None:
            self._type = VoltageSource.APPLIED_E_FIELD

        elif flags == "applied-e-field":
            self._type = VoltageSource.APPLIED_E_FIELD


    ###
    # return a string version of the source in nec format
    #
    # @returns - string in NEC format
    #
    def to_nec(self):
        seg = 0
        return "EX %d %d %d 0 %f %f 0 0 0" % (
            self._type, 
            self._attached._tag_id, seg, 
            self._voltage.real, self._voltage.imag
        )
