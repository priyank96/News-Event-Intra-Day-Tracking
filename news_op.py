'''picks the positive headlines from the scrubbed headlines'''
from scrubber import scrubber
import headlines_ndtv

f=open("headlines(ndtv).txt",'r')

h=open("calls(ndtv).txt",'w')
hl=' '
while hl!="end":

        
        if(',' in hl):      #space for commas
                hl=hl.replace(',',' ,',7)
        if("'" in hl):      #space for apostrophes
                hl=hl.replace("'","",7)    
        hl=hl.split(' ')
        #print(hl)
        score=scrubber(hl[:-1])
        if(score>0):
                 h.write(' '.join(hl)+'\n')
                #h.write('score: '+str(score)+'\n\n')
         #print(score)
        hl=f.readline().lower()

        
h.close()
#print(f.read())

f.close()
print("Done- news_op")

        
if __name__=='__main__':
        with open("calls(ndtv).txt",'r') as f:
                print(f.read())
        

        
       
    
	
