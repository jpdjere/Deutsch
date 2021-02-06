# -*- coding: utf-8 -*-
import re

inputNoun = re.compile(r'.+ = \[ (.+)\] <br>(.+)')
# outputNoun = re.compile(r'$2 = $1')
inputVerb = re.compile(r'(.+ )= \[(.+·.+)\] <br>(.+)')
# outputVerb = re.compile(r'$3 = $1 <br><br> $2')
inputSpecialVerb = re.compile(r'(.+) = (.+\(\+.+\).+\[.+\])(.+)((Ej|EJ).+)')
# outputSpecialVerb = re.compile(r'$3 = $1 <br><br> $2 <br><br> $4')
inputAdjective = re.compile(r'(.+ )= \[(.+\|.+)\] <br>(.+)')
# outputAdjective = re.compile(r'$3 = $1 <br><br> \[$2\]')
inputOthersWithExample = re.compile(r'(.+ )= \[(.+\|.+)\] <br>(.+)')
# outputOthersWithExample = re.compile(r'$2 = $1 <br><br> $3')
inputOthers = re.compile(r'(.+) = (.+)')
# outputOthers = re.compile(r'$2 = $1')

totalLines = 0
editedLines = 0

with open("Wortschatz.txt", "rt") as inputFile:
  with open("Intermediate.txt", "wt") as outputFile:
    for line in inputFile:
      totalLines += 1
      
      matchTheorie = re.match(r'\[THEORIE\].+', line)
      matchNoun = re.match(inputNoun, line)
      matchVerb = re.match(inputVerb, line)
      matchSpecialVerb = re.match(inputSpecialVerb, line)
      matchAdjective = re.match(inputAdjective, line)
      matchOthersWithExample = re.match(inputOthersWithExample, line)
      matchOthers = re.match(inputOthers, line)

      if matchTheorie:
        continue
      if matchNoun:
        outputFile.write(matchNoun.group(2) + " = " + matchNoun.group(1) + "\n")
        editedLines += 1
        continue
      if matchVerb:
        outputFile.write(matchVerb.group(3) + " = " + matchVerb.group(1) +  '<br><br>[' + matchVerb.group(2) + "]\n")
        editedLines += 1
        continue
      if matchSpecialVerb:
        outputFile.write(matchSpecialVerb.group(3) + " = " + matchSpecialVerb.group(1) +  '<br><br>' + matchSpecialVerb.group(2) +  '<br><br>' + matchSpecialVerb.group(4) + "\n")
        editedLines += 1
        continue
      if matchAdjective:
        outputFile.write(matchAdjective.group(3) + " = " + matchAdjective.group(1) +  '<br><br>[' + matchAdjective.group(2) + "]\n")
        editedLines += 1
        continue
      if matchOthersWithExample:
        outputFile.write(matchOthersWithExample.group(2) + " = " + matchOthersWithExample.group(1) +  '<br><br>[' + matchOthersWithExample.group(3) + "]\n")
        editedLines += 1
        continue
      if matchOthers:
        outputFile.write(matchOthers.group(2) + " = " + matchOthers.group(1) + "\n")
        editedLines += 1
        continue
      
    print("Total Lines: ", totalLines)
    print("Edited Lines: ", editedLines)
      
with open("Intermediate.txt", "rt") as inputFileCleanup:
  with open("English_zu_Deutsch.txt", "wt") as outputFileCleanup:
    for line in inputFileCleanup:
      matchCleanup = re.match(r'^\s*<br>\s*(.+)', line)
      if matchCleanup:
        outputFileCleanup.write(matchCleanup.group(1) + "\n")
        continue
      outputFileCleanup.write(line)
