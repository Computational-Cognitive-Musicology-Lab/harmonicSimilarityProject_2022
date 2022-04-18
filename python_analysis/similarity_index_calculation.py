
import pandas as pd
import numpy as np
import copy
import seaborn as sns

notes_to_numbers_flat = {'C':1, 'C#':2, 'D':3, 'D#':4, 'E':5, 'F':6, 'F#':7, 'G':8, 'G#':9, 'A':10, 'A#':11, 'B':12} #flat: b
notes_to_numbers_sharp = {'C':1, 'Db':2, 'D':3, 'Eb':4, 'E':5, 'F':6, 'Gb':7, 'G':8, 'Ab':9, 'A':10, 'Bb':11, 'B':12}#sharp: #
numbers_to_notes_flat = {1:'C', 2:'C#', 3:'D', 4:'D#', 5:'E', 6:'F', 7:'F#', 8:'G', 9:'G#', 10:'A', 11:'A#', 12:'B'} #flat: b
numbers_to_notes_sharp = {1:'C', 2:'Db', 3:'D', 4:'Eb', 5:'E', 6:'F', 7:'Gb', 8:'G', 9:'Ab', 10:'A', 11:'Bb', 12:'B'}#sharp: #

def note_add(note_num, add):
    if (note_num + add > 12):
        return (note_num + add - 12)
    else:
        return (note_num + add)

#chord types (take root C as an example)
#C, Cm, Cdim, Caug, C7, Cm7, Cmaj7, C9, Cadd9, Cm9, Cmaj9, C6, Cm6, 
#Csus2, Csus4, C11, C13, Cdim7, Caug7, Cm7b5, C7b5, C7#9
def major(root):
    chord_index_list = [1, 5, 8]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list
def minor(root):
    chord_index_list = [1, 4, 8]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list
def dim(root):
    chord_index_list = [1, 4, 7]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list
def aug(root):
    chord_index_list = [1, 5, 9]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list
def dominant7(root):
    chord_index_list = [1, 5, 8, 11]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list
def major7(root):
    chord_index_list = [1, 5, 8, 12]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list
def minor7(root):
    chord_index_list = [1, 4, 8, 11]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list
def add9(root):
    chord_index_list = [1, 5, 8, 3]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list
def major9(root):
    chord_index_list = [1, 5, 8, 12, 3]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list
def minor9(root):
    chord_index_list = [1, 4, 8, 11, 3]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list
def dominant9(root):
    chord_index_list = [1, 5, 8, 11, 3]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list
def major6(root):
    chord_index_list = [1, 5, 8, 10]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list
def minor6(root):
    chord_index_list = [1, 4, 8, 10]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list
def sus4(root):
    chord_index_list = [1, 6, 8]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list
def sus2(root):
    chord_index_list = [1, 3, 8]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list
def dominant11(root):
    chord_index_list = [1, 5, 8, 11, 3, 6]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list
def dominant13(root):
    chord_index_list = [1, 5, 8, 11, 3, 6, 10]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list
def minor7flat5(root):
    chord_index_list = [1, 4, 7, 9]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list
def dim7(root):
    chord_index_list = [1, 4, 7, 10]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list
def aug7(root):
    chord_index_list = [1, 5, 9, 11]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list    
def sevensharp9(root):
    chord_index_list = [1, 5, 8, 11, 4]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list
def sevenflat5(root):
    chord_index_list = [1, 5, 7, 11]
    chord_list = []
    for i in chord_index_list:
        chord_list.append(note_add(i, root-1))
    return chord_list

def detect_root(chord): #detect root of the chords
    if '/' in chord:
        chord = chord[:chord.find('/')]
    if "'" in chord:
        chord = chord[:chord.find("'")]
    if '#' in chord or 'b' in chord:
        if chord[1]=='#' or chord[1]=='b':
            return chord[:2]
        else:
            return chord[0]
    else:
        return chord[0]
def detect_chord_type(chord):
    if '/' in chord:
        chord = chord[:chord.find('/')]
    if "'" in chord:
        chord = chord[:chord.find("'")]
    if 'm7b5' in chord:
        return 'm7b5'
    else:
        chord = chord.replace('#','')#make root as C
        chord = chord.replace('b','')
        return chord[1:]

def key_normalization(note_num, key_num): #transfer original key to key C
    if (note_num - key_num >= 0): #key_num: original key
        return (note_num-key_num+1)
    else:
        return (13 + note_num - key_num)
def chord_normalization(chord, initial_key):    
    chord_root = detect_root(chord)
    chord_type = detect_chord_type(chord)
    if '#' in chord_root:
        note_num = notes_to_numbers_flat.get(chord_root)
    else:
        note_num = notes_to_numbers_sharp.get(chord_root)
    if '#' in initial_key:
        key_num = notes_to_numbers_flat.get(initial_key)
    else:
        key_num = notes_to_numbers_sharp.get(initial_key)    
    transfer_root = key_normalization(note_num, key_num)
    transfer_note = numbers_to_notes_sharp.get(transfer_root)
    return str(transfer_note)+chord_type
def chord_progression_normalization(chord_list, initial_key):
    if initial_key == 'C':
        return chord_list
    else:
        if chord_list == ['nan']:
            return chord_list
        else:
            normalized_chord_list = []
            for chord in chord_list:
                normalized_chord_list.append(chord_normalization(chord, initial_key))
            return normalized_chord_list
def progression_group_normalization(progression_group, initial_key):
    normalized_group = []
    for chord_list in progression_group:
        normalized_group.append(chord_progression_normalization(chord_list, initial_key))
    return normalized_group

def chord_simplification(chord):
    root_note = detect_root(chord)
    if 'maj' in chord:
        chord_type = ''
    else:
        if 'm' in chord:
            chord_type = 'm'
        else:
            chord_type = ''
    return root_note+chord_type
def chord_progression_simplification(chord_list): #['Am7', 'Em7', 'G7', 'C7']
    simplified_list = []
    for i in chord_list:
        simplified_list.append(chord_simplification(i))
    return simplified_list
def progression_group_simplification(progression_group): #[['Cmaj7', 'Gadd9', 'Am7', 'F11'], ['nan'], ['nan'], ['nan']]
    simplified_group = []
    for chord_list in progression_group:
        if chord_list == ['nan']:
            simplified_group.append(['nan'])
        else:
            simplified_group.append(chord_progression_simplification(chord_list))
    return simplified_group

def root_to_note(root):
    if '#' in root:
        return notes_to_numbers_flat.get(root)
    elif 'b' in root:
        return notes_to_numbers_sharp.get(root)
    else:
        return notes_to_numbers_flat.get(root)
def chord_to_notes(chord): # return note list for chords
    root_note = detect_root(chord)
    if '#' in root_note:
        root = notes_to_numbers_flat.get(root_note)
    else:
        root = notes_to_numbers_sharp.get(root_note)
    chord_type = detect_chord_type(chord)
    if chord_type == '':
        return major(root)
    elif chord_type == 'm':
        return minor(root)
    elif chord_type == 'dim':
        return dim(root)
    elif chord_type == 'aug':
        return aug(root)
    elif chord_type == '7':
        return dominant7(root)
    elif chord_type == 'maj7':
        return major7(root)
    elif chord_type == 'm7':
        return minor7(root)
    elif chord_type == 'add9':
        return add9(root)
    elif chord_type == 'maj9':
        return major9(root)
    elif chord_type == 'm9':
        return minor9(root)
    elif chord_type == '9':
        return dominant9(root)
    elif chord_type == '6':
        return major6(root)
    elif chord_type == 'm6':
        return minor6(root)
    elif chord_type == 'sus4':
        return sus4(root)
    elif chord_type == 'sus2':
        return sus2(root)
    elif chord_type == '11':
        return dominant11(root)
    elif chord_type == '13':
        return dominant13(root)
    elif chord_type == 'm7b5':
        return minor7flat5(root)
    elif chord_type == 'dim7':
        return dim7(root)
    elif chord_type == 'aug7':
        return aug7(root)
    elif chord_type == '7#9':
        return sevensharp9(root)
    elif chord_type == '7b5':
        return sevenflat5(root)
    else:
        print(chord_type, ': unknown, please check again')


# ## Chord Progression Similarity Index
def transition_matrix(chord_list, first_chord_weight): 
    matrix_list = copy.deepcopy(chord_list)
    matrix_list.append(matrix_list[0])
    matrix = np.zeros((12,12))   
    chord_index = 0
    while chord_index < len(matrix_list) - 1:
        chord1 = matrix_list[chord_index]
        chord2 = matrix_list[chord_index+1]        
        if chord_index == 0:
            for i in chord_to_notes(chord1):
                for j in chord_to_notes(chord2):
                    matrix[i-1][j-1] = matrix[i-1][j-1] + 1 + first_chord_weight
        else:
            for i in chord_to_notes(chord1):
                for j in chord_to_notes(chord2):
                    matrix[i-1][j-1] = matrix[i-1][j-1] + 1
        chord_index = chord_index + 1
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if np.sum(matrix[i]) != 0:
                matrix[i][j] = matrix[i][j]/np.sum(matrix[i])   
    return matrix #return np.array

def root_transition_matrix(chord_list, first_chord_weight):#chord_list:['Am','Cm','Em','G']; first_chord_weight:[0,1]
    root_list = []
    for i in chord_list:
        root_list.append(detect_root(i))
    matrix_list = copy.deepcopy(root_list)
    matrix_list.append(matrix_list[0])
    matrix = np.zeros((12,12))
    root_index = 0    
    while root_index < len(matrix_list) - 1:
        root1 = root_to_note(matrix_list[root_index])-1
        root2 = root_to_note(matrix_list[root_index+1])-1   
        if np.sum(matrix[root1]) == 0:
            matrix[root1][root2] = 1
        else:
            exist = np.count_nonzero(matrix[root1])+1
            for i in range(len(matrix[root1])):
                if matrix[root1][i] != 0:
                    matrix[root1][i] = 1/exist
            matrix[root1][root2] = 1/exist
        root_index = root_index + 1   
    first_root = root_to_note(matrix_list[0])-1
    second_root = root_to_note(matrix_list[1])-1
    if np.count_nonzero(matrix[first_root]) == 1:
        return matrix
    else:
        matrix[first_root][second_root] = matrix[first_root][second_root]*(1+first_chord_weight)
        rest = np.count_nonzero(matrix[first_root])-1
        for i in range(len(matrix[first_root])):
            if (i != second_root) and (matrix[first_root][i] != 0):
                matrix[first_root][i] = (1-matrix[first_root][second_root])/rest
        return matrix

def matrix_distance(matrix1, matrix2): #Euclidean Distance
    sum = 0
    for i in range(0, len(matrix1)): #rows
        for j in range(0, len(matrix1[0])): #colomns
            sum = sum + (matrix1[i][j]-matrix2[i][j])**2
    distance = np.sqrt(sum)
    return distance

def similarity_index_v1(song1, song2, first_chord_weight1, first_chord_weight2): #base on groups: chordlist_song1, chordlist_song2
    matrix = np.zeros((len(song1),len(song2)))
    for i in range(0, len(song1)):
        for j in range(0, len(song2)):
            matrix[i][j]=matrix_distance(transition_matrix(song1[i],first_chord_weight1),transition_matrix(song2[j],first_chord_weight2))
    song1_index1, song2_index1 = 0, 0
    for i in range(0,len(matrix)):
        song1_index1 = song1_index1 + min(matrix[i])
    for i in range(0, len(matrix.transpose())):
        song2_index1 = song2_index1 + min(matrix.transpose()[i])
    return [song1_index1/len(song1), song2_index1/len(song2)]

def similarity_index_v2(song1, song2, first_chord_weight1, first_chord_weight2): #base on songs: chordlist_song1, chordlist_song2
    return matrix_distance(transition_matrix(song1, first_chord_weight1), transition_matrix(song2, first_chord_weight2))

def root_similarity_index_v1(song1, song2, weight1, weight2): #base on groups, first_chord_weight1, first_chord_weight2
    matrix = np.zeros((len(song1),len(song2)))
    for i in range(0, len(song1)):
        for j in range(0, len(song2)):
            matrix[i][j]=matrix_distance(root_transition_matrix(song1[i],weight1),root_transition_matrix(song2[j],weight2))
    song1_index1, song2_index1 = 0, 0
    for i in range(0,len(matrix)):
        song1_index1 = song1_index1 + min(matrix[i])
    for i in range(0, len(matrix.transpose())):
        song2_index1 = song2_index1 + min(matrix.transpose()[i])
    return [song1_index1/len(song1), song2_index1/len(song2)]

def root_similarity_index_v2(song1, song2, first_chord_weight1, first_chord_weight2):
    return matrix_distance(root_transition_matrix(song1, first_chord_weight1), root_transition_matrix(song2, first_chord_weight2))


similarity_function_mode = input('input the similarity index function (group:1; full: 2): ')
if similarity_function_mode == '1': #Em C G D, Em C G D
    print('Example chord progression groups input: Em C G D,Em C G D\nExample key input: Eb (D#)\nExample weight input: float between 0.0-1.0' )
    song1_str = input('input chord progression groups for song 1: ')
    song1_key = input('input key for song 1: ')
    song1_weight = input('input the weight of the first chord in song 1: ')
    song2_str = input('input chord progression groups for song 2: ')
    song2_key = input('input key for song 2: ')
    song2_weight = input('input the weight of the first chord in song 2: ')
    song1_group_list = song1_str.split(',')
    song2_group_list = song2_str.split(',')
    song1_original, song2_original = [], []
    for i in song1_group_list:
        song1_original.append(i.split(' '))
    for i in song2_group_list:
        song2_original.append(i.split(' ')) 
    song1 = progression_group_normalization(song1_original, song1_key)
    song2 = progression_group_normalization(song2_original, song2_key)
    print('similarity index: ', similarity_index_v1(song1, song2, float(song1_weight), float(song2_weight)))
else:#Em C G D
    print('Example input: Em C G D\nExample key input: Eb (D#)\nExample weight input: float between 0.0-1.0')
    song1_str = input('input chord progression for song 1: ')
    song1_key = input('input key for song 1: ')
    song1_weight = input('input the weight of the first chord in song 1: ')
    song2_str = input('input chord progression for song 2: ')
    song2_key = input('input key for song 2: ')
    song2_weight = input('input the weight of the first chord in song 2: ')
    song1_original = song1_str.split(' ')
    song2_original = song2_str.split(' ')
    song1 = chord_progression_normalization(song1_original, song1_key)
    song2 = chord_progression_normalization(song2_original, song2_key)
    print('similarity index: ', similarity_index_v2(song1, song2, float(song1_weight), float(song2_weight)))


