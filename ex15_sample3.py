print("Type the file name")
filename = input("> ")

txt = open(filename) #opens the file and assigns the text to txt

print(f"Here's your file {filename}:") #prints file name
print(txt.read())

print("Type the filename again:")
file_again = input(">")   #takes file name as input from the user

txt_again = open(file_again) #opens the file again and assigns the text to txt_again

print(txt_again.read())   #prints the text from txt_again
