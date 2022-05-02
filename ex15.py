#gets argv module from sys package
from sys import argv
#use argv to get a file name
script, filename = argv

txt = open(filename) #new command, open

print(f"Here's your file {filename}:") #nalagay yung filename
print(txt.read()) #call a function on txt named read, niread file

print("Type the filename again:") #pinapatype uli filename
file_again = input("> ") #parang yung sa prompt, string

txt_again = open(file_again) #type uli file para maopen

print(txt_again.read()) #iriread uli siya
