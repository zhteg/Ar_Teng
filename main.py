# -*- coding: utf-8 -*-
"""
Created on Tue Aug 09 19:08:08 2016

@author: tzhan
"""
from atom.atomSubMain import Atoms
from integration.IntegrationSubMain import Simulation

numAtoms = 864 # Number of atoms to simulate
nSteps=1000 # Number of steps to simulate
targetTemp=90 # K
# steps for NVT, do temp rescale every "nvtRelaxation" step or when temp deviates above "tempBound" 
nvtLength, nvtRelaxation, tempBound =200, 30, 10 

fwlog=open("log.txt","w",0)
fwlog.write( "timestepID Temp \t\tPE \t\t\tKE \n" )

"""initialization: add atom, create velocity, force update"""
atoms=Atoms(numAtoms) # adding atoms by sigma distance
atoms.applyGaussian(targetTemp) # assign initial velocity
atoms.momentumCorrection()
atoms.kineticEnergy()
print "Temperature=",atoms.temperature()
atoms.updateForces()

"""NVT equaliriate structures"""
for timestepID in range(0, nvtLength):
    atoms.nvt(atoms.velocityRescale,targetTemp,nvtRelaxation,tempBound,timestepID)
    fwlog.write( "%5i \t %8.4f %e %e \n" % (timestepID, atoms.temperature(), atoms.potentialEnergy(), atoms.kineticEnergy()) )
    print "\rstep %i " % timestepID,

"""NVE production run"""
for timestepID in range(nvtLength, nSteps):
    atoms.nve()
    fwlog.write( "%5i \t %8.4f %e %e \n" % (timestepID, atoms.temperature(), atoms.potentialEnergy(), atoms.kineticEnergy()) )
    print "\rstep %i " % timestepID,
    
