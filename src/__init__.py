# __main__.py

import sys
from lexer import tokenize
from syntatic import syntatic

if __name__ == "__main__":
  print("to aqui")
  if (len(sys.argv) < 2):
    exit(1)

  file = open(sys.argv[1], 'r')
  data = file.read()

  logFile = open('logs/' + sys.argv[1].split('.')[0].split('/')[-1] + '.marks', 'w')

  tokens = tokenize(data)

  for token in tokens:
    logFile.write(str(token) + '\n')

  pass
