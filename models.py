import random
import names

COLORS = ['♡', '♤', '♧', '♢']
VALUES = {
    '2': 15,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'V': 11,
    'D': 12,
    'R': 13,
    'A': 14
}


class Deck:
    """ Deck du jeu de société du Président. """

    def __init__(self):
        self.__cards: list = []
        """ Génération d'un deck de 52 cartes"""
        for (symbol, val) in VALUES.items():
            for color in COLORS:
                new_card = Card(symbol, color)
                self.__cards.append(new_card)

    def shuffle(self) -> None:
        """ Mélanger les cartes de mon deck. """
        random.shuffle(self.__cards)

    def pick_card(self):
        return self.cards.pop(0)

    def __str__(self) -> str:
        return str(self.__cards)

    @property
    def cards(self):
        return self.__cards


class Card:
    __symbol: str
    __value: int
    __color: str

    def __init__(self, symbol: str, color: str):
        """
            Card Constructor.
            attrs:
                symbol: One of the VALUES keys.
                color:  One of the  COLORS values.
        """

        self.__symbol = symbol
        self.__value = VALUES[symbol]
        self.__color = color

    def __lt__(self, other):
        return self.__value < other.value

    def __gt__(self, other):
        return self.__value > other.value

    def __eq__(self, other):
        return self.__value == other.value

    def __ne__(self, other):
        return self.__value != other.value

    def __ge__(self, other):
        return self.__value >= other.value

    @property
    def value(self):
        return self.__value

    @property
    def symbol(self):
        return self.__symbol

    def __repr__(self):
        return f"{self.__symbol} {self.__color}"


class Player:
    president = False

    def __init__(self, player_name=None):
        self._name: str = player_name if player_name is not None else \
            names.get_first_name()
        self._hand: list = []

    def add_to_hand(self, card: Card):
        self._hand.append(card)
        self._hand.sort()

    def remove_from_hand(self, cards: list):
        for c in cards:
            self._hand.remove(c)

    @property
    def hand(self):
        return self._hand

    @property
    def name(self):
        return self._name

    def play(self, plays) -> list:
        """
        Remove from the hand of the player, all cards having a corresponding symbol.
        Args:
            symbol: The symbol to look for.
        Returns: The cards removed from the hand of the player. It will return an empty array if
        nothing is found.
        """
        cards_played = []

        choice_value = 0
        choice = None
        nb_cards = None
        if plays is None:
            while choice == None:
                choice = input('What value do you wish to play ? ')
                print(choice)
                if choice != "0":
                    if self.has_symbol(choice) > 1:
                        while not type(nb_cards) == int:
                            nb_cards = input("nombre de carte jouer ?")
                            try:
                                nb_cards = int(nb_cards)
                            except:
                                pass
                    elif self.has_symbol(choice) < 1:
                        choice = None
                    else:
                        nb_cards = 1
        if plays is not None:
            nb_cards = len(plays)

            while (choice_value < plays[0].value or nb_cards > self.has_symbol(choice)) and choice != "0":
                choice = input('What value do you wish to play ? ')
                try:
                    choice_value = VALUES[choice]
                except:
                    pass

        if choice != "0":
            cards_available = [card for card in self._hand if card.symbol == choice]
            for i in range(nb_cards):
                cards_played.append(cards_available.pop(0))
            print(cards_played)
            self.remove_from_hand(cards_played)
        else:
            cards_played = []
        return cards_played

    def __repr__(self):
        return f"{self.name}\t: {self.hand}"

    def has_symbol(self, card_symbol) -> int:
        nb_cards = 0
        for card in self._hand:
            if card.symbol == card_symbol:
                nb_cards += 1
        return nb_cards

    def infer(x, y):
        while x < y:
            print("vous ne pouvez pas jouer une carte inférieure à la carte précedente")
            return False
        else:
            return True


def win(best_choice):
    if best_choice is None:
        print("je n'ai plus de carte pour pouvoir rivaliser à ton grand pouvoir")
        return False


def winn(variab):
    compt = 0
    if variab is None:
        print("je suis la ")
        return True


class AIPlayer(Player):

    def play(self, choice, nb_cards: int) -> list:
        """
        Play a card correspondig to what has been played on the table.
        TODO: Implement an AI
        Args:
            choice: The minimum card value to play.
            nb_cards: The number of cards to play.
        Returns: An array of cards to play.
        """
        best_choice = None
        if choice is None or choice == 0:
            nb_cards = 0
            for card in self.hand:
                if nb_cards < self.has_symbol(card.symbol):
                    nb_cards = self.has_symbol(card.symbol)
                    choice = card.symbol

        for index, card in enumerate(self.hand):
            if best_choice is None and card.value >= int(VALUES[choice]) and \
                    self.has_symbol(card.symbol) >= \
                    nb_cards:
                cards_played = self._hand[index:index + nb_cards]
                best_choice = card.symbol
                self.remove_from_hand(cards_played)
        return cards_played if best_choice is not None else []


class PresidentGame:
    president = None
    trouduc = None
    def __init__(self, nb_players):
        self.__generate_players(nb_players)
        self.distribute_cards()
        self.round = 0

    def __generate_players(self, nb_players):
        self.__players = [Player()]
        for _ in range(nb_players - 1):
            self.__players.append(AIPlayer())

    def __generate_cards(self):
        self.__deck = Deck()
        self.__deck.shuffle()

    def distribute_cards(self):
        self.__generate_cards()
        giving_card_to_player = 0
        nb_players = len(self.__players)
        while len(self.__deck.cards) > 0:
            card = self.__deck.pick_card()
            self.__players[giving_card_to_player].add_to_hand(card)
            giving_card_to_player = (giving_card_to_player + 1) % nb_players
    @property
    def players(self):
        return self.__players

    @property
    def ai_players(self):
        return self.__players[1:]

    @property
    def main_player(self):
        """ Main player is player 0 """
        return self.__players[0]
