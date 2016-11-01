from scrubber import scrubber, re_list
import headlines_ndtv
choice=0
f=open("headlines(ndtv).txt",'r')

h=open("calls(ndtv).txt",'w')
hl=' '
while hl!="end":
        print(hl)
        if(',' in hl):      #space for commas
                hl=hl.replace(',',' ,',7)
        if("'" in hl):      #space for apostrophes
                hl=hl.replace("'"," '",7)    
        hl=hl.split(' ')
        score=scrubber(hl[:-1])
        if(score>0):
                h.write(' '.join(hl)+'\n')
                h.write('score: '+str(score)+'\n\n')
        #print(score)
        hl=f.readline().lower()
f.close()
h.close()
with open("calls(ndtv).txt",'r') as f:
        print(f.read())
        

        
       
    
	
