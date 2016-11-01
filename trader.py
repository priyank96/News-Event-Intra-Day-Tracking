from __future__ import division 
from time import sleep
from datetime import datetime, time
from BSEQuote import getPrice
from EntityClass import Entity
from logger import logger
import pickle
        
         
            
        

if __name__ == "__main__":
    
    while datetime.now().second != 59:
        continue
    
    entities = [Entity('530019'),Entity('532296'),Entity('500086'),Entity('500228'),Entity('500875')]
    tradeLog= {entity.ID : [] for entity in entities}
        
    while datetime.now().time()<time(15,30):
        if datetime.now().time()>time(9,14):
            for i in entities:
                i.updateValues()
                if i.cornerPoint<0 and i.holdState==0 and i.prevDayDelta[-1]>0:
                    i.holdState =-1
                    i.trade.append(i.priceList[-1])
                    print (i.trade[0])
                    tradeLog[i.ID].append(i.priceList[-1])

                if i.holdState==-1  and ((i.trade[0]-i.priceList[-1])/i.priceList[-1])>0.0040 :       
                    i.holdState = 1
                    tradeLog[i.ID].append(i.priceList[-1])
                    print((i.trade[0]-i.priceList[-1])/i.priceList[-1])
                    
                if(i.holdState==1):                  #change back to 5
                    entities.remove(i)
                    if len(entities)==0:
                        break

                print(i)
                with open('TradeLog.p','wb') as handle:
                    pickle.dump(tradeLog,handle)
                logger(tradeLog)
                
          
        else:
            print ("waiting "+str(datetime.now().time()))   

        sleep(60)
                #if i.holdState == 1 and i.cornerPoint>0:
                #    i.holdState = 2
                #    i.trade.append(i.priceList[-1])
                #    print (i.trade[1])
                #    tradeLog[i.ID].append(i.priceList[-1])


                #if i.holdState == 2  and i.cornerPoint<0 and ((i.priceList[-1]-i.trade[1])/i.trade[1])>0.0030 :
                #    i.holdState = 5
                #    tradeLog[i.ID].append(i.priceList[-1])

    
    print("here")
       
        
