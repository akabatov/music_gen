from Note import Note
from theory import MusicTheory

class Scale():
    scale = []
    def __init__(self, root : Note, major: bool, minor : bool):
        self.root = root
        self.major = major
        self.minor = minor
    
    def get_scale(self):
        natural_scale = MusicTheory.create_scale(self.root.name)
        sharps = MusicTheory.getSharps(self.root.name, False)
        Scale.scale = natural_scale
        if len(sharps) == 0:
            return Scale.scale
        
        for note in sharps:
            note_index = Scale.scale.index(note)
            Scale.scale[note_index] = note + "#"

        return Scale.scale

        
        
    
