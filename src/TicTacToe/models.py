from django.db import models

class TTTGame(models.Model):
    player_turn: bool = models.BooleanField(default=True)
    board_str: str = models.CharField(max_length=9, default="000000000") 

    def current_player(self) -> int:
        return 1 if self.player_turn else 2

    def pos(self, pos: int) -> int:
        player = int(self.board_str[pos])
        if (player < 0 or 2 < player):
            assert "A case in the board should have a value between 0 and 2"
        
        return player

    def board(self) -> list:
        if (len(self.board_str) != 9):
            assert "It is impossible to have a board with more or less than 9 box"
        
        board_as_list = [
            [self.pos(0), self.pos(1), self.pos(2)], 
            [self.pos(3), self.pos(4), self.pos(5)], 
            [self.pos(6), self.pos(7), self.pos(8)], 
        ]
        return board_as_list


