"""
Working dir should be set to project root.
"""

# with is like try with resources - file will be closed as in finally section
with open('temp/temp.txt', 'w', encoding='utf8') as file:
    sentence = 'The content of file\nąśżźćńłóę\npolskie litery'
    file.write(sentence)  # default encoding is platform dependent (cp1250)

print('File is closed:', file.closed)

print('Content of the file:')
with open('temp/temp.txt', encoding='utf8') as file:
    for line in file:  # readline() is used for iteration
        print(line, end='')
