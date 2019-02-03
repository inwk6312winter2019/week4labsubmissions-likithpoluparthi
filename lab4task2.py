import string
count=0
d=dict()
d1=dict()
fin=open("book1.txt")
fin2=open("book2.txt")
for line in fin:
  line=line.strip()
  line=line.lower()
  line=line.split()
  #print(line)
  for word in line:
    count+=1
    x=(word.strip(string.punctuation))
    #print(x)
    if word not in d:
      d[word]=1
    else:
      d[word]+=1
print(count)
#print(d)
for line in fin2:
  line=line.strip()
  line=line.lower()
  line=line.split()
  #print(line)
  for word in line:
    count+=1
    x=(word.strip(string.punctuation))
    #print(x)
    if word not in d1:
      d1[word]=1
    else:
      d1[word]+=1
print(len(d))
print(len(d1))
if len(d)>len(d1):
  print("first book is extensive than second")
else:
  print("Second book is extensive")
