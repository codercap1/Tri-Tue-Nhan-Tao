import random

# xác định các hướng có thể đi từ vị trí (x, y)
def P_moves(x, y, last_action):
    moves = []

    if x < 3:
        moves.append('D')   # xuống
    if x > 0:
        moves.append('U')   # lên
    if y < 3:
        moves.append('R')   # phải
    if y > 0:
        moves.append('L')   # trái

    # loại bỏ hướng ngược lại với bước vừa đi
    opposite = {
        'D': 'U',
        'U': 'D',
        'R': 'L',
        'L': 'R'
    }

    if last_action in opposite:
        reverse_move = opposite[last_action]
        if reverse_move in moves:
            moves.remove(reverse_move)

    return moves


def Matrix_Random(rows, cols):
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]


def Update_State(state, action, model):
    x, y = state

    if action == 'D':
        x += 1
    elif action == 'U':
        x -= 1
    elif action == 'R':
        y += 1
    elif action == 'L':
        y -= 1

    percept = model[x][y]
    return (x, y), percept


def Rule_Match(state, percept, last_action):
    x, y = state

    # nếu ô bẩn thì hút bụi
    if percept == 1:
        return "CLEAN"

    # nếu sạch thì chọn hướng ngẫu nhiên nhưng không quay đầu ngay
    moves = P_moves(x, y, last_action)
    return random.choice(moves)


def is_full_zero(matrix):
    return sum(sum(row) for row in matrix) == 0


model = Matrix_Random(4, 4)
state = (0, 0)
action = None
last_move = None
percept = model[0][0]

print("Ma trận ban đầu:")
for row in model:
    print(row)

print("\nBắt đầu chạy Agent:\n")

while True:

    # cập nhật trạng thái nếu hành động trước là di chuyển
    if action is not None and action != "CLEAN":
        state, percept = Update_State(state, action, model)
        last_move = action

    # chọn luật
    action = Rule_Match(state, percept, last_move)

    x, y = state

    # thực hiện hành động
    if action == "CLEAN":
        model[x][y] = 0
        percept = 0
        print(f"Hút bụi tại ({x}, {y})")

    else:
        print(f"Di chuyển {action} từ ({x}, {y})")

    for row in model:
        print(row)
    print()

    if is_full_zero(model):
        print("Successfully! Nhà đã sạch hoàn toàn.")
        break