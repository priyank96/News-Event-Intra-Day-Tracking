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
    for hl in headlines:
        for company in listed.keys():
            if company in hl:
                #print(hl)
                companies.append(listed[company])

    for company in list(set(companies)):
        print(company)
        entities.append(EntityClass(company))
    return entities


if __name__ == '__main__':
    for entity in headline_to_symbol():
        print(entity.id)
