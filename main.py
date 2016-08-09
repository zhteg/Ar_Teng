# -*- coding: utf-8 -*-
"""
Created on Tue Aug 09 19:08:08 2016

@author: tzhan
"""
from atom.atomSubMain import Atoms
from integration.IntegrationSubMain import simulation

numAtoms = 864 # Number of atoms to simulate
nSteps=10 # Number of steps to simulate

for step in range(0, nSteps):
    # Run the simulation for a single step
    simulation()