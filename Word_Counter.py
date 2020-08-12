#Jack Gryzik
#Python Word Count Assignment (Github)
#8/12/2020

# file Word_Counter.py
import sys
import pathlib
from builtins import input

loopState = 0
#while loop to verify if file type is a .txt file, using pathlib method Path().suffix to check if .txt
while loopState == 0:
    fileName = input('Please enter the name of the file (ending in .txt): ')
    if pathlib.Path(fileName).suffix == '.txt':
        break
    print('The filename you entered is not a text file. Please try again.')

#Opening and reading from text file:
with open(fileName, 'r') as f:
    input = f.read()

#Word count function
def wordCount(a):
    
    counter = 0
    state = False
    #for loop iterating through each character to identify word-separating characters (space, new line, tab)
    for i in range (len(a)):
        if a[i] == ' ' or a[i] == '\n' or a[i] == '\t': #if a word-separating character is found, sets the state to false
            state = False

        elif state == False:    
            state = True       #resets state to true, set for next iteration of for loop if necessary
            counter = counter+1 #increases word count

    return counter

wordsInFile = wordCount(input) #variable to print total words counted

print(f'Number of words in text file : {wordsInFile}') #print to console
    




