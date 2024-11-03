class Stone:
    def __init__(self, stone_type: str):
        if stone_type not in ('+', '-', 'f'):
            raise ValueError("stone_type must be '+', '-', or 'f'")
        self.stone_type = stone_type

    def __str__(self):
        return f"Stone(type={self.stone_type})"