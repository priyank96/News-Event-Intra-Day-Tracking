from words import words
fs=open("words2.txt",'r')
listed=[]
for i in fs:
    listed.append(i[:-1])
fs.close()

def scrubber(ch):
    '''Removes numbers, Cr., crores, q1, etc'''
    temp=[]
    #print(ch,"HERE")
    for i in ch:
      
        for j in range(0,len(i)):
            if i[j].isnumeric():
                break
            if j+1==len(i) and i not in ('crore','cr','rs','rs.','|'):
                temp.append(i) 
        #print(temp)
    return scorer(temp,temp)

def scorer(ch,temp): #listed companies to be added somewhere here
    sc=[]
    global words, listed
    
    for i in ch:
        if i in words.keys():
            sc.append(words[i])
        else:
            sc.append(0)
    
    
    #print("\nNews For: ")
    islisted=False
    for i in range(0,len(ch)-3): #to assign listed company score and print listed company, given 3, to distinguish
            if(ch[i]+' '+ch[i+1]+' '+ch[i+2] in listed):        #breaks after recognizing one company
                sc[i]=3
                #print(ch[i]+' '+ch[i+1]+' '+ch[i+2])
                #print(sc)
                del sc[i+1], sc[i+1]
                i=i+2
                islisted=True
                break

            elif(ch[i]+' '+ch[i+1]+' '+ch[i+2]+' '+ch[i+3] in listed):
                sc[i]=3
                #print(ch[i]+' '+ch[i+1]+' '+ch[i+2]+' '+ch[i+3])
                #print(sc)
                del sc[i+1], sc[i+1],sc[i+1]
                i=i+3
                islisted=True
                break
                
            elif(ch[i]+' '+ch[i+1] in listed):
                sc[i]=3
                #print(ch[i]+' '+ch[i+1])
                del sc[i+1]
                i=i+1
                islisted=True
                break

            elif(ch[i] in listed):
                sc[i]=3
                #print(ch[i])
                islisted=True
                break
    if(islisted==False):
        return -3
        
    
  
    
    return calc(sc,temp)

def calc(ch,temp):  #calculates sentiment score for headline
    start=0
    total=0
    if('but' in temp):
        start=temp.index('but')
        
    p1=100
    p2=100
    t1=0
    t2=0
    v1=0
    v2=0
    for i in range(start,len(ch)):
        #print(total)
        if(ch[i]==1 or ch[i]==-1): #modifier found
            for j in range(i+1,len(ch)): #looks for keywords to the right
                if ch[j]==2 or ch[j]==-2:
                    t1=j
                    p1=j-i
                    v1=ch[i]
                    break
            for j in range(i-1,start-1,-1): #looks for keywords to the left
                if(ch[j]==2 or ch[j]==-2):
                    t2=j
                    p2=i-j
                    v2=ch[i]
                    break
            if(p2<p1 ):             #checks if left or right is closer
                total+=ch[t2]*v2
            elif(p1>p2):
                total+=ch[t1]*v1
            else:                   #if both are equal ,preference to non listed company keyword
                if(ch[t2]<3):
                    total+=ch[t2]*v2
                else:
                    total+=ch[t1]*v1
        if(i+1==len(ch) and total==0):
            total=-3 
            for j in ch:
                total+=j
            
    return total    
            
        
    
