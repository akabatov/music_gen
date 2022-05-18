#Chord generator
#Emulates piano keys to camculate distance between notes
piano_sharps = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C',
               'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C']
piano_flats = ['C','Df', 'D', 'Ef', 'E', 'F', 'Gf', 'G', 'Af', 'A', 'Bf', 'B', 'C',
              'Df', 'D', 'Ef', 'E', 'F', 'Gf', 'G', 'Af', 'A', 'Bf', 'B']

#Generates triad chords for a major or a minor from a note of the scale 
def triad_gen(scale, note):
    if len(scale) < 7: return "Error: Scale must consist of 7 notes"
    two_octave = scale + scale
    if note == 1: return scale[0:5:2]
    elif note == 2: return scale[1:6:2]
    elif note == 3: return scale[2:7:2]
    elif note == 4: return two_octave[3:8:2]
    elif note == 5: return two_octave[4:9:2]
    elif note == 6: return two_octave[5:10:2]
    elif note == 7: return two_octave[6:11:2]
    else: return "Error: note must be an int in range 1<= x <= 7" 
    #print("The root triad is: '{0}'\nThe second minor chord is: '{1}'\nThe third minor chord is: '{2}'\nThe fourth major chord is: '{3}'\nThe fifth major chord is: '{4}'\nThe sixth minor chord is: '{5}'\nThe seventh diminished chord is: '{6}'".format(first_triad, second_minor, third_minor, fourth_major, fifth_major, sixth_minor, seventh_dim))

#Adds a root note on top of a triad
def triad_add_root(triad):
    triad.append(triad[0])
    return triad
    
#Geneartes seventh chords in a given scale from a given note
def seventh_gen(scale, note):
    #Make a wrapping effect
    double_octave = scale + scale 
    print(double_octave)
    
    #Maj7 from a root note
    if note == 1: return scale[0:7:2]       
    
    #Min7 from II note
    elif note == 2:                         
        for i in piano_flats:                
            if i == double_octave[3]:
                double_octave[3] = piano_flats[piano_flats.index(i)-1] 
                break 
        for j in piano_flats:
            if j == double_octave[7]: 
                double_octave[7] = piano_flats[piano_flats.index(j)-1]
                break
        return double_octave[1:8:2]
    
    #Min7 from III note
    elif note == 3:                         
        for i in piano_flats:
            if i == double_octave[4]:
                double_octave[4] = piano_flats[piano_flats.index(i)-1] 
                break 
        for j in piano_flats:
            if j == double_octave[8]: 
                double_octave[8] = piano_flats[piano_flats.index(j)-1]
                break
        return double_octave[2:9:2]
    #Maj7 from a IV note
    elif note == 4: return double_octave[3:10:2]
    
    #DOM7 from a V note
    elif note == 5: return double_octave[4:11:2] 
    
    #Min7 from a VI note
    elif note == 6:                                                                        
        for i in piano_flats:
            if i == double_octave[7]:
                double_octave[7] = piano_flats[piano_flats.index(i)-1] 
                break 
        for j in piano_flats:
            if j == double_octave[11]: 
                double_octave[11] = piano_flats[piano_flats.index(j)-1]
                break
        return double_octave[5:12:2]
        
    #Halfdim7 from VII note
    elif note == 7:                                      
        for i in piano_flats:
            if i == double_octave[8]:
                double_octave[8] = piano_flats[piano_flats.index(i)-1] 
                break 
        for k in piano_flats:
            if k == double_octave[10]:
                double_octave[10] = piano_flats[piano_flats.index(k)-1]
                break
        for j in piano_flats:
            if j == double_octave[12]: 
                double_octave[12] = piano_flats[piano_flats.index(j)-1]
                break
        return double_octave[6:13:2]
    #If note is out of range 
    return "Error: Please input a note in range 1-7"
        
        
#Returns true if the scale is major, False if minor 
def isMajor(scale):
    if getDistance(scale[0], scale[2]) == 4: return True 
    else: return False

#Calculates the distance between two notes in half steps
def getDistance(note1, note2):
    index1 = 0
    index2 = 0
    for i in piano_sharps:
        if i == note1:
            index1 = piano_sharps.index(i)
            break 
    temp = index1
    while piano_sharps[temp] != note2:
        temp += 1
    index2 = temp     
    return index2 - index1
    
def main():
    test = ['G', 'A', 'B', 'C', 'D', 'E', 'F#']
    print(triad_add_root(['D','F#','A']))
    print(seventh_gen(test, 7))
    
if __name__ == "__main__":
    main()
