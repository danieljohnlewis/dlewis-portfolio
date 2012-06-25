# @author Daniel Lewis ( danieljohnlewis@gmail.com )
# An efficient "in-place" string reversal algorithm, taking an argument from command line
# Could probably enhance it a little more by using negative indexes.. e.g. word[-i+1:] instead of word[l-i+1:]

from sys import argv
word = argv[1]

i = 0
l = len(word)-1
while i<(int(round(l/2))):
	word = word[:i] + word[l-i] + word[i+1:l-i] + word[i] + word[l-i+1:]
	i += 1

print(word)
