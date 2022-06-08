# # Dado uma matriz 2D e uma palavra, identifique se esta determinada palavra está dentro da matriz.
# #
# # A palavra pode ser construída a partir de letras que estão sequenciais em valores adjacentes, onde valores
# # adjacentes são aqueles que estão horizontalmente ou verticalmente por perto.
# #
# # LEMBRE-SE: a mesma letra não pode ser usada duas vezes para construir uma palavra.
# #
# # board = [
# #           ['A','B','C','E'],
# #           ['S','F','C','S'],
# #           ['A','D','E','E']
# #         ]
# # Dada a palavra = "ABCCED", retorne true.
# # Dada a palavra = "SEE", retorne true.
# # Dada a palavra = "ABCB", retorne false.
#
# def solution(board,word):
#     if len(word) == 0 :
#         return False
#     for x in range(len(board)):
#         for y in range(len(board[x])):
#             if board[x][y] == word[0]:
#                 move = (x,y)
#                 if deep_first_search(move, [move], word, 0, board):
#                     return True and print('Ok')
#     return False and print('shit')
# def deep_first_search(current_move,visited_paths, expected_word, word_index, board):
#     if word_index + 1 >= len(expected_word):
#         return True and print('Ok')
#
#     x, y = current_move
#     possible_moves = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
#     board_x_size = len(board)
#     board_y_size = len(board[0])
#
#     for move_x, move_y in possible_moves:
#         if move_x >= 0 and move_x < board_x_size and move_y >= 0 and move_y < board_y_size:
#             if board[move_x][move_y] == expected_word[word_index + 1]:
#                 if (move_x, move_y) not in visited_paths:
#                     next_move = (move_x, move_y)
#                     if deep_first_search(next_move, visited_paths + [next_move], expected_word, word_index + 1,board):
#                         return True and print('Ok')
#     return False and print('Shit')
#
# solution([
#            ['A','B','C','E'],
#            ['S','F','C','S'],
#            ['A','D','E','E']
#         ], 'SEE')
#
