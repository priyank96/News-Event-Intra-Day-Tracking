
from BSEQuote import get_price

past_trades_file_name = "PastTrades.h5"
class EntityClass:
    __slots__ = ['id', 'line', 'headline']

    def __init__(self, symbol,headline=""):
        self.id = symbol
        self.headline = headline
        self.line = []

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if isinstance(other, EntityClass):
            return self.id == other.id

    def update_values(self):
        row = get_price(self.id)
        self.line.append(row[2])

if __name__ == '__main__':
    sample_entity = EntityClass('500570')
    sample_entity.update_values()
    sample_entity.update_values()
