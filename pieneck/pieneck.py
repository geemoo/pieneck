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
        self._segments = 11
        self._yrotstep = 18
        self._zrotstep = 18


    ###
    # sets the resolution properties that determines how detailed the simulation is
    #
    # @param wirechunks - how many pieces should wires be segmented into during simulation
    # @param yrotstep - how many degrees should we step when doing radation plots around y axis
    # @param zrotstep - how many degrees should we step when doing radation plots around z axis
    #
    def resolution(self, segments = 11, yrotstep = 18, zrotstep = 18):
        # store values passed in for later
        self._segments = segments
        self._yrotstep = yrotstep
        self._zrotstep = zrotstep


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

        # write contents of geometry, set tag_id's as we do this
        tag_id = 1
        for c in self._geometry:
            c._tag_id = tag_id
            tag_id = tag_id + 1
            fp.write("%s\n" % c.to_nec(self._segments))
        fp.write("GE 0 0 0 0 0 0 0 0 0\n")

        # write all our properties
        for c in self._properties:
            fp.write("%s\n" % c.to_nec())
    
        # write the frequency card
        num = ((self._fstop - self._fstart) / self._fstep) + 1
        fp.write("FR 0 %d 0 0 %f %f 0 0 0 0\n" % (num, self._fstart / 1e6, self._fstep / 1e6))

        # write the END card, it's always last
        fp.write("EN 0 0 0 0 0 0 0 0 0\n")

        # close the file
        fp.close()
