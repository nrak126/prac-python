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
    pass

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
    
    #全てのマスにマークが設置されていたら'Draw'を返す
    #return 'Draw'
    
    #継続ならNoneを返す
    #return 'None'
    
    pass

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
    #プレイヤーを変更する処理を実装
    # 勝敗判定、継続判定を行う
    
    