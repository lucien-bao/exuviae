class Card:
    SUITS: tuple[str] = ("♣️", "♥️", "♠️", "♦️")
    VALUES: str = "A23456789TJQK"

    """
    Each suit represents a different insect
    theme (life stage/action) in EXUVIAE:
    =======================================
    Suit        Stage       Facet
    ---------------------------------------
    Clubs       Eggs        Waiting
    Hearts      Nymph       Hiding
    Spades      Molting     Revealing
    Diamonds    Adult       Hunting
    """

    """
    Results of actions are determined by its difficulty
    (inherent and as augmented by character's skill) and
    by the value of the card drawn:
    ===============================================
    Value       Simple      Tricky      Challenging
    -----------------------------------------------
    2 3 4    Complication   Oversight   Catastrophe
    5 6 7       Success   Complication  Oversight
    8 9 10      Success     Success    Complication
      A         Success     Success     Success
    J Q K     ! ! ! ! ! ! Interruption ! ! ! ! ! !
    """

    def __init__(self, id: int) -> None:
        self.image          = None # TODO
        self.suit: int      = id // 13
        self.value: int     = id % 13

        # displays only
        # self.frontUp: bool  = False
    
    def __str__(self) -> str:
        return Card.VALUES[self.value] + Card.SUITS[self.suit]

    def deck() -> tuple[list, list]:
        main = []
        faces = []
        for i in range(52):
            if i % 13 >= 10:
                faces.append(Card(i))
            else:
                main.append(Card(i))
        
        return (main, faces)

    # displays only
    # def display(self):
    #     # TODO
    #     pass