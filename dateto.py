filename = input("Input the Filename: ")
f_extns = filename.split(" ")
last_text = f_extns[-1]
char = last_text[len(last_text) - 1]
print(last_text)
print(char)
filename.find(char)
print(filename)
print ("The extension of the file is : " + repr(f_extns[-1]))