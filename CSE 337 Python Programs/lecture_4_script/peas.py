f = open("peas.txt")
line = f.readline()
while line:
   print(line.swapcase()) # lowercase becomes uppercase, and vice-versa
   line = f.readline()
f.close()

f = open("peas.txt")
line = f.readline()
while line:
   line = line.rstrip()  # Return a copy of the string with trailing white spaces removed
   lst = list(line)
   lst.reverse()
   print(''.join(lst))
   line =(f.readline())
f.close()

# Reverses the order of strings in the original file
f = open("peas.txt")
fout = open("peas2.txt", "w")
lst = f.readlines()
lst.reverse()
for x in lst:
   fout.write(x)
fout.close()
f.close()

f = open("peas.txt")
fout = open("peas3.txt", "w")
lst = f.readlines()
lst.sort()
fout.writelines(lst)
fout.close()
f.close()
print()


