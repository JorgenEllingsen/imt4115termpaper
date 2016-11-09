read = open('b.txt','r')
write = open('res.txt','w')
for line in read:
       if 'Warning--' in line:
           x = line.replace('Warning', '\n Warning')
           write.write(x)
