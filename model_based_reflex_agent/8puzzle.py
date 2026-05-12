import random
def P_moves(x, y):
    moves = []
    if (x < 2): 
        moves.append('D')
    if (x > 0): 
        moves.append('U')
    if (y < 2): 
        moves.append('R')
    if (y > 0): moves.append('L')
    return moves

# hàm tạo mảng ngẫu nhiên ban đầu
def matrix_random():
    numbers = list(range(9))  # [0,1,2,3,4,5,6,7,8]
    random.shuffle(numbers)   # đảo ngẫu nhiên
    return [numbers[i:i+3] for i in range(0, 9, 3)]

#tìm vị trí trống
def find_zero(matrix):
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                return i, j
            
# cập nhật trạng thái sau hành động
def update_state(state, action):
    x, y = find_zero(state)

    new_state = [row[:] for row in state]

    if action == "U":
        new_state[x][y], new_state[x - 1][y] = new_state[x - 1][y], new_state[x][y]

    elif action == "D":
        new_state[x][y], new_state[x + 1][y] = new_state[x + 1][y], new_state[x][y]

    elif action == "L":
        new_state[x][y], new_state[x][y - 1] = new_state[x][y - 1], new_state[x][y]

    elif action == "R":
        new_state[x][y], new_state[x][y + 1] = new_state[x][y + 1], new_state[x][y]

    return new_state

# Hành động ngược lại
# để tránh đi tới rồi quay lại ngay
def opposite(action):
    opposite_moves = {
        "U": "D",
        "D": "U",
        "L": "R",
        "R": "L"
    }
    return opposite_moves.get(action)


# RULE-MATCH
# chọn random action
# nhưng loại bỏ action ngược
# với hành động vừa thực hiện
def rule_match(state, last_action):
    x, y = find_zero(state)
    possible = P_moves(x, y)

    # loại bỏ hành động ngược với bước trước
    if last_action:
        reverse = opposite(last_action)
        if reverse in possible and len(possible) > 1:
            possible.remove(reverse)

    return random.choice(possible)

# In ma trận
def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# khởi tạo mảng random
state = matrix_random()

print("Trạng thái ban đầu:")
print_matrix(state)

step = 0
max_step = 50
last_action = None

check = True
while state != goal and step < max_step:
    # percept = trạng thái hiện tại
    percept = state

    # chọn action
    action = rule_match(percept, last_action)

    print(f"Bước {step + 1}: Action = {action}")

    # cập nhật state
    state = update_state(state, action)

    print_matrix(state)

    # lưu action vừa thực hiện
    last_action = action
    step += 1

if state == goal:
    print("Đã đạt trạng thái đích!")
else:
    print("Chưa đạt trạng thái đích sau", max_step, "bước.")