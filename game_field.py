import random
import logging

LOG = logging.getLogger(__name__)


class GameField:
    def __init__(self):
        generated_field = list(range(16))
        random.shuffle(generated_field)
        self.game_field = [generated_field[0: 4], generated_field[4: 8], generated_field[8: 12], generated_field[12: 16]]
        self.empty_column = 0
        self.empty_row = 0
        self.find_empty_tile()

    def find_empty_tile(self):
        for row_num, row in enumerate(self.game_field):
            for col_num, element in enumerate(row):
                if element == 0:
                    self.empty_row = row_num
                    self.empty_column = col_num

    def validate(self, column, row):
        if (0 > column) or (column > 3):
            logging.info("User want to perform incorrect move")
            return False
        if (0 > row) or (row > 3):
            # return False
            raise RuntimeError("Incorrect move")
        return True

    def up(self):
        new_empty_column = self.empty_column
        new_empty_row = self.empty_row - 1
        if not self.validate(new_empty_column, new_empty_row):
            return
        self.swap(new_empty_column, new_empty_row)

    def down(self):
        new_empty_column = self.empty_column
        new_empty_row = self.empty_row + 1
        if not self.validate(new_empty_column, new_empty_row):
            return
        self.swap(new_empty_column, new_empty_row)

    def swap(self, new_empty_column, new_empty_row):
        self.game_field[self.empty_row][self.empty_column], self.game_field[new_empty_row][new_empty_column] = \
            self.game_field[new_empty_row][
                new_empty_column], self.game_field[self.empty_row][self.empty_column]
        self.empty_row = new_empty_row
        self.empty_column = new_empty_column

    def left(self):
        new_empty_column = self.empty_column - 1
        new_empty_row = self.empty_row
        if not self.validate(new_empty_column, new_empty_row):
            return
        self.swap(new_empty_column, new_empty_row)

    def right(self):
        new_empty_column = self.empty_column +1
        new_empty_row = self.empty_row
        if not self.validate(new_empty_column, new_empty_row):
            return
        self.swap(new_empty_column, new_empty_row)

    def __str__(self):
        result = ""
        result = result + '*' * 11
        result += "\n"
        for line in self.game_field:
            result += f"{line[0]:2} {line[1]:2} {line[2]:2} {line[3]:2}"
            result += "\n"
        result += '*' * 11
        result += "\n"
        return result

    def game_finished(self):
        flatten = sum(self.game_field, [])
        is_win = (flatten[0: 15] == sorted(flatten[0: 15]))
        is_win = is_win and (flatten[0] != 0)
        return is_win
