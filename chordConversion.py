"""
__________________________________ChordMD__________________________________

This program asks the user to input the chords in any key. 

The script replaces chords with the Nashville Number System chords. 

This is useful for musicians to transpose easier to other keys.

                               ©sjcreator06
"""

from fpdf import FPDF

def chordAnalysis():
    global songFileString, chordNumbers, G_chords, keyChords, keys

    chordNumbers = []
    keyChords = []
    keys = []

    with open("Data/songInput.txt", "r") as songFile:
        songFileString = songFile.read()

    with open("Data/numberSystem.txt", "r") as numberSystemFile:
        for chord in numberSystemFile:
            chordNumbers.append(chord.strip())

    with open("Data/chordsDatabase.csv", "r") as chordDatabase:
        for chordGroup in chordDatabase:
            keyChords.append(chordGroup.strip().split(","))

    for key in keyChords:
        keys.append(key[0])

def replaceChords():
    global songFileUpdated

    songFileUpdated = songFileString
    for i in range(len(chordNumbers)):
        songFileUpdated = songFileUpdated.replace(keyChords[keyIndex][i], str(chordNumbers[i]))

def createFormattedPDF(songName, artistName, content):
    pdf = FPDF(format='letter')
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"{songName}", ln=True, align='C')

    # Artist
    pdf.set_font("Arial", 'I', 12)
    pdf.cell(0, 10, f"by {artistName}", ln=True, align='C')

    pdf.ln(10)

    # Chord content
    pdf.set_font("Courier", size=11)
    for line in content.splitlines():
        pdf.multi_cell(0, 8, line)

    pdf.output(artistName + "_" + songName + "_" +  ".pdf")


def main():
    chordAnalysis()

    if len(songFileString.strip()) == 0:
        print("Please update songInput.txt with the chords of your song!")
        return

    print("__________ChordMD_________\n")

    songName = input("Please enter the name of your song: ")
    artistName = input("Please enter the name of the artist: ")
    keyStr = input("Please enter the key of your song: ")

    global keyIndex
    keyIndex = keys.index(keyStr.upper())

    replaceChords()

    createFormattedPDF(songName, artistName, songFileUpdated)

    print("\nFormatted song PDF saved as 'ChordMD_Output.pdf'.")
    print("\n--- Converted Song ---\n")
    print(songFileUpdated)

if __name__ == "__main__":
    main()
