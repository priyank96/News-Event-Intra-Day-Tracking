''' runs news_op and headlines_ndtv, positive headlines are available, creates trading entities of companies appearing in
    positive headlines'''
from words import listed
from EntityClass import *

import news_op


def headline_to_symbol():
    with open("calls(ndtv).txt", 'r') as fil:
        headlines = (fil.read().strip().splitlines())
    entities = []
    companies = []

    # re work this logic, it doesn't work. refer to scrubber
    for hl in headlines:
        for company in listed.keys():
            if company+' ' in hl:
                #print(hl)
                companies.append((listed[company]," ".join(hl.split())))



    for company in companies:
        #print(company)
        entities.append(EntityClass(company[0],company[1]))

    return set(entities)


if __name__ == '__main__':
    for entity in headline_to_symbol():
        print(entity.id)
