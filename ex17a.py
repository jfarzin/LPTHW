from sys import argv
#this line no longer needed:
#from os.path import exists

script, from_file, to_file = argv

#indata = open(from_file).read()

#combine these two lines to the third line (and eliminate close at end)
#out_file = open(to_file, 'w')
#out_file.write(indata)
#open(to_file, 'w').write(indata)

#combine indata line and prior line to this line:
open(to_file, 'w').write(open(from_file).read())

#out_file.close()
print("All done.")