from random import shuffle

# global variable
cards = {'1':10,'A': 11,'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'J': 10, 'Q': 10, 'K': 10}



class Blackjack():
    def __init__(self,name='',dealer=False):
        self.dealer = False
        self.name = name
        self.hand = []
        self.bust = False
        self.soft17 = False
        self.point = 0
        self.blackjack = False
        if len(deck) != 52:
            raise ValueError("At the start of the game, the entire deck doesn't have 52 cards.")

    def hit(self):
        self.hand.append(deck.pop())
        self.score()
        
    def score(self):
        points = 0
        ace_counter = 0
        ace_flag = False

        for i in self.hand:
            points = points + cards[i[0][0]]
            if i in ['A♤', 'A♡', 'A♧', 'A♢']:
                ace_flag = True
                ace_counter += 1
        while ace_counter > 0 and points > 21:
            points -= 10
            ace_counter -= 1

        self.point = points
        self.bust = self.point > 21
        self.soft17 = (self.point == 17 and ace_flag == True)
        self.blackjack = (self.point == 21 and ace_flag == True)



# create a deck of cards
faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', "J", "Q", "K"]
suits = ['♤', '♡', '♧', '♢']
deck = []
for suit in suits:
    for face in faces:
        deck.append(face + suit)

shuffle(deck)

# init player and dealer
def player_init(player_name=['player1']):
    player = {}
    for index,name in enumerate(player_name,1):
        player[index]=Blackjack(name=name)
    return player

player = player_init(['josh','alvin','chris'])
dealer = Blackjack(name='dealer',dealer=True)

# deal card to player
for key in player:
    player[key].hit()
    print(player[key].name,'\t',player[key].hand,'\t',player[key].point)

# deal card to dealer
dealer.hit()
print(dealer.name,'\t',dealer.hand,'\t',dealer.point)

# deal card to player
for key in player:
    player[key].hit()
    print(player[key].name,'\t',player[key].hand,'\t',player[key].point)

# deal card to dealer
dealer.hit()
print(dealer.name,'\t',dealer.hand,'\t',dealer.point)

