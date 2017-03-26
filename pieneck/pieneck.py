class Pieneck(object):

    ###
    # object instance method
    #
    def __init__(self):

        # variables to hold simulation properties
        self._geometry = [ ]
        self._properties = [ ]
        self._comments = [ ]
        self._fstart = 299.8e6
        self._fstop = 299.8e6
        self._fstep = 0


    ###
    # adds a component to the pieneck simulation environment
    #
    # @param component - the component to add
    #
    def add(self, component):
        if component.isGeometry():
            self._geometry.append(component)
        elif component.isProperty():
            self._properties.append(component)
        else:
            raise Error("unsupported component type: %s" % component)


    ###
    # specifies the frequency range we are going to measure
    #
    # @param fstart - start frequency
    # @param fstop - stop frequency
    # @param fstep - frequency interval to step over range
    def frequency(self, fstart, fstop, fstep):
        self._fstart = fstart
        self._fstop = fstop
        self._fstep = fstep


    ###
    # write the simulation configuration out to an NEC file
    #
    # @param filename - the filename to open and write the NEC file to
    #
    def writeNecFile(self, filename):
        
        # open file, overwriting if it exists
        fp = open(filename, "w")

        # output comments
        fp.write("CM --- NEC2 Input File created by pieneck\n")
        for c in self._comments:
            fp.write("CM %s\n" % c)
        fp.write("CE --- End Comments ---\n")

        # write contents of geometry
        for c in self._geometry:
            fp.write("%s\n" % c.to_nec())
        fp.write("GE 0 0 0 0 0 0 0 0 0\n")

        # write all our properties
        for c in self._properties:
            fp.write("%s\n" % c.to_nec())
    
        # write the frequency card
        num = ((self._fstop - self._fstart) / self._fstep) + 1
        fp.write("FR 0 %d 0 0 %f %f 0 0 0 0\n" % (num, self._fstart, self._fstep))

        # write the END card, it's always last
        fp.write("EN 0 0 0 0 0 0 0 0 0\n")

        # close the file
        fp.close()
