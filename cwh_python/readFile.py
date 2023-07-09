
#specifying the file and code to read ie.r
f=open('sample.txt','r')

#fetching the data...use open() function to read the content of a file
data=f.read()

#displaying the data
print(data)

#closing the file
f.close()