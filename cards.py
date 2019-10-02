'''
Return the correct card from a deck. The instructions are: write the function: get_card(deck, suit, rank)

returns the relevant card in the deck suit will be one of ♢♣♡♠ rank will be a number 1 through 13

The assumptions are that: the deck parameter will always be in the A-K and ♢♣♡♠ order
'''



deck = ['A♢', '2♢', '3♢', '4♢', '5♢', '6♢', '7♢', '8♢', '9♢', '10♢', 'J♢', 'Q♢', 'K♢', 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♡', '2♡', '3♡', '4♡', '5♡', '6♡', '7♡', '8♡', '9♡', '10♡', 'J♡', 'Q♡', 'K♡', 'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠']

char_cards = {
  1: 'A',
  11: 'J',
  12: 'Q',
  13: 'K'
}

def get_card(cards, figure, rank):
  card_selector = char_cards.get(rank, rank)
  
  card = f'{card_selector}{figure}'

  if card in cards:
    return card
  else:
    # print('ups your card is not inside the deck')
    return None 

card = get_card(deck, '♡', 12)
print(card) # Q♡