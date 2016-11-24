''' runs news_op and headlines_ndtv, positive headlines are available, creates trading entities of companies appearing in
    positive headlines'''
from words import listed
from EntityClass import *
import news_op

def headline_to_symbol() -> object:
    
    
    with open("calls(ndtv).txt",'r') as fil:
        headlines=(fil.read().strip().splitlines())
    entities = []
    
    for hl in headlines:
        for company in listed.keys():
            if company in hl:
                entities.append(Entity(listed[company]))
    for entity in entities:
        print(entity.ID)
    return entities

if __name__=='__main__':
    for entity in headline_to_symbol():
        print(entity.ID)


    
