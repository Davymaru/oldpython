def nato_alph():
#REMEMBER TO SPACE OUT SO YOU CAN READ IT

    return {
    'A': 'Alpha', 

    'B': 'Bravo', 

    'C': 'Charlie',

    'D': 'Delta',

    'E': 'Echo',

    'F': 'Foxtrot',

    'G': 'Golf',

    'H': 'Hotel',

    'I': 'India',

    'J': 'Juliett',

    'K': 'Kilo',

    'L': 'Lima', 

    'M': 'Mike',

    'N': 'November',

    'O': 'Oscar',

    'P': 'Papa',

    'Q': 'Quebec',

    'R': 'Romeo',

    'S': 'Sierra', 

    'T': 'Tango',

    'U': 'Uniform', 

    'V': 'Victor',

    'W': 'Whiskey', 

    'X': 'X-ray',

    'Y': 'Yankee',

    'Z': 'Zulu'
    }

def spell_word(word, nato_alphabet):
   
    spelled_word = []
   
    for letter in word:
   
        if letter.upper() in nato_alphabet:
   
            spelled_word.append(nato_alphabet[letter.upper()])
   
        else:
   
            spelled_word.append(letter)
   
    return spelled_word

def main():
   
    nato_alphabet = nato_alph()
   
    word = input("enter a word: ")
   
    spelled_word = spell_word(word, nato_alphabet)
   
    print("here is what it is in the nato alphabet:")
   
    print(spelled_word)


main()
