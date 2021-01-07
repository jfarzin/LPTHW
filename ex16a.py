from sys import argv

script, filename = argv

txt = open(filename)
print(f"Now we can read our new file {filename}:")
print(txt.read())
txt.close()
