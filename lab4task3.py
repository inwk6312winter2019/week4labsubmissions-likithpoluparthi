import string
count=0
d=dict()
d1=dict()
fin=open("book1.txt")
fin2=open("words.txt")
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
#print(count)
#print(d)
for line in fin2:
  line1=line.strip()
  line1=line.lower()
  line1=line.split()
  print(line1)
  for word in line1:
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
for k in d.keys():
  if d[k]>20:
    print(k)
for k in d1.keys():
  if d1[k]>20:
    print(k)




