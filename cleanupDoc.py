fileObject=open('greek_and_latin_roots2.txt','r')

newFile=open('rootsList.txt','w')
newFile2=open('definitions.txt','w')

filenew=fileObject.readlines()

for line in filenew:
    getIndex=filenew.index(line)
    line=line.replace('\n','')
    
    if len(line)>1:
        if line[-1]=='-':
            newFile.write(line+"\n")
            
            newFile2.write(filenew[getIndex+1])


exit=input("Exit on click.")

