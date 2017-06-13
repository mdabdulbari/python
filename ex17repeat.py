from sys import argv
from os.path import exists

script, fromfile, tofile = argv
print(f"Copying from {fromfile} to {tofile}.")

infile = open(fromfile)
indata = infile.read()

print(f"Does the output file exist? {exists(tofile)}")
print("Ready, hit RETURN to contunie, CTRL-C to abort")
input()

outfile = open(tofile, 'w')
outfile.write(indata)

print("Alright, all done.")
outfile.close()
infile.close()
