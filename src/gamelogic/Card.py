class Card:

    def __init__(self, color):
        allowed_colors = ("red", "blue", "green", "yellow",)

        for c in color:
            if c not in allowed_colors:
                raise ValueError(f"Invalid color: {c}")

        self.color = color