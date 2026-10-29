from filhandling import openFile, createFileAppend

filename = "learning_python.txt"
file = openFile(filename)
for line in file:
    newline = line.replace("python", "java")
    createFileAppend("learning_python_replace.txt", newline)
file.close()
