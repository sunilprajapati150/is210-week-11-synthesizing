#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Synthesizing task to make a chess move tracker"""

class ChessPiece(object):
    
    """Represents starting positon"""
    
    import time
    prefix = ''

    def __init__(self, position):
        if ChessPiece.is_legal_move(self, position):
            self.position = position
            self.moves = []
        else:
            excep = "`{}` not legal position to start at"
            raise ValueError(excep.format(position))

    def algebraic_to_numeric(self, tile):
        """Helps to find legal moves"""
        if len(tile) == 2:
            x_coord = "abcdefgh".find(tile[0])
            y_coord = "12345678".find(tile[1])
            if x_coord != -1 and y_coord != -1:
                return (x_coord, y_coord)
        return None

    def is_legal_move(self, position):
        """Tells if the move is legal"""

        if self.algebraic_to_numeric(position) is None:
            return False
        else:
            return True

    def move(self, position):
        """Actually makes a move"""

        if self.is_legal_move(position):
            oldposition = self.position
            self.position = position
            timestamp = self.time.time()
            the_tup = (oldposition, position, timestamp)
            self.moves.append(the_tup)
            return the_tup
        else:
            return False


class Rook(ChessPiece):
    """Creating Rook"""

    prefix = "R"

    def is_legal_move(self, position):
        cur_pos = self.algebraic_to_numeric(self.position)
        new_pos = self.algebraic_to_numeric(position)
        if new_pos is not None:
            if cur_pos[0] == new_pos[0] or cur_pos[1] == new_pos[1]:
                return True
        return False


class Bishop(ChessPiece):
    """Creating Bishop"""
    prefix = 'B'

    def is_legal_move(self, position):
        """Legal position """
        cur_pos = self.algebraic_to_numeric(self.position)
        new_pos = self.algebraic_to_numeric(position)
        if new_pos is not None:
            if abs(cur_pos[0] - new_pos[0]) == abs(cur_pos[1] - new_pos[1]):
                return True
        return False


class King(ChessPiece):
    """Creating the king"""

    prefix = "K"

    def is_legal_move(self, position):
        """Position: alpha/num pair """
        cur_pos = self.algebraic_to_numeric(self.position)
        new_pos = self.algebraic_to_numeric(position)
        if new_pos is not None:
            if abs(cur_pos[0] - new_pos[0]) <= 1 and \
               abs(cur_pos[1] - new_pos[1]) <= 1:
                return True
        return False


class ChessMatch(object):
    """Creates the chessboard and keep tracks of the moves"""

    def __init__(self, pieces=None):
        if pieces is None:
            self.reset()
        else:
            self.pieces = pieces
            self.log = []

    def reset(self):
        """ resets the board"""
        self.log = []
        self.pieces = {'Ra1': Rook('a1'), 'Rh1': Rook('h1'),
                       'Ra8': Rook('a8'), 'Rh8': Rook('h8'),
                       'Bc1': Bishop('c1'), 'Bf1': Bishop('f1'),
                       'Bc8': Bishop('c8'), 'Bf8': Bishop('f8'),
                       'Ke1': King('e1'), 'Ke8': King('e8')}

    def move(self, piece, new_pos):
        """Keeps track of the moves made """
        result = self.pieces[piece].move(new_pos)
        if result is not False:
            self.log.append(result)
            new_ent = self.pieces[piece].prefix + new_pos
            self.pieces[new_ent] = self.pieces.pop(piece)
        return False

    def __len__(self):
        return len(self.log)
