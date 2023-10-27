from theory import MusicTheory

class Note: 
    def __init__(self, name, sharp = False, flat = False):

        if name not in MusicTheory.natural_notes:
            raise TypeError("Note name is not correct!")

        if sharp and flat:
            raise TypeError("Note can't be sharp and flat")
        
        self.name = name
        self.sharp = sharp
        self.flat = flat

    def getSharp(self):
        return self.sharp
    
    def getFlat(self):
        return self.flat
    
    def getName(self):
        return self.name
    
    def setName(self, new_name : str):
        self.name = new_name
    
    def setSharp(self, sharp : bool):
        self.sharp = sharp
    
    def setFlat(self, flat : bool):
        self.flat = flat
    
    def noteDisplay(self):
        display_name = self.name
        
        if self.sharp and len(display_name) == 1: return display_name + "#"
        if self.flat  and len(display_name) == 1: return display_name + "♭"
        return display_name
    
    
    def noteChange(self, steps, number_steps, dir):
        flat = True if self.flat else False
        new_note = MusicTheory.getIntervalNote(self.name, dir, flat, steps, number_steps)
        self.name = new_note["name"]
        self.sharp = new_note["sharp"]
        self.flat = new_note["flat"]
    
        
            
