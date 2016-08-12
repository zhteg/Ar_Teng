from  simulationSettings import*
from numpy import inf
import math
from copy import deepcopy

class Analysis(object):
    def __init__(self):
        self.fwlog=open("log.txt","w",0)
        self.fwlog.write( "timestepID Temp \t\tPE \t\t\tKE \n" )
        self.fwXYZ=open("vmd.xyz","w",0)   
        self.fwRdf=open("rdf.txt","w",0)  
        self.fwAuto=open("autocorrelation.txt","w",0) 
    def dump2log(self, freq):  
        if self.timestepID % freq==0:
            self.fwlog.write( "%5i \t %8.4f %e %e \n" % (self.timestepID, self.temperature(), self.potentialEnergy(), self.kineticEnergy()) )
            print "\rstep %i " % self.timestepID,
    
    def dump2vmd(self,freq):
        if self.timestepID % freq==0:
            self.fwXYZ.write("%i \n" % self.numAtoms)
            self.fwXYZ.write("timestep %i \n" % self.timestepID)
            for atom in self.atoms:
                self.fwXYZ.write( "Ar  %8.4f %8.4f %8.4f \n" % (atom.x*10**10, atom.y*10**10, atom.z*10**10))
                
    def pairDistributionFunction(self,binNum,binWidth,freq):
        """Generates a pair-distribution function on given data"""
        if self.timestepID % freq !=0:
            return 0
        
        global boxSize, sigma, PI
        rbinWidth=binWidth*sigma
        atom_counts = [0]*binNum
        print("rdf..."),
        
        for atom1 in range(0, self.numAtoms-1):
            for atom2 in range(atom1+1, self.numAtoms):
                dx = self.atoms[atom1].x - self.atoms[atom2].x
                dy = self.atoms[atom1].y - self.atoms[atom2].y
                dz = self.atoms[atom1].z - self.atoms[atom2].z

                # Minimum Image Convention
                dx -= boxSize*round(dx/boxSize)
                dy -= boxSize*round(dy/boxSize)
                dz -= boxSize*round(dz/boxSize)
                
                r2 = dx*dx + dy*dy + dz*dz
                r = math.sqrt(r2)
                ibin=int(r//rbinWidth)
                
                # If the atom is within the 
                if ibin<binNum:
                    atom_counts[ibin]+=1
        
        self.fwRdf.write("timestep %i \n" % self.timestepID)            
        for i in range(binNum):    
            self.fwRdf.write("%f %f \n" % ((i+0.5)*binWidth,  atom_counts[i]*(boxSize)**3/self.numAtoms/(4.0*PI*((i+0.5)*rbinWidth)**2*rbinWidth)/(self.numAtoms/2.0)  ))
                        
    def velocityAutocorrelation(self, step):
        "autocorrelation t=0 at step"
        if step == self.timestepID:
            self.atom0=deepcopy(self.atoms)
        if step <= self.timestepID:  
            v2=0
            for atom in range(self.numAtoms):
                v2 += self.atom0[atom].vx * self.atoms[atom].vx +\
                      self.atom0[atom].vy * self.atoms[atom].vy +\
                      self.atom0[atom].vz * self.atoms[atom].vz
            self.fwAuto.write( "%5i %e \n" % (self.timestepID, v2/self.numAtoms))