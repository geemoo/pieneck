class Pieneck(object):

    ###
    # object instance method
    #
    def __init__(self):

        # variables to hold simulation properties
        self._geometry = [ ]
        self._comments = [ ]


    ###
    # adds a component to the pieneck simulation environment
    #
    # @param component - the component to add
    #
    def add(self, component):
        self._geometry.append(component)


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

        # close the file
        fp.close()
