import random
def P_moves(x, y):
    moves = []
    if (x < 3): 
        moves.append('D')
    if (x > 0): 
        moves.append('U')
    if (y < 3): 
        moves.append('R')
    if (y > 0): moves.append('L')
    return moves

def Matrix_Random(rows, cols):
    matrix = [[random.randint(0,1) for _ in range(cols)] for _ in range(rows)]
    return matrix

def Thuchien(action, matrix, x, y):
    if action == 'D':
        x += 1
    elif action == 'U':
        x -= 1
    elif action == 'R':
        y += 1
    elif action == 'L':
        y -= 1

    return matrix[x][y], x, y

def is_full_zero(matrix): # kiểm tra nhà sạch chưa 
    return sum(sum(row) for row in matrix) == 0

# khai báo ban đầu
m_matrix = Matrix_Random(4, 4)
i, j = 0, 0
state = m_matrix[i][j]

# chạy chương trình
while (True):
    moves = P_moves(i, j) # các chiều có thế chọn
    action = random.choice(moves) #chọn chiều ngẫu nhiên trong moves
    if state == 1: 
        m_matrix[i][j] = 0
    state, i, j = Thuchien(action, m_matrix, i, j) #thực hiện chiều đã trọn ở trên
    print(m_matrix)

    #kiểm tra mảng full 0 chưa
    if is_full_zero(m_matrix): 
        print("successfully")
        break
            