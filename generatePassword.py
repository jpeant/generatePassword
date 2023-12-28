####################################################
#   Name:   generatePassword.py
#   Usage:  py %filename.py 
#
#   Params:   (length 8 - 24, complexity level 1 - 3)
#
#   Date:   7.3.2023
#   Author: jpeant
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
  letters = string.ascii_letters
  numerals = string.digits
  symbols = string.punctuation
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
      charbucket += letters
    elif int(sys.argv[2]) == 2:
      charbucket += letters + numerals
    elif int(sys.argv[2]) >= 3:
      charbucket += letters + numerals + symbols
  else:
    charbucket += letters + numerals + symbols
    
# shuffleling the characters
  shuffleString(charbucket)
          
# random character chooser.
  for i in range(length):
    password += ''.join(secrets.choice(charbucket))

  print(shuffleString(password))
  #return(shuffleString(password)         # in case using this as a function
  
if __name__ == '__main__':
    main(sys.argv[1:])
