import json
from copy import deepcopy


class Game3DGo:
    """Minimal 3D Go engine with Ko rule tracking."""

    def __init__(self, size):
        self.size = size
        # board[z][y][x]
        self.board = [
            [
                [0 for _ in range(size)]
                for _ in range(size)
            ]
            for _ in range(size)
        ]
        # history of serialized board states
        self.previousBoards = [self._serialize_board(self.board)]
        self.warning = None

    def _serialize_board(self, board):
        """Return a JSON string representation of the board."""
        return json.dumps(board, sort_keys=True)

    def placeStone(self, x, y, z, color):
        """Attempt to place a stone.

        Returns True if the move is accepted. If the resulting
        board state matches a previous one, the move is blocked
        and `warning` is set to 'koRule'.
        """
        if self.board[z][y][x] != 0:
            self.warning = 'occupied'
            return False

        new_board = deepcopy(self.board)
        new_board[z][y][x] = color
        serial = self._serialize_board(new_board)
        if serial in self.previousBoards:
            self.warning = 'koRule'
            return False

        self.board = new_board
        self.previousBoards.append(serial)
        self.warning = None
        return True
