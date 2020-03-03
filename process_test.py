source_file=open('greek_and_latin_roots2.txt','r') #opens the greek_and_latin_roots2.txt file
roots_file=open('roots.txt','w')
defs_file=open('definitions.txt','w') #create two new text files, one for the list of roots and the other for the definitions

source_lines=source_file.readlines() #read each line separately from the source text document
source_file.close()

debug_file=open("debug.txt","w")

i=0
for line in source_lines: 
    line=line.replace('\n','') #for each generated line, replace the newline character with empty space
    
    if len(line)>1 and line[-1]=='-': #if the line ends in a dash
        roots_file.write(line+"\n") #its a root and you should write it to the roots.txt file
        defs_file.write(source_lines[i+1]) #uses the index of the current line, adds 1, then grabs that line. Writes it to the defs file.
            #this is the pattern that shows up in the original source file with the definitions and root words
            #so this may be subject to change 
    i+=1

defs_file.close()
roots_file.close()

defs_file=open("definitions.txt","r")
corrected_defs=open("corrected_definitions.txt","w") #creates new file so we can clean up the original definitions file.

all_defs=defs_file.readlines() #reads in all definitions.
defs_file.close()

knownDupes=[12,218,558,602,653,685,825,1016,1068,1121,1125] #this was found manually,
#by comparing to the original pdf 
#but it is a list of all words appearing twice that
#are meant to appear twice

replacements={} #empty list to fill in replacements

words_to_replace= [ #these are the replacements that are each filled in for the found duplicates
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

for word in words_to_replace: #for each word that appears in the replacement list
    word=word.split(" ") #we split it to get rid of the number on the front
    word_index=int(word[0])-1 #grabs the index for each replacement word
    body=" ".join(word[1:]) #joins any words that are currently separate in the definition
    
    replacements[word_index]=body
    
linesList=[]
i=-1
l=1
line_index=0

print(replacements)
for line in all_defs:
    if line == all_defs[line_index+1]:
        if all_defs.index(line) not in knownDupes:
            print(line_index)
           # corrected_defs.write(str(line_index)+" "+replacements[str(line_index)]+"\n")
        else:
            corrected_defs.write(str(line_index)+" "+line+"\n")
    else:
        corrected_defs.write(str(line_index)+" "+line+"\n")
    line_index+=1
    
"""for line in linesList:
    if linesList.index(line) != 0:
        line=line.replace("\n","")
        
        if linesList[i+1]==linesList[i]:
            if (i+1) not in knownDupes:
                corrected_defs.write(str(l)+" "+replacements[i+l]+"\n")
            else:
                corrected_defs.write(str(l)+" "+line+"\n")
            
        else:
            corrected_defs.write(str(l)+" "+line+"\n")
            
    else:
        line=line.replace("\n","")
        corrected_defs.write(str(l)+" "+line+"\n")
        
    l+=1
    i+=1 """
print("Done")
exit=input("")