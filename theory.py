class MusicTheory:
    all_notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A","A#", "B"]
    natural_notes = ["C", "D", "E", "F", "G", "A", "B"]
    sharps = ["F", "C", "G", "D", "A", "E", "B"]
    flats = sharps[::-1]
    flats_mapping = {
        "C#": "D♭",
        "D#": "E♭",
        "F#": "G♭",
        "G#": "A♭",
        "A#": "B♭"
    }

    #Returns the note in the givenm interval from the given note
    #Input direction 'dim' for going down the scale and 'aug' for going up the scale
    #Input if the return note should be a flat or a sharp True --> flat, False --> sharp
    #Input the steps function will traverse the scale 'half' --> in half steps, 'full' --> full steps
    #Input the interval (number of steps)
    #Returns an object containing natural note, and two boolean values for sharp and flat
    @classmethod
    def getIntervalNote(self, note : str, direction : str, flat : bool, steps : str, number_steps : int):
        index_curr = MusicTheory.all_notes.index(note)
        new_flat = False
        new_sharp = False

        if steps not in ["half", "full"]:
            raise ValueError("Steps parameter has to be 'half' or 'full'!")
        
        reducer = 1 * number_steps if steps == "half" else 2 * number_steps
        new_index = (index_curr - reducer) % len(MusicTheory.all_notes) if direction == "dim" else (index_curr + reducer) % len(MusicTheory.all_notes)
        new_note = MusicTheory.all_notes[new_index]

        if (len(new_note) > 1):
            if flat:
                new_note = MusicTheory.flats_mapping.get(new_note)
                new_flat = True
            else:
                new_sharp = True
        
        return {"name" : new_note, "sharp" : new_sharp, "flat" : new_flat }
    
    @classmethod
    def getSharps(self, root : str, minor : bool):
        
        if not minor:
            index = MusicTheory.sharps.index(root) 
            if index > 1:
                return MusicTheory.sharps[:index-1]
            elif index == 0:
                return "in progress"
            else: return []

    @classmethod
    def create_scale(self, root):
        scale = MusicTheory.natural_notes
        index_start = scale.index(root)
    
        scale.extend(scale[:index_start])
        del scale[:index_start]

        return scale
