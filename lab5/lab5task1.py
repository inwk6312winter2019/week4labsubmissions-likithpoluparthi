import string
file1 = open("58820-0.txt")
for line in file1:
    line = line.strip()
    line = line.lower()
    line = line.split()
    for word in line:
       print(word.strip(string.punctuation))
