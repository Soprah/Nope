class Card:

    def __init__(self, color_amount, color):
        allowed_colors = ("red", "blue", "green", "yellow",)
        if not isinstance(color, tuple):
            color = (color,)

        if len(color) != color_amount:
            raise ValueError(f"Expected {color_amount} colors, got {len(color)}")

        self.color_amount = color_amount

        for c in color:
            if c not in allowed_colors:
                raise ValueError(f"Invalid color: {c}")

        self.color = color