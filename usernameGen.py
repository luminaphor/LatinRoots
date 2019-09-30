import random

run=True

print("Type 'Done' to exit the program.")
print("Type fav1,fav2, or both to add either root word to your favorites.")
#print("Your favorite root words will be used more frequently.")

#perbyWeight:
#   favorite.append(thing)
#   mainlist
#   for all stuff in mainlist:
#       if stuff in favorite:
#           stuff=stuff*(weightedpercent)
#   make random choice.

while run:
    roots=open("rootsList.txt","r")
    defs=open("corrected.txt","r")
    newFile3=open('compare.txt','w')

    rootsDict={}
    rootsList=[]
    defsList=[]
    rootsDef={}
    favorites=[]
    i=0

    for line in roots:
        newRoot=line.replace("\n","")
        rootsList.append(newRoot)
        
    for line in defs:
        newDef=line.replace("\n","")
        splitDef=newDef.split(" ")
        newDef=splitDef[1:]
        newDef=" ".join(newDef)
        
        defsList.append(newDef)

    for _ in range(len(rootsList)):
        rootsDef[rootsList[_]]=defsList[_]

  #  for root in rootsList:
  #      if root in favorites:
  #          root=root
            
    def getUserName(rootsList,defsList):
        blank=""
        
        ch=random.sample(rootsList,2) #pick 2 random roots, puts them in a list
        c1=ch[0] #separates this list into two separate strings
        c2=ch[1]

        d1=defsList[c1] #finds the definitions that corresponds to each root in the definitions list
        d2=defsList[c2]
        
        meaning=[d1,d2] #assigns variable "meaning" so we can display the meaning behind each root word
        
        c1=c1.replace("-",blank)
        c2=c2.replace("-",blank)
        
        print("Your root words were: {} and {}".format(c1,c2))
        print("Meaning: {} and {}".format(d1,d2))
        print("\nYour potential usernames are: \n")
        
        username=[]
     
        if "," in c1:
            c1=c1.split(",")
            
        if "," in c2:
            c2=c2.split(",")
        
        try:
            if isinstance(c1,str) and isinstance(c2,str):
                username.append(c1+c2)
                username.append(c2+c1)
            else:
                raise
            
        except:
            if isinstance(c1,list) and isinstance(c2,list):
                for c in c1:
                    for cn in c2:
                        username.append(c+cn)
                        username.append(cn+c)
                        
            if isinstance(c1,list) and isinstance(c2,str):
                for c in c1:
                    username.append(c+c2)
                    username.append(c2+c)
                    
            if isinstance(c1,str) and isinstance(c2,list):
                for nc in c2:
                    username.append(c1+nc)
                    username.append(nc+c1)

        for name in username:
            if " " in name:
                name=name.replace(" ","")
            print(name)

    getUserName(rootsList,rootsDef)
    cont=input(" ")
    if cont=='fav1':
        favorites.append(c1)
    elif cont=='fav2':
        favorites.append(c2)
    elif cont=='both':
        favorites.append(c1)
        favorites.append(c2)
        
    elif cont=='Done':
        run=False

exit=input("\nExit on click")
        