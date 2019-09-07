# Graverobber game library as depicted in Petscop
# See: https://petscop.fandom.com/wiki/Graverobber
from typing import List, Tuple
import operator


class Plane(list):
    def __init__(self):
        for i in range(8):
            self.append([Empty] * 8)
        self._moves = []
        self._graves = []
        self._obstacles = []
            
    def _move_piece(self, piece, new_pos) -> None:
        current_pos = piece.position()
        self[current_pos[0]][current_pos[1]] = Empty
        self[new_pos[0]][new_pos[1]] = piece
        piece.update_position(*new_pos)

    def _moveset(self, piece) -> Tuple[int, int, int, int]:
        """Get the number of spaces a player piece can move as the tuple
        (left, right, up, down)"""
        current_pos = piece.position()
        def get_closest(position, axis, score, div_op):
            """Find the closest item to the current player position."""

            # This is a bit complicated, so I'm going to leave an explanation
            # First, we filter for only items on the path to movement in a
            # particular direction (div_op).
            # Next, we choose the item closest to the player piece. This is
            # dependent on which side of the board we're looking at so the score
            # function changes (score).
            # Axis is of course which coordinate we're analyzing, left/right or
            # up/down.
            return score([item if div_op(item.position()[axis], position[axis])
                          for item in self._obstacles],
                         key=(lambda item: item.position()[axis]))
        left_limiter = get_closest(current_pos, 0, max, operator.lt)
        right_limiter = get_closest(current_pos, 0, min, operator.gt)
        up_limiter = get_closest(current_pos, 1, max, operator.lt)
        down_limiter = get_closest(current_pos, 1, min, operator.gt)
        return (current_pos[0] - left_limiter.position()[0] + 1,
                right_limiter.position() - current_pos[0] + 1,
                current_pos[1] - up_limiter.position()[1] + 1,
                down_limiter.position() - current_pos[1] + 1)
        
    def _calc_new_position(self, move) -> Tuple[int, int]:
        current_pos = move.player.position()
        ops = {"DOWN":(operator.add, 1),
               "UP":(operator.sub, 1),
               "RIGHT":(operator.add, 0),
               "LEFT":(operator.sub, 0)}
        op = ops[move.direction]
        new_pos = list(current_pos)
        new_pos[op[1]] = op[0](new_pos[op[1]], move.spaces)
        return tuple(new_pos)
            
    def validate_move(self, move: Move) -> bool:
        new_pos = self._calc_new_position(move)
        directions = {"LEFT":0,
                      "RIGHT":1,
                      "UP":2,
                      "DOWN":3}
        if new_pos[op[1]] > 7 or new_pos[op[1]] < 0:
            return False
        elif move.spaces > self._moveset(move.player)[directions[move.direction]]:
            return False
        else:
            return True
        
    def add_move(self, move: Move):
        if not validate_move(move):
            raise InvalidMove
        self._moves.append(move)
        self._move_piece(move.player, move.
        
    def moves(self) -> List[Move]:
        return _moves

    def lost(self) -> bool:
        if False in [grave.dug() for grave in self._graves]:
            return False
        else:
            return True
    
class Empty(None):
    pass

class PlayerPiece:
    def __init__(self, name):
        self._name = name
        self.height = 1
        self.width = 1

    def position(self):
        return (self._x, self._y)

    def update_position(self, x, y):
        self._x = x
        self._y = y
            
class Obstacle:
    def __init__(self, name):
        self._name = name
        self.height = 2
        self.width = 2

    def position(self):
        return (self._x, self._y)

    def update_position(self, x, y):
        self._x = x
        self._y = y
                         
class GraveStone:
    def __init__(self, contents):
        self.height = 1
        self.width = 1

    def position(self):
        return (self._x, self._y)

    def update_position(self, x, y):
        self._x = x
        self._y = y
                         
    def dig(self) -> None:
        self._dug = True
        
    def dug(self) -> bool:
        return _dug

class GravePatch:
    def __init__(self, contents):
        self.height = 1
        self.width = 1

    def position(self):
        return (self._x, self._y)

    def update_position(self, x, y):
        self._x = x
        self._y = y
                         
    def dig(self) -> None:
        self._dug = True
        
    def dug(self) -> bool:
        return _dug
                         
        
class Move:
    def __init__(self, player, direction, spaces):
        self.player = player
        self.direction = direction
        self.spaces = spaces

class InvalidMove(Exception):
    pass
