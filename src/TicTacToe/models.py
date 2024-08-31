from django.db import models

class TTTGame(models.Model):
    player_turn: bool = models.BooleanField()
    board_str: str = models.CharField(max_length=9) 

    def get_pos(self, pos: int) -> int:
        player = int(self.board_str[pos])
        if (player < 0 or 2 < player):
            assert "A case in the board should have a value between 0 and 2"
        
        return player

    def get_board_as_list(self) -> list:
        if (len(self.board_str) != 9):
            assert "It is impossible to have a board with more or less than 9 box"
        
        board_as_list = [
            [self.get_pos(0), self.get_pos(1), self.get_pos(2)], 
            [self.get_pos(3), self.get_pos(4), self.get_pos(5)], 
            [self.get_pos(6), self.get_pos(7), self.get_pos(8)], 
        ]
        return board_as_list


