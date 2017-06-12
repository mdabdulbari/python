from sys import argv

script, filename = argv

txt = open(filename) #opens the file and assigns the text to txt

print(f"Here's your file {filename}:") #prints file name
print(txt.read())
