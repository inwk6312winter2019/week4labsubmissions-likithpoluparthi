import string
fin=open("book1.txt")
fin2=open("words.txt")
line1=list()
line2=list()
for line in fin:
  line=line.strip()
  line=line.lower()
  line=line.split()
  for word in line:
     line1.append(word.strip(string.punctuation))
for line in fin2:
     line2.append(line.strip())
for item in line1:
  if item not in line2:
    print(item)

