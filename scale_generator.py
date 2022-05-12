#relative_scales --> minor : major
relative_scales = {'C':'Ef','D':'F','E':'G','F':'Af','G':'Bf','A':'C','B':'D',   
                   'Af':'Cf','Bf':'Df', 'Ef':'Gf','F#':'A','C#':'E','G#':'B',
                   'D#':'F#','A#':'C#'}
#Define the notes 
natural_sharps = ['G', 'D', 'A', 'E', 'B', 'F#', 'C#']
natural_flats = ['F', 'Bf', 'Ef', 'Af', 'Df', 'Gf', 'Cf']
sharps = [['F#'], 
          ['F#','C#'], 
          ['F#','C#','G#'], 
          ['F#','C#','G#','D#'], 
          ['F#','C#','G#','D#','A#'],
          ['F#','C#','G#','D#','A#','E#'],
          ['F#','C#','G#','D#','A#','E#','B#']]
flats = [['Bf'], 
         ['Bf','Ef'], 
         ['Bf','Ef','Af'], 
         ['Bf','Ef','Af','Df'],
         ['Bf','Ef','Af','Df','Gf'],
         ['Bf','Ef','Af','Df','Gf','Cf'],
         ['Bf','Ef','Af','Df','Gf','Cf','Ff']]
#The rearranged scale without any signs 
just_notes = []
#flag for recursion so the scale doesnt get rearranged with the note for the relative major
flag = False

#Rearranges the scale to start from a given note
def rearrange(note):
    note_first = note[0]
    scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    scale_copy = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    temp_arr = []
    i = 0
    while scale[i] != note_first:
        temp_arr.append(scale[i])
        scale_copy.pop(0)
        i = i + 1
    return scale_copy + temp_arr
        
#Return the scale of a key 
def scale_generator(key,major):
    global flag
    global just_notes
    signs = []
    if flag == False:
        just_notes = rearrange(key)
        
    #If minor then use relative scales 
    if major == False:
        flag = True 
        just_notes = rearrange(key)
        return scale_generator(relative_scales[key], True)
        
    #If it is a natural major and not F then get the sharps for the scale
    if (len(key) == 1 or key[1] == '#') and key != 'F':
        for i in natural_sharps:
            if i == key:
                signs.append(sharps[natural_sharps.index(i)])
                signs = [item for elem in signs for item in elem]
    elif key == 'F' or key[1] == "f":
        for i in natural_flats:
            if i == key:
                signs.append(flats[natural_flats.index(i)])
                signs = [item for elem in signs for item in elem]
                
    #Change the signs in the scale            
    for i in just_notes:
        for j in signs:
            if j[0] == i:
                just_notes[just_notes.index(i)] = signs[signs.index(j)]
    return just_notes
    
def main():
    print(scale_generator('G',False))
    
if __name__ == "__main__":
    main()
