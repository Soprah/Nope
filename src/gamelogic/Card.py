class Card:

    def __init__(self, color_amount, color, id):
        allowed_colors = ("red", "blue", "green", "yellow",)

        if not isinstance(color, tuple):
            color = (color,)

        if len(color) != color_amount:
            raise ValueError(f"Expected {color_amount} colors, got {len(color)}")

        self.color_amount = color_amount

        if len(set(color)) != len(color):
            raise ValueError("Duplicate colors not allowed")

        for c in color:
            if c not in allowed_colors:
                raise ValueError(f"Invalid color: {c}")

        if color_amount == 1:
            self.color = color
        elif color_amount == 2:
            self.color = color
        elif color_amount == 4:
            self.color = color
        else:
            raise ValueError("Invalid color amount")

        self.id = id