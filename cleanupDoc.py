fileObject=open('greek_and_latin_roots2.txt','r') #opens the greek_and_latin_roots2.txt file

newFile=open('rootsList.txt','w')
newFile2=open('definitions.txt','w') #create two new text files, one for the list of roots and the other for the definitions

filenew=fileObject.readlines() #read each line separately from the source text document

for line in filenew: 
    getIndex=filenew.index(line) #get the index of that line specifically
    line=line.replace('\n','') #for each generated line, replace the newline character with empty space
    
    if len(line)>1: #if the line has a length greater than 1 characters
        if line[-1]=='-': #if the line ends in a dash
            newFile.write(line+"\n") #its a root and you should write it to the roots.txt file
            
            newFile2.write(filenew[getIndex+1]) #uses the index of the current line, adds 1, then grabs that line. Writes it to the defs file.
            #this is the pattern that shows up in the original source file with the definitions and root words
            #so this may be subject to change 


exit=input("Exit on click.")

