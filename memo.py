def calculator():
    while True: #無限ループ(breakまで)
        expression = input("計算式を入力してください（例: 3 + 5）: ")
        
        # exitでbreak
        if expression.lower() == "exit":
            print("電卓を終了します。")
            break

        # tryでエラーがあってもキャッチ
        try:
            # eval:文字列をPythonのコードとして実行する関数
            result = eval(expression)
            print("結果:", result)
        # エラーキャッチ
        # エラー名 as eでeにエラー詳細を格納
        except Exception as e:
            print("エラー:", e)

calculator()
# evalすげえ...


import ast
import math

def safe_eval(expression):
    """安全に数式を評価する"""
    try:
        # ast:Abstract Syntax Tree"（抽象構文木）
        # parseで木を作る
        # eval()の安全版
        tree = ast.parse(expression, mode='eval')

        # 許可する演算子のみ使用可（+ - * / ** ()）
        allowed_operators = {ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow}

        # 全てのnodeを順番にエラーチェック
        # node:ast.*(数値・演算子・式)
        for node in ast.walk(tree):
        # 入力値の演算子 && 許可演算子
        # isinstance(変数, 型):変数が型か？
        # BinOp(Binary Operation（2項演算))許可演算子か？  
        # typeは()の型を取得　　演算子を取得（Operator = 演算子）
            if isinstance(node, ast.BinOp) and type(node.op) not in allowed_operators:
                # raiseでエラーを手動で発生
                raise ValueError("使用できない演算子があります！")
            # Expression:単一式, BinOp:二項演算子, Constant:数値, UnaryOp:単項演算(-x, +x), Pow:累乗, Call:関数
            if not isinstance(node, (ast.Expression, ast.BinOp, ast.Constant, ast.UnaryOp, ast.Pow, ast.Call)):
                raise ValueError("安全でない式です！")
        # 辞書                     組み込み関数を無効化     　math.sqrt()などのみ許可
        return eval(expression, {"__builtins__": None}, {"math": math})
    except Exception as e:
        # 戻り値でエラーを返す
        # fで文字列の中に変数や式を埋め込める
        return f"エラー: {e}"

def calculator():
    while True:
        expression = input("計算式を入力 (`exit` で終了) : ")

        if expression.lower() in ["exit", "quit"]:
            print("電卓を終了")
            break

        result = safe_eval(expression)
        print("結果:", result)

calculator()



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "エラー: 0で割ることはできません"
    return a / b

def calculator():
    while True:
        print("\n【電卓】")
        print("1: 足し算（+）")
        print("2: 引き算（-）")
        print("3: 掛け算（×）")
        print("4: 割り算（÷）")
        print("5: 終了")
        
        choice = input("選択してください: ")
        
        if choice == "5":
            print("電卓を終了します。")
            break
        
        num1 = float(input("1つ目の数値: "))
        num2 = float(input("2つ目の数値: "))

        if choice == "1":
            print("結果:", add(num1, num2))
        elif choice == "2":
            print("結果:", subtract(num1, num2))
        elif choice == "3":
            print("結果:", multiply(num1, num2))
        elif choice == "4":
            print("結果:", divide(num1, num2))
        else:
            print("無効な入力です。")

calculator()


