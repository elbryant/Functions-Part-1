#import arguments
from sys import argv

#2 arguments, using script and an input file
script, input_file = argv

#create  file called print all that takes an input f
def print_all(f):
    #print out f in read
    print f.read()
    
#create a file called rewind    
def rewind(f):
    #return to the beginning
    f.seek(0)
    
#create a function print_a_line that takes in line count and f
def print_a_line(line_count, f):
    #print the line count and a line from f
    print line_count, f.readline()
    
#set variable current file to open the input_file
current_file = open(input_file)

print "First let's print the whole file:\n"
#use print all the print the current file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#rewind to the beginning of the current file
rewind(current_file)

print "Let's print three lines:"

#set current line equal to 1
current_line = 1
#call function print_a_line and input the current line number from the current file
print_a_line(current_line, current_file)
#current line is 1

current_line = current_line + 1
#call function print_a_line and take the current line number of 1 and add 1
print_a_line(current_line, current_file)
#current line is 2

current_line = current_line + 1
#call function print_a_line and take the current line number of 2 and add 1
print_a_line(current_line, current_file)
#current line is 3