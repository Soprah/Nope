class Card:

    def __init__(self, id, color):
        allowed_colors = ("red", "blue", "green", "yellow",)

        if not isinstance(color, tuple):
            color = (color,)

        if len(color) != len(set(color)):
            raise ValueError("Duplicate colors not allowed")

        for c in color:
            if c not in allowed_colors:
                raise ValueError(f"Invalid color: {c}")

        if len(color) == 1 or len(color) == 2 or len(color) == 4:
            self.color = color
        else:
            raise ValueError("Invalid color amount")

        self.id = id

    def __str__(self):
        return f"ID: {self.id} Anzahl Farben: {len(self.color)} Colors: {self.color}"

    def get_color(self):
        return self.color