class Pieneck(object):

    ###
    # object instance method
    #
    def __init__(self):

        # create a list to hold the components in
        self._components = [ ]


    ###
    # adds a component to the pieneck simulation environment
    #
    # @param component - the component to add
    #
    def add(self, component):
        self._components.append(component)


    ###
    # write the simulation configuration out to an NEC file
    #
    # @param filename - the filename to open and write the NEC file to
    #
    def writeNecFile(self, filename):
        
        # open file, overwriting if it exists
        fp = open(filename, "w")

        # write contents of simulation

        # close the file
        fp.close()
