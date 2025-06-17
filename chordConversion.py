"""
__________________________________ChordMD__________________________________

This program asks the user to input the chords in any key. 

The script replaces the chords with the Nashville Number System chords. 

This is useful for musicians to transpose easier to other keys.

                               ©sjcreator06
"""

def chordAnalysis():
    global songFileString,chordNumbers,G_chords,keyChords,keys

    # Lists
    chordNumbers  = []
    keyChords = []
    keys = []

    # Reads the Song Input File
    songFile = open("songInput.txt", "r")
    songFile = open("Data/songInput.txt", "r")
    songFileString = songFile.read()

    # Creates a list for the Nashville Number System
    numberSystemFile = open("numberSystem.txt", "r")
    numberSystemFile = open("Data/numberSystem.txt", "r")
    for chord in numberSystemFile:
        chordNumbers.append(chord.strip())


    # Create a Dictionary for the Chords of Each Key (Key:List of Chords)
    chordDatabase = open("chordsDatabase.csv", "r")
    chordDatabase = open("Data/chordsDatabase.csv", "r")

    # Reading the Chords Database and Creating a List for Each Key and List of all Keys
    for chordGroup in chordDatabase:
        keyChords.append(chordGroup.split(","))

    for key in keyChords:
        keys.append(key[0])

    print()



def replaceChords():
    global songFileUpdated

    songFileUpdated = songFileString.replace(keyChords[keyIndex][13], str(chordNumbers[13]))\
        .replace(keyChords[keyIndex][15],str(chordNumbers[15]))\
            .replace(keyChords[keyIndex][1],str(chordNumbers[1]))\
                .replace(keyChords[keyIndex][2],str(chordNumbers[2]))\
                    .replace(keyChords[keyIndex][3],str(chordNumbers[3]))\
                        .replace(keyChords[keyIndex][4],str(chordNumbers[4]))\
                            .replace(keyChords[keyIndex][5],str(chordNumbers[5]))\
                                .replace(keyChords[keyIndex][6],str(chordNumbers[6]))\
                                    .replace(keyChords[keyIndex][7],str(chordNumbers[7]))\
                                        .replace(keyChords[keyIndex][8],str(chordNumbers[8]))\
                                            .replace(keyChords[keyIndex][9],str(chordNumbers[9]))\
                                                .replace(keyChords[keyIndex][10],str(chordNumbers[10]))\
                                                    .replace(keyChords[keyIndex][11],str(chordNumbers[11]))\
                                                        .replace(keyChords[keyIndex][12],str(chordNumbers[12]))\
                                                                .replace(keyChords[keyIndex][14],str(chordNumbers[14]))\
                                                                        .replace(keyChords[keyIndex][16],str(chordNumbers[16]))\
                                                                            .replace(keyChords[keyIndex][0],str(chordNumbers[0]))



def main():
    chordAnalysis()

    # Checks if the Song File is Empty
    if len(str(songFileString)) == 0:
        print("Please update song.txt with the chords of your song!")

    else:
        print("__________ChordMD_________"+ "\n")

    songName = input("Please enter the name of your song: ")
    
    global keyIndex
    keyStr = input("Please enter the key of your song: ")
    songName = input("Please enter the name of your song: ")
    

    keyIndex = keys.index(keyStr)

    replaceChords()

    print(songFileUpdated)

if __name__ == "__main__":
    main()
