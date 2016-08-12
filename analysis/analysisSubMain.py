class Analysis(object):
    def __init__(self):
        self.fwlog=open("log.txt","w",0)
        self.fwlog.write( "timestepID Temp \t\tPE \t\t\tKE \n" )
        self.fwXYZ=open("vmd.xyz","w",0)   
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