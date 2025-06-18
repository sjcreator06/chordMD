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
    songFile = open("Data/songInput.txt", "r")
    songFile = open("Data/songInput.txt", "r")
    songFileString = songFile.read()

    # Creates a list for the Nashville Number System
    numberSystemFile = open("Data/numberSystem.txt", "r")
    numberSystemFile = open("Data/numberSystem.txt", "r")
    for chord in numberSystemFile:
        chordNumbers.append(chord.strip())


    # Create a Dictionary for the Chords of Each Key (Key:List of Chords)
    chordDatabase = open("Data/chordsDatabase.csv", "r")
    chordDatabase = open("Data/chordsDatabase.csv", "r")

    # Reading the Chords Database and Creating a List for Each Key and List of all Keys
    for chordGroup in chordDatabase:
        keyChords.append(chordGroup.split(","))

    for key in keyChords:
        keys.append(key[0])

    print()

def replaceChords():
    global songFileUpdated
    songFileUpdated = songFileString

    order = [1, 13, 14, 15, 16, 17, 18, 19, 20, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for i in order:
        songFileUpdated = songFileUpdated.replace(keyChords[keyIndex][i], str(chordNumbers[i]))

def main():
    chordAnalysis()

    # Checks if the Song File is Empty
    if len(str(songFileString)) == 0:
        print("Please update song.txt with the chords of your song!")

    else:
        print("__________ChordMD_________"+ "\n")

    global keyIndex
    keyStr = input("Please enter the key of your song: ")
    
    keyIndex = keys.index(keyStr)

    replaceChords()

    print("\n" + songFileUpdated)

if __name__ == "__main__":
    main()
