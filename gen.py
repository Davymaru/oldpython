
def two_letter_combinations(characters):


    for char1 in characters:


        for char2 in characters:

            
            combination = char1 + char2

            yield combination  

def main():
  
    characters_list = ['a', 'b', 'c']

   
    combinations_generator = two_letter_combinations(characters_list)

 
    for combination in combinations_generator:

        print(combination)


main()
