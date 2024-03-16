#  input format:
#  >>> countCardsA countCardsB changes
#  >>> N elements ai, where 1<=ai<=10^9
#  >>> N elements bj, where 1<=bj<=10^9
#  ...
#  Q lines next format:
#  >>>  type, player, card, where type∈(1, -1), player∈(A, B), 1<=card<=10^9

#  Case 1
#  3 3 5
#  1000 2000 1001
#  1001 2001 1000
#  1 A 100000
#  -1 B 2001
#  1 B 2000
#  1 B 100001
#  1 A 1
#
#  output: 3 2 1 2 3
from typing import NamedTuple, Literal
from queue import Queue


class Action(NamedTuple):
    type: Literal[1, -1]
    player: Literal["A", "B"]
    card: int


class CardCollection:
    def __init__(self, input_str: str, limit: int):
        self.cards_collection = {}
        self.__get_collections_from_input(input_str, limit)

    @property
    def cards(self):
        return self.cards_collection.keys()

    def add_card(self, card: int) -> None:
        self.cards_collection[card] = self.cards_collection.get(card, 0) + 1

    def remove_card(self, card: int) -> None:
        if self.cards_collection[card] > 1:
            self.cards_collection[card] -= 1
        else:
            del self.cards_collection[card]

    def __get_collections_from_input(self, input_string: str, limit: int):
        collections = tuple(map(int, input_string.split()))
        if len(collections) != limit:
            raise ValueError("Invalid input")
        self.cards_collection = {}
        for card in collections:
            self.cards_collection[card] = self.cards_collection.get(card, 0) + 1


def get_action_from_input(input_string: str) -> Action:
    _type, player, card = input_string.split()
    return Action(int(_type), player, int(card))


if __name__ == "__main__":
    count_cards_A, count_cards_B, changes = map(int, input().split())
    collection_A = CardCollection(input(), count_cards_A)
    collection_B = CardCollection(input(), count_cards_B)

    actions = Queue()

    for _ in range(changes):
        action = get_action_from_input(input())
        actions.put(action)

    while not actions.empty():
        action = actions.get()
        player_collection = collection_A if action.player == "A" else collection_B
        match action.type:
            case -1:
                player_collection.remove_card(action.card)
            case 1:
                player_collection.add_card(action.card)
            case _:
                raise ValueError(f"Invalid action type")
        print(len(set(collection_A.cards) ^ set(collection_B.cards)), end=" ")

    #  O(N)
