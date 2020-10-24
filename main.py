#!/usr/bin/env python3
'''
Import English/German translations into Anki.
Translations come from deepl.com/translator

1. 
Copy and paste desired German sentences here:
deepl.com/translator
English outputted to the right.

2.
Copy and paste sentences into text file.
See file content example below.


File content example:

GERMAN SENTENCE 1
GERMAN SENTENCE 2
GERMAN SENTENCE 3
--------
ENGLISH SENTENCE 1
ENGLISH SENTENCE 2
ENGLISH SENTENCE 3


3.
Run this program, it'll make a csv.

4.
Import CSV into Anki, onto desired deck.
Settings:
- First column is the front of the card (English)
- Second column is the back of the card (German)
'''

import csv
import sys 

# Ask user for name of text file
if len(sys.argv) > 1:
  filename = sys.argv[1]
else:
  filename = "batch.txt"

# Removes empty lines
file1 = open(filename, 'r').read().splitlines()
lines = [line for line in file1 if line]

# Separate the English and German lines
# english_lines and german_lines should both be the same length
split_index = lines.index('--------')
german_lines = lines[:split_index]
english_lines = lines[split_index+1:]

# Pair the lines
line_tuple_pairs = list(zip(english_lines, german_lines))
line_pairs = [list(pair) for pair in line_tuple_pairs]

# Create CSV
for pair in line_pairs:
  with open('batch.csv', 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerows(line_pairs)

print("Success")
