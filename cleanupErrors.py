newFile=open("definitions.txt","r")
newFile2=open("corrected.txt","w")

getLines=newFile.readlines()

knownDupes=[12,218,558,602,653,685,825,1016,1068,1121,1125]
replacements={}

wordstoreplace= [
    "6 bitter, pungent, sharp, sour",
    "33 be dry",
    "74 stench",
    "104 relating to the wrist",
    "115 empty",
    "142 curl,tentacle",
    "158 neck",
    "190 lie",
    "397 hour",
    "460 send",
    "493 stay",
    "495 hand",
    "525 less,smaller",
    "579 ninth",
    "586 new",
    "610 hate",
    "641 choose",
    "694 foot",
    "734 pine",
    "741 calm",
    "788 carry",
    "807 for,forward",
    "943 six each",
    "946 seven",
    "955 late",
    "984 comfort,soothe",
    "985 alone,lonely",
    "1074 complete",
    "1155 urine",
    "1172 hunt",
    "1200 green",
    "1210 wish"]

for word in wordstoreplace:
    word=word.split(" ")
    k=int(word[0])-1
    body=word[1:]
    body=" ".join(body)
    
    replacements[k]=body
    
linesList=[]
i=-1
l=1

for line in getLines:
    linesList.append(line)
    
for line in linesList:
    if linesList.index(line) != 0:
        line=line.replace("\n","")
        
        if linesList[i+1]==linesList[i]:
            if (i+1) not in knownDupes:

                newFile2.write(str(l)+" "+replacements[i+1]+"\n")
            else:
                newFile2.write(str(l)+" "+line+"\n")
            
        else:
            newFile2.write(str(l)+" "+line+"\n")
            
    else:
        line=line.replace("\n","")
        newFile2.write(str(l)+" "+line+"\n")
        
    l+=1
    i+=1
