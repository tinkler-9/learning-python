a = [0]*8
board=[a]*8
print(board)
print('----')
a[1] = 2
print(board)
print('----')
board2 = [[0] * 8 for _ in range(8)]
print(board2)
print('----')
board2[0][1] = 2
print(board2)
print('----')
board3 = []
for _ in range(8):
    board3.append([0] * 8)
print(board3)