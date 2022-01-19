# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 15:11:05 2022

@author: amar.gadipudi
"""
"""
Problem 3_6:
Write a program (not just a function, but a stand alone program or script) that 
reads through a file and writes another file that gives the length of each line
in the first file.  If line is the line that you've read into your program, use
line.strip("\n") to strip away the invisible newline character at the end of
each line.  Otherwise, your count will be one higher than the autograder's. 
Note that since this is a program running from the Command Window (or terminal
or cmd.exe), it won't be runnable as our usual functions are by entering
Shift-Enter.  You should use the File menu in Spyder to create you own file.
But, if you prefer, there is a starter file called problem3_6starter.py.

Here is a run of my solution program using the HumptyDumpty.txt file. The run
is followed by a printout of HumptyDumpty.txt and the written file
HumptyLength.txt. Note that your program does not print anything out.  It does
write a text file though.  To see these files we have to use type on a PC ( but
it would be cat for Mac or Linux).
"""
import sys

infile = sys.argv[1]
outfile = sys.argv[2]

text_file = open(infile)
length_file = open(outfile, 'w')

for line in text_file:
    line = line.strip("\n")
    ct = len(line)
    length_file.write(str(ct)+ '\n')
text_file.close()
length_file.close()