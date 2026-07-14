def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# 盤面の初期化
board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


# お題1：石を置けるか判定する関数
def can_place(board, row, col):
    # TODO: ここに処理を書く（置けるならTrue、ダメならFalseを返す）
    if board[row][col] == '-':
        return True
    return False

# お題2：勝敗を判定する関数
def check_winner(board):
    # TODO: ここに処理を書く（'O'の勝ち, 'X'の勝ち, 'Draw', 'None'(継続) を返す）
    
    # 上がりのパターンのリスト
    lines = [
        board[0], board[1], board[2], #横列
        [board[0][0], board[1][0], board[2][0]], #左の縦列
        [board[0][1], board[1][1], board[2][1]], #真ん中の縦縦
        [board[0][2], board[1][2], board[2][2]], #右の縦縦
        [board[0][0], board[1][1], board[2][2]], #右下がり斜め
        [board[0][2], board[1][1], board[2][0]], #右上がり斜め       
    ]

    #上がりが見つかったらそのプレイヤー名を返す
    #return プレイヤー名
    for line in lines:
        if line.count('O') == 3:
            return "O"
        if line.count('X') == 3:
            return "X"
    
    #全てのマスにマークが設置されていたら'Draw'を返す
    #return 'Draw'
    if sum(line.count('-') for line in lines) == 0:
        return "Draw"
    
    #継続ならNoneを返す
    #return 'None'
    return "None"

current_player = 'O'
while True:
    print_board(board)
    print(f"プレイヤー {current_player} の番です。")
    
    try:
        print("マークを置く場所を選んでください。")
        row = int(input("タテの行を入力 (0, 1, 2): "))
        col = int(input("ヨコの列を入力 (0, 1, 2): "))
    except ValueError:
        print("※エラー：数字を入力してください！\n")
        continue
    
    #マークを置く処理を実装
    if can_place(board, row, col):
        board[row][col] = current_player
    else:
        print("置けない！")
        continue

    #プレイヤーを変更する処理を実装
    if current_player == 'O':
        current_player = 'X'
    else:
        current_player = 'O'

    # 勝敗判定、継続判定を行う
    if check_winner(board) == 'None':
        continue
    print_board(board)
    if check_winner(board) == "Draw":
        print("引き分け")
    else:
        print(check_winner(board), "の勝ち！")
    break
