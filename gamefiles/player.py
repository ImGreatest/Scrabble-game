class Player:
    def __init__(self):
        self.score = 0
        self.count_layout_letters = 0

    def change_score(self, value: int) -> int:
        self.score += value
        return self.score

    def layout_letter(self):
        self.count_layout_letters += 1
        return self.count_layout_letters
