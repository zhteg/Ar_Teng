
def nve():
    def verletIntegration(self):
        """Moves the system through a given time step, according to the energies"""
        for atom in range(0, self.numAtoms):
            
            # Update velocities
            self.atoms[atom].vx += (self.atoms[atom].fx/self.m)*self.dt
            self.atoms[atom].vy += (self.atoms[atom].fy/self.m)*self.dt
            self.atoms[atom].vz += (self.atoms[atom].fz/self.m)*self.dt
            
            
            # Update positions
            newX = self.atoms[atom].x + self.atoms[atom].vx*self.dt
            newY = self.atoms[atom].y + self.atoms[atom].vy*self.dt
            newZ = self.atoms[atom].z + self.atoms[atom].vz*self.dt

            # Update current positions (applying PBC)
            if newX < 0:
                self.atoms[atom].x = newX + self.lbox
            elif newX > self.lbox:
                self.atoms[atom].x = newX - self.lbox
            else:
                self.atoms[atom].x = newX
            
            if newY < 0:
                self.atoms[atom].y = newY + self.lbox
            elif newY > self.lbox:
                self.atoms[atom].y = newY - self.lbox
            else:
                self.atoms[atom].y = newY
                
            if newZ < 0:
                self.atoms[atom].z = newZ + self.lbox
            elif newZ > self.lbox:
                self.atoms[atom].z = newZ - self.lbox
            else:
                self.atoms[atom].z = newZ