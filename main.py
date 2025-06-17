"""
__________________________________ChordMD__________________________________

This program asks the user to input the chords in the key of G. 

The script replaces the chords with the Nashville Number System parallel. 

This is useful for musicians to transpose easier to other keys.

                               ©sjcreator06

"""

# Creates a list of all the Chords in the Key of G
G_chords = []

chordsFile = open("keyofG.txt", "r")

for chord in chordsFile:
    G_chords.append(chord.strip())

# Reads the Song Input File
songFile = open("songInput.txt", "r")

songFileString = songFile.read()

# Checks if the Song File is Empty
if len(str(songFileString)) == 0:
    print("Please update song.txt with the chords of your song in the key of G")
    
else:
    print("__________ChordMD_________"+ "\n")

numberSystemFile = open("numberSystem.txt", "r")

# Creates a list for the Nashville Number System
chordNumbers  = []

for chord in numberSystemFile:
    chordNumbers.append(chord.strip())

songFileUpdated = songFileString.replace(G_chords[13], str(chordNumbers[13]))\
    .replace(G_chords[1],str(chordNumbers[1]))\
        .replace(G_chords[2],str(chordNumbers[2]))\
            .replace(G_chords[3],str(chordNumbers[3]))\
                .replace(G_chords[4],str(chordNumbers[4]))\
                    .replace(G_chords[5],str(chordNumbers[5]))\
                        .replace(G_chords[6],str(chordNumbers[6]))\
                            .replace(G_chords[7],str(chordNumbers[7]))\
                                .replace(G_chords[8],str(chordNumbers[8]))\
                                    .replace(G_chords[9],str(chordNumbers[9]))\
                                        .replace(G_chords[10],str(chordNumbers[10]))\
                                            .replace(G_chords[11],str(chordNumbers[11]))\
                                                .replace(G_chords[12],str(chordNumbers[12]))\
                                                        .replace(G_chords[14],str(chordNumbers[14]))\
                                                            .replace(G_chords[15],str(chordNumbers[15]))\
                                                                .replace(G_chords[16],str(chordNumbers[16]))\
                                                                    .replace(G_chords[0],str(chordNumbers[0]))



print(songFileUpdated)