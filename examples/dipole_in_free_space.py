#!/usr/bin/python

from pieneck.pieneck import Pieneck
from pieneck.geometry import Wire
from pieneck.properties import VoltageSource
import pieneck.constants


# create simulation object
pn = Pieneck()
pn.resolution(51, 360, 360)

# set frequency range to plot over
pn.frequency(13e6, 15e6, 100e3)

# create a 16ga, 20m long wire
w1 = Wire(20, pieneck.constants.AWG16)
w1.setCenter((0, 0, 10), (0, 0, 0))

# add the wire to the simulation
pn.add(w1)

# add a 1V voltage source to the simulation
source = VoltageSource(1 - 2j)
source.attach(w1, 50)
pn.add(source)

# export to an NEC file
pn.writeNecFile("dipole_in_free_space.nec")
