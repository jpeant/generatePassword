####################################################
#   Name:   generatePassword.py
#   Usage:  py %filename.py 
#
#   Args:   (length 8 - 24, complexity level 1 - 3)
#
#   Date:   7.3.2023
#   Author: jpeant
#####################################################

import secrets
import string
import sys, getopt

def main(params):
  letters = string.ascii_letters
  numerals = string.digits
  symbols = string.punctuation
  charbucket = ''
  password = ''
  length = 0

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
    
# complexity level 1-3, default is 3.

  if len(sys.argv) > 2:
    if int(sys.argv[2]) == 1:
      charbucket += letters
    elif int(sys.argv[2]) == 2:
      charbucket += letters + numerals
    elif int(sys.argv[2] >= 3):
      charbucket += letters + numerals + symbols
  else:
    charbucket += letters + numerals + symbols
          
# random character chooser.

  for i in range(length):
    password += ''.join(secrets.choice(charbucket))

  print(password)
  
if __name__ == '__main__':
    main(sys.argv[1:])
