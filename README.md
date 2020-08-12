# WordCounter

README (Thought process for Word counter assignment)
Jack Gryzik
8/12/2020

Goal of Assignment: Count number of words in a text file and output the solution to the console
-For consistency, I'm going to establish what would be considered a word in this program (I'm using Microsoft Word as my basis for word count):
		1) Any single letter or combination of letters in the english alphabet, capitalized or uncapitalized
		2) Any integer (1, 2, 3, ...)
		3) any special character (a, ^, %, etc)

	Other things to consider:
		hyphenated words (for example "two-handed" or "life-size" will count as one word
		words that read as two (for example $4 or "four dollars") will count as one word
		
Program Structure:
	1) read text file into program (needs to be in current directory or lower) using file type verification
	2) create variable called "input" to collect data into a list
	3) scan through list using a function that looks for spacing (" "), new lines (\n), or tabs (\t) which will increment a word counter if triggered

Research done:  used pathlib library for file input verification
