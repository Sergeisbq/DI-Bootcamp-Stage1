import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        pass

    def show(self):
        print('{} of {}'.format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for i in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for j in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']:
                self.cards.append(Card(i, j))

    def show(self):
        for i in self.cards:
            i.show()

    def shuffle(self):
        for i in range(len(self.cards) -1, 0, -1):
            j = random.randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def deal(self):
        i = self.cards.pop()
        return i
    
deck = Deck()
deck.shuffle()
card = deck.deal()
card.show()
print('-------------')
deck.show()
print(len(deck.cards))
card = deck.deal()
card.show()
print('-------------')
deck.show()
print(len(deck.cards))
card = deck.deal()
card.show()
print('-------------')
deck.show()
print(len(deck.cards))

