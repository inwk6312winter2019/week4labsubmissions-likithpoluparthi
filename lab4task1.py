import string
fin=open("book1.txt")
for line in fin:
  line=line.strip()
  line=line.lower()
  line=line.split()
  for word in line:
    print(word.strip(string.punctuation))
