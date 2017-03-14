#!/usr/bin/python

from pieneck.pieneck import Pieneck
from pieneck.components import Wire
import pieneck.constants


# create simulation object
pn = Pieneck()

# create a 16ga, 20m long wire
w1 = Wire(20, pieneck.constants.AWG16)
w1.setCenter((0, 0, 10), (0, 0, 0))

# add the wire to the simulation
pn.add(w1)

# add a voltage source to the simulation

# export to an NEC file
pn.writeNecFile("dipole_in_free_space.nec")
