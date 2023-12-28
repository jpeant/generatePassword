'''
Generates password string 8-24 charachters long with letters, number and symbols upon complexity level given.
Uses Shuffle-Randompick-Shuffle (SranS) method.
    Usage:   generatePassword.py (parameter1, parameter2)
    Params:   (length 8 - 24, complexity level 1 - 3)
    Level 1 = letters, Level 2 = L1 + numbers, Level 3 = L2 + symbols
    Date:   7.3.2023
    Author: jpeant
'''
####################################################
#   ToDO
#   - exception error
#   - help
####################################################

import secrets
import random
import string
import sys, getopt

# subprogram. takes string and shuffles characters and returns shuffled string.
def shuffleString(string: str) -> str: 
    List = list(string)
    random.shuffle(List)
    return "".join(List)

def main(params):
  letters = string.ascii_letters  # uppper and lowercase
  numerals = string.digits        # numbers
  symbols = string.punctuation    # symbols
  charbucket = ''
  password = ''
  length = 0

# first parameter
# setting length of characters 8 - 24, default is 8.
  if len(sys.argv) > 1:
    if int(sys.argv[1]) <= 7 :
      length = 8
    elif int(sys.argv[1]) >= 24:
      length = 24
    else:
      length = int(sys.argv[1])
  else:
    length = 8

# second parameter    
# complexity level 1 - 3, default is 3.
  if len(sys.argv) > 2:
    if int(sys.argv[2]) == 1:
      charbucket += letters                         # Level 1, just letters
    elif int(sys.argv[2]) == 2:
      charbucket += letters + numerals              # Level 2, letters and numbers
    elif int(sys.argv[2]) >= 3:
      charbucket += letters + numerals + symbols    # Level 3, letters, numbers and symbols
  else:
    charbucket += letters + numerals + symbols
    
# shuffleling the characters
  shuffleString(charbucket)
          
# random character chooser.
  for i in range(length):
    password += ''.join(secrets.choice(charbucket))

# shuffle once more before output
  print(shuffleString(password))
  #return(shuffleString(password)         # in case using this as a function
  
if __name__ == '__main__':
    main(sys.argv[1:])
