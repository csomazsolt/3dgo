import os
import sys
import pytest

# Ensure the project root is on the Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from game3dgo import Game3DGo


def test_previous_board_tracking():
    game = Game3DGo(2)
    assert len(game.previousBoards) == 1  # initial empty board
    assert game.placeStone(0, 0, 0, 1) is True
    assert len(game.previousBoards) == 2


def test_ko_rule_blocks_repetition():
    game = Game3DGo(2)
    assert game.placeStone(0, 0, 0, 1) is True
    # simulate capture bringing board back to empty state
    game.board[0][0][0] = 0
    assert game.placeStone(0, 0, 0, 1) is False
    assert game.warning == 'koRule'
