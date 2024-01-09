from random import shuffle

from card import Card

class Osmosis:
    SIMPLE: int         = 0
    TRICKY: int         = 1
    CHALLENGING: int    = 2

    SUCCESS: str        = "Success!"
    COMPLICATION: str   = "Complication..."
    OVERSIGHT: str      = "Oversight..."
    CATASTROPHE: str    = "Catastrophe!"
    INTERRUPTION: str   = "Interruption!"

    OUTCOMES_LOW: list[str]     = [COMPLICATION,    OVERSIGHT,      CATASTROPHE]
    OUTCOMES_MED: list[str]     = [SUCCESS,         COMPLICATION,   OVERSIGHT]
    OUTCOMES_HIGH: list[str]    = [SUCCESS,         SUCCESS,        COMPLICATION]

    def __init__(self) -> None:
        # Generate all the cards
        self.stock: list[Card]
        self.faces: list[Card]
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
        for _ in range(12):
            self.stock.pop(0)

        # Determine number of players, then initialize grips
        self.playerCount = int(input("How many players? (Enter number and press [Enter])\n"))
        self.grips: list[list[Card]] = [[] for _ in range(self.playerCount)]

    def drawCard(self) -> None:
        print("Which player is drawing?")
        player: int = None
        try:
            player = int(input("Enter the player's number:\n")) - 1
        except:
            print("Draw canceled.")
            return
            
        print("How challenging is the task?")
        answer = int(input("Simple: [1]; Tricky: [2]; Challenging: [3]; Cancel: press [Enter]\n"))
        difficulty = None
        match answer:
            case 1:
                difficulty = Osmosis.SIMPLE
            case 2:
                difficulty = Osmosis.TRICKY
            case 3:
                difficulty = Osmosis.CHALLENGING
            case _:
                print("Draw canceled.")
                return

        print("What are we drawing from: exuvia or stock?")
        answer = int(input("Exuvia: [1], [2], or [3]; Stock: [4]; Cancel: press [Enter]\n"))
        card: Card = None
        match answer:
            case 1:
                if len(self.exuviae[0]) < 1:
                    print("Exuvia empty, draw canceled.")
                    return
                card = self.exuviae[0].pop(0)
            case 2:
                if len(self.exuviae[1]) < 1:
                    print("Exuvia empty, draw canceled.")
                    return
                card = self.exuviae[1].pop(0)
            case 3:
                if len(self.exuviae[2]) < 1:
                    print("Exuvia empty, draw canceled.")
                    return
                card = self.exuviae[2].pop(0)
            case 4:
                # TODO: if stock is empty, dead end
                card = self.stock.pop(0)
            case _:
                print("Draw canceled.")
                return
        
        outcome: str = Osmosis.determineDrawOutcome(card, difficulty)
        print("You drew: " + str(card))
        print("Outcome: " + outcome)

        self.grips[player].insert(0, card)
        # TODO: handle dead end when two face cards are stacked

    def handleDeadEnd(self) -> None:
        print("The characters have reached a dead end! Re-dealing...")
        for grip in self.grips:
            for card in grip:
                if card.value in [10, 11, 12]:
                    continue
                self.stock.append(card)
        self.grips = [[] for _ in range(self.playerCount)]

        for exuvia in self.exuviae:
            for card in exuvia:
                self.stock.append(card)
        
        shuffle(self.stock)

        self.exuviae = [self.stock[0:4], self.stock[4:8], self.stock[8:12]]
        for _ in range(12):
            self.stock.pop(0)


    def determineDrawOutcome(card: Card, difficulty: int) -> str:
        value = card.value
        match value:
            case 1 | 2 | 3: # 2, 3, 4
                return Osmosis.OUTCOMES_LOW[difficulty]
            case 4 | 5 | 6: # 5, 6, 7
                return Osmosis.OUTCOMES_MED[difficulty]
            case 7 | 8 | 9: # 8, 9, 10
                return Osmosis.OUTCOMES_HIGH[difficulty]
            case 0: # A
                return Osmosis.SUCCESS
            case _: # face card
                return Osmosis.INTERRUPTION

    def determineVictory(self) -> bool:
        truths = 0
        for i in range(4):
            truths += (len(self.conspiracy[i]) + 2) // 3
        return truths >= self.playerCount * 4

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
    while(True):
        osmosis.status()
        osmosis.drawCard()
        keepGoing = input("Type 'exit' to exit, 'de' for dead end, anything else will continue: ")
        if keepGoing == "exit":
            break
        if keepGoing == "de":
            osmosis.handleDeadEnd()
        print()
        print()