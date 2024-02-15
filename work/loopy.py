bottles = 99



while bottles > 1:
    print(bottles, "bottles of beer on the wall\n",bottles, "bottles of beer\ntake one down pass it around")
   
    bottles -= 1  
   
    if bottles > 1:print(bottles, "bottles of beer on the wall\n\n")
 
    elif bottles == 1: print(bottles, "bottle of beer on the wall\n\n", bottles, "bottle of beer on the wall\n",bottles,"bottle of beer\nTake one down pass it around") 
    print ("No botttles of beer on the wall")


