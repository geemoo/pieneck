#!/usr/bin/python

from pieneck.pieneck import Pieneck
from pieneck.components import Wire
import pieneck.constants


# create simulation object
pn = Pieneck()

# set frequency range to plot over
pn.frequency(13e6, 15e6, 100e3)

# create a 16ga, 20m long wire
w1 = Wire(20, pieneck.constants.AWG16)
w1.setCenter((0, 0, 10), (0, 0, 0))

# add the wire to the simulation
pn.add(w1)

# add a 1V voltage source to the simulation
source = VoltageSource(1)
source.attach(w1, 50)

# export to an NEC file
pn.writeNecFile("dipole_in_free_space.nec")
