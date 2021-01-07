#import sys
#script, input_encoding, error = sys.argv

for_encoding = "utf-8"
error_handling = "strict"

def check_line(file, enc, erhandle):
    byte_line = file.readline().strip()
    if byte_line:
        show_me(byte_line, for_encoding, error_handling)
        check_line(languages, for_encoding, error_handling)

def show_me(byte_line_var, enc, erhandle):
    print(">>byte line:", byte_line_var)
    edit_byte = byte_line_var[:-4]
    print(">>edited byte:", edit_byte)
    strline = byte_line_var.decode(enc, erhandle)
    print(">>string line:", strline)
        

languages = open("lang.txt", mode = "rb")
check_line(languages, for_encoding, error_handling)


#byte_line = languages.readline().strip()
#if byte_line:
#    print(">>there is a byte line:", byte_line)
#    strline = byte_line.decode(enc, erhandle)
#    print(">>should be a string line:", strline)
