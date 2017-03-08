import os.path
import csv
from BSEQuote import get_price

class EntityClass:
    __slots__ = ['id', 'file_name','start']

    def __init__(self, symbol):
        self.id = symbol
        self.file_name = "PastTrades/" + self.id + '.csv'
        file_count = 0
        while os.path.isfile(self.file_name):
            self.file_name = "PastTrades/" + self.id + str(file_count) + '.csv'
            file_count += 1
        with open(self.file_name, 'w'):
            pass

    def update_values(self):
        with open(self.file_name,'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            row = get_price(self.id)
            writer.writerow(row)

if __name__ == '__main__':
    sample_entity = EntityClass('500570')
    sample_entity.update_values()
    sample_entity.update_values()
