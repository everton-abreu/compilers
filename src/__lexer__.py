# src/__lexer__.py

import sys
from lexer import tokenize

def get_tokens(data):
  return tokenize(data)
  pass

if __name__ == '__main__':
  if (len(sys.argv) < 2):
    exit(1)

  file = open(sys.argv[1], 'r')
  data = file.read()

  logFile = open('logs/marks/' + sys.argv[1].split('.')[0].split('/')[-1] + '.marks', 'w')

  tokens = get_tokens(data)

  for token in tokens:
    logFile.write(str(token) + '\n')
