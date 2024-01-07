from random import shuffle

from card import Card

class Osmosis:
    def __init__(self) -> None:
        # Generate all the cards
        self.stock, self.faces = Card.deck()
        shuffle(self.stock)

        # Begin the conspiracy and shuffle first interruptions in
        top: Card = self.stock.pop(0)
        self.conspiracy: list[list[Card]] = [[top], [], [], []]

        firstFaces: list[Card] = self.faces[top.suit*3 : top.suit*3 + 3]
        for firstFace in firstFaces:
            self.stock.append(firstFace)
            self.faces.remove(firstFace)
        shuffle(self.stock)

        # Deal the exuviae
        self.exuviae: list[list[Card]] = [self.stock[0:4], self.stock[4:8], self.stock[8:12]]
        for i in range(12):
            self.stock.pop(0)

        # Determine number of grips
        number = int(input("How many players? (Enter number and press [ENTER])\n"))
        self.grips = [[]] * number

    def status(self) -> None:
        print("stock")
        for i in self.stock:
            print(str(i), end=" ")
        print(f"{len(self.stock)} cards"); print()

        print("faces")            
        for i in self.faces:
            print(str(i), end=" ")
        print(); print()

        print("conspiracy")
        for pile in self.conspiracy:
            if len(pile) == 0:
                print("<empty>")
            else:
                for card in pile:
                    print(str(card), end=" ")
                print()
        print()

        print("exuviae")
        for exuvia in self.exuviae:
            if len(exuvia) == 0:
                print("<empty>")
            else:
                for card in exuvia:
                    print(str(card), end=" ")
                print()
        print()

        print("grips")
        for grip in self.grips:
            if len(grip) == 0:
                print("<empty>")
            else:
                for card in grip:
                    print(str(card), end=" ")
                print()
        print()
        


# for testing purposes
if __name__ == "__main__":
    osmosis = Osmosis()
    osmosis.status()